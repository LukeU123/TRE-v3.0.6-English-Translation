# usage: build.py  -> applies all work/tr/*.json, writes out/*.gba + .bps, prints warnings
import sys,json,glob,struct,zlib,re;sys.path.insert(0,'tools');from g3text import *
src=open('rom/PkmnTeamRocket.gba','rb').read();d=bytearray(src)
S={x['off']:x for x in json.load(open('work/strings.json'))}
old={x['off']:x for x in json.load(open('work/kept.json'))}
tr={}
for f in sorted(glob.glob('work/tr/*')):
    if f.endswith('.json'): tr.update({int(k,16):v for k,v in json.load(open(f)).items()})
    elif f.endswith('.txt'):
        for ln in open(f,encoding='utf-8'):
            ln=ln.rstrip('\n')
            if '|' in ln and not ln.startswith('#'):
                k,v=ln.split('|',1);tr[int(k,16)]=v
FREE=0x1cdadc0;warn=[];inp=mov=0
def goodrefs(x):
    o=x['off']
    return [r for r in x['refs'] if r%4==0 or src[r-2:r]==b'\x0f\x00' or src[r-1]==0x67 or (0x1e0000<=r<0x500000 and src[o-1] in (0xff,0x00))]
split=lambda s:re.split(r'\\[nlp]',re.sub(r'\{[^}]*\}','',s))
for off,en in sorted(tr.items()):
    x=S.get(off)
    if x is None: warn.append('%x unknown string'%off);continue
    try:b=encode(en)
    except Exception as e: warn.append('%x encode error %r'%(off,e));continue
    es_codes=re.findall(r'\{[^}]*\}|\\[nlp]',x['text']);en_codes=re.findall(r'\{[^}]*\}',en)
    if sorted(c for c in es_codes if c.startswith('{'))!=sorted(en_codes): warn.append('%x control codes differ'%off)
    mx=max(max(len(l) for l in split(x['text'])),34)
    for l in split(en):
        if len(l.replace('{','')) >mx+1: warn.append('%x long line (%d>%d): %s'%(off,len(l),mx,l))
    lead=lambda t:len(t)-len(t.lstrip(' '))
    if lead(x['text'])!=lead(en): warn.append('%x LEADING SPACES differ'%off)
    n=x['end']-off
    if len(b)<=n: d[off:off+n]=b+b'\xff'*(n-len(b));inp+=1
    elif goodrefs(x):
        d[FREE:FREE+len(b)]=b
        for r in goodrefs(x): struct.pack_into('<I',d,r,FREE+0x08000000)
        FREE=(FREE+len(b)+3)&~3;mov+=1
    else: warn.append('%x TOO LONG and unpointed (%d>%d): %s'%(off,len(b),n,en))
print('strings',len(tr),'in place',inp,'moved',mov,'free ptr',hex(FREE))
for w in warn:print('WARN',w)
open('out/PkmnTeamRocket_EN.gba','wb').write(d)
def vi(n):
    o=bytearray()
    while True:
        x=n&0x7f;n>>=7
        if n==0:o.append(0x80|x);break
        o.append(x);n-=1
    return bytes(o)
p=bytearray(b'BPS1')+vi(len(src))+vi(len(d))+vi(0);i=0;N=len(d)
while i<N:
    j=i
    if src[i]==d[i]:
        while j<N and src[j]==d[j]:j+=1
        p+=vi(((j-i-1)<<2))
    else:
        while j<N and src[j]!=d[j]:j+=1
        p+=vi(((j-i-1)<<2)|1)+d[i:j]
    i=j
p+=struct.pack('<II',zlib.crc32(src),zlib.crc32(d));p+=struct.pack('<I',zlib.crc32(p))
open('out/PkmnTeamRocket_EN.bps','wb').write(p)
