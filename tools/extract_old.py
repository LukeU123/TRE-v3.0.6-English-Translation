import sys,pickle,re,json;sys.path.insert(0,'tools');from g3text import *
d=open('rom_en/old.gba','rb').read()
P=pickle.load(open('work/ptrs_old.pkl','rb'))
REG=[(0x200000,0x500000),(0x5A0000,0x5C0000),(0x800000,0xA00000),(0xE00000,0x1200000)]
inreg=lambda o:any(a<=o<b for a,b in REG)
cands=set(t for t in P if inreg(t))
for a,b in REG:
    i=d.find(b'\xff',a)
    while 0<=i<b: cands.add(i+1); i=d.find(b'\xff',i+1)
groups={}
for o in cands:
    s,e=decode(d,o,1500)
    if s is None or len(s)<2: continue
    groups.setdefault(e,[]).append(o)
def kind(o):
    refs=P.get(o,[])
    if any(d[r-2:r]==b'\x0f\x00' or d[r-1] in (0x67,0x0f) for r in refs): return 0
    if refs and d[o-1] in (0xff,0x00): return 1
    if any(r%4==0 for r in refs): return 2
    if d[o-1] in (0xff,0x00): return 3
    return 9
out=[]
for e,starts in groups.items():
    starts.sort()
    best=min(starts,key=lambda o:(kind(o),o))
    if kind(best)==9: continue
    s,_=decode(d,best)
    letters=sum(c.isalpha() for c in s)
    if letters<2 or letters/len(s)<0.45: continue
    if re.search(r'[ÀÂÇÈÊËÌÎÏÒÔŒÙÛßàâçèêëìîïòôœùûÄÖÜäöü×]',s): continue
    if re.search(r'(.)\1\1\1',s): continue
    out.append(dict(off=best,end=e,refs=P.get(best,[]),kind=kind(best),text=s))
out.sort(key=lambda x:x['off'])
json.dump(out,open('work/old_strings.json','w'),ensure_ascii=False)
print(len(out),sum(len(x['text']) for x in out))
