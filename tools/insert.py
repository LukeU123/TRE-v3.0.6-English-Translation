import sys,json,pickle,struct,zlib;sys.path.insert(0,'tools');from g3text import *
src=open('rom/PkmnTeamRocket.gba','rb').read();d=bytearray(src)
kept={x['off']:x for x in json.load(open('work/kept.json'))}
tr={}
for f in sys.argv[2:]: tr.update({int(k,16):v for k,v in json.load(open(f)).items()})
# free space: last big FF run
FREE=None
run=0
for o in range(len(d)-1,0x1000000,-1):
    if d[o]==0xFF: run+=1
    else:
        if run>0x10000: FREE=o+1+16; break
        run=0
FREE=(FREE+3)&~3; print('free space from',hex(FREE)); inplace=moved=0
for off,en in tr.items():
    x=kept[off]; b=encode(en); oldlen=x['end']-off
    if len(b)<=oldlen:
        d[off:off+oldlen]=b+b'\xff'*(oldlen-len(b)); inplace+=1
    else:
        d[FREE:FREE+len(b)]=b
        for r in x['refs']: struct.pack_into('<I',d,r,FREE+0x08000000)
        FREE=(FREE+len(b)+3)&~3; moved+=1
print('in place',inplace,'repointed',moved)
open(sys.argv[1],'wb').write(d)
# BPS
def vi(n):
    o=bytearray()
    while True:
        x=n&0x7f;n>>=7
        if n==0:o.append(0x80|x);break
        o.append(x);n-=1
    return bytes(o)
p=bytearray(b'BPS1')+vi(len(src))+vi(len(d))+vi(0)
i=0;N=len(d)
while i<N:
    j=i
    if src[i]==d[i]:
        while j<N and src[j]==d[j]:j+=1
        p+=vi(((j-i-1)<<2)|0)
    else:
        while j<N and src[j]!=d[j]:j+=1
        p+=vi(((j-i-1)<<2)|1)+d[i:j]
    i=j
p+=struct.pack('<I',zlib.crc32(src))+struct.pack('<I',zlib.crc32(d))
p+=struct.pack('<I',zlib.crc32(p))
open(sys.argv[1].rsplit('.',1)[0]+'.bps','wb').write(p);print('bps',len(p))
