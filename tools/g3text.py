import re
T={0x00:' ',0x01:'À',0x02:'Á',0x03:'Â',0x04:'Ç',0x05:'È',0x06:'É',0x07:'Ê',0x08:'Ë',0x09:'Ì',0x0B:'Î',0x0C:'Ï',0x0D:'Ò',0x0E:'Ó',0x0F:'Ô',0x10:'Œ',0x11:'Ù',0x12:'Ú',0x13:'Û',0x14:'Ñ',0x15:'ß',0x16:'à',0x17:'á',0x19:'ç',0x1A:'è',0x1B:'é',0x1C:'ê',0x1D:'ë',0x1E:'ì',0x20:'î',0x21:'ï',0x22:'ò',0x23:'ó',0x24:'ô',0x25:'œ',0x26:'ù',0x27:'ú',0x28:'û',0x29:'ñ',0x2A:'º',0x2B:'ª',0x2D:'&',0x2E:'+',0x34:'[Lv]',0x35:'=',0x36:';',0x51:'¿',0x52:'¡',0x53:'[PK]',0x54:'[MN]',0x5A:'Í',0x5B:'%',0x5C:'(',0x5D:')',0x68:'â',0x6F:'í',0x85:'<',0x86:'>',0xAB:'!',0xAC:'?',0xAD:'.',0xAE:'-',0xAF:'·',0xB0:'…',0xB1:'“',0xB2:'”',0xB3:'‘',0xB4:'’',0xB5:'♂',0xB6:'♀',0xB7:'$',0xB8:',',0xB9:'×',0xBA:'/',0xF0:':',0xF1:'Ä',0xF2:'Ö',0xF3:'Ü',0xF4:'ä',0xF5:'ö',0xF6:'ü'}
for i in range(10):T[0xA1+i]=str(i)
for i in range(26):T[0xBB+i]=chr(65+i);T[0xD5+i]=chr(97+i)
FCARGS={1:1,2:1,3:1,4:3,5:1,6:1,8:1,0xB:2,0xC:1,0xD:1,0xE:1,0x10:2,0x11:1,0x12:1,0x13:1,0x14:1,0x19:1}
R={v:k for k,v in T.items()}
def decode(d,o,maxlen=2000):
    s=[];i=o
    while i<len(d) and i-o<maxlen:
        b=d[i]
        if b==0xFF: return ''.join(s),i+1
        if b in T: s.append(T[b]);i+=1
        elif b==0xFE: s.append('\\n');i+=1
        elif b==0xFA: s.append('\\l');i+=1
        elif b==0xFB: s.append('\\p');i+=1
        elif b==0xFD: s.append('{V%02X}'%d[i+1]);i+=2
        elif b==0xFC:
            c=d[i+1];n=FCARGS.get(c,0)
            s.append('{C'+''.join('%02X'%x for x in d[i+1:i+2+n])+'}');i+=2+n
        else: return None,i
    return None,i
def encode(s):
    out=bytearray();i=0
    while i<len(s):
        if s.startswith('\\n',i):out.append(0xFE);i+=2;continue
        if s.startswith('\\l',i):out.append(0xFA);i+=2;continue
        if s.startswith('\\p',i):out.append(0xFB);i+=2;continue
        if s[i]=='{':
            j=s.index('}',i);tok=s[i+1:j]
            if tok[0]=='V':out+=bytes([0xFD,int(tok[1:],16)])
            else:out.append(0xFC);out+=bytes.fromhex(tok[1:])
            i=j+1;continue
        if s[i]=='[':
            j=s.index(']',i);out.append(R[s[i:j+1]]);i=j+1;continue
        ch=s[i]
        if ch in "'":ch='’'
        if ch=='"':ch='”'
        out.append(R[ch]);i+=1
    out.append(0xFF);return bytes(out)
