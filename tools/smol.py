import struct
def _tmpl(x):
    if x==0: return 0
    if x>=64: return (0)|((x-64)<<8)
    k=6-(x.bit_length()-1)
    return (k&7)|(((x<<k)-64)<<8)|(((1<<k)-1)<<16)
TMPL=[_tmpl(x) for x in range(128)]
def build_table(freqwords):
    f=[0]*16
    for i in range(3):
        w=freqwords[i]
        for j in range(5): f[i*5+j]=(w>>(6*j))&0x3f
        f[15]+=(w&0xC0000000)>>(30-2*i)
    t=[]
    for s in range(16):
        for j in range(f[s]): t.append(TMPL[f[s]+j]|(s<<3))
    assert len(t)==64,(len(t),f)
    return t
class Stream:
    def __init__(s,words,pos,state):
        s.w=words;s.p=pos;s.bits=words[pos];s.bi=0;s.state=state
    def nib(s,t):
        yk=t[s.state];sym=(yk&0xff)>>3;k=yk&7;mask=yk>>16
        s.state=((yk>>8)&0xff)+((s.bits>>s.bi)&mask);s.bi+=k
        if s.bi>=32:
            s.p+=1;s.bits=s.w[s.p] if s.p<len(s.w) else 0;s.bi-=32
            if s.bi: s.state+=(s.bits&((1<<s.bi)-1))<<(k-s.bi)
        return sym
def header(d,o):
    w0,w1=struct.unpack_from('<II',d,o)
    return dict(mode=w0&15,imageSize=(w0>>4)&0x3fff,symSize=(w0>>18)&0x3fff,initialState=w1&0x3f,bitstreamSize=(w1>>6)&0x1fff,loSize=(w1>>19)&0x1fff)
def decode(d,o):
    h=header(d,o);mode=h['mode'];base=o+8
    nwords=4096*4
    words=list(struct.unpack_from('<%dI'%min(nwords,(len(d)-base)//4),d,base))
    lo_enc=mode in (4,5,6);sym_enc=mode in (2,3,5,6);delta=mode in (3,6)
    loS,symS=h['loSize'],h['symSize']
    if mode==1:
        sym=list(struct.unpack_from('<%dH'%symS,d,base));lo=d[base+symS*2:base+symS*2+loS]
    else:
        if mode==4: loF=words[0:3];sp=3
        elif mode in (2,3): symF=words[0:3];sp=3
        else: loF=words[0:3];symF=words[3:6];sp=6
        st=Stream(words,sp,h['initialState'])
        left=base
        if lo_enc:
            t=build_table(loF);lo=bytearray()
            for i in range(loS):
                a=st.nib(t);b=st.nib(t);lo.append(a|(b<<4))
            left+=12
        if sym_enc:
            t=build_table(symF);sym=[];cur=0
            for i in range(symS):
                v=0
                for n in range(4):
                    x=st.nib(t)
                    if delta: cur=(cur+x)&15;x=cur
                    v|=x<<(4*n)
                sym.append(v)
            left+=12
        left+=4*h['bitstreamSize']
        if not sym_enc: sym=list(struct.unpack_from('<%dH'%symS,d,left));left+=symS*2
        if not lo_enc: lo=d[left:left+loS]
    out=[];si=0;i=0
    while i<loS:
        if lo[i]&0x80:
            ln=(lo[i]&0x7f)|(lo[i+1]<<7);off=lo[i+2]&0x7f
            if lo[i+2]&0x80: off|=lo[i+3]<<7;i+=4
            else: i+=3
        else:
            ln=lo[i]&0x7f;off=lo[i+1]&0x7f
            if lo[i+1]&0x80: off|=lo[i+2]<<7;i+=3
            else: i+=2
        if ln:
            v=sym[si];si+=1;out.append(v)
            if off==1: out.extend([v]*ln)
            else:
                for _ in range(ln): out.append(out[-off])
        else:
            out.extend(sym[si:si+off]);si+=off
    b=struct.pack('<%dH'%len(out),*out)
    return b[:h['imageSize']*4],h
