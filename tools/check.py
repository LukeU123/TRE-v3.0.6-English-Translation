# usage: python3 tools/check.py work/tr/FILE.txt   -> reports problems; exit code 1 if any
import sys,json,re;sys.path.insert(0,'/home/claude/tools');from g3text import encode
src=open('/home/claude/rom/PkmnTeamRocket.gba','rb').read()
S={x['off']:x for x in json.load(open('/home/claude/work/strings.json'))}
def goodrefs(x):
    o=x['off'];return [r for r in x['refs'] if r%4==0 or src[r-2:r]==b'\x0f\x00' or src[r-1]==0x67 or (0x1e0000<=r<0x500000 and src[o-1] in (0xff,0x00))]
split=lambda s:re.split(r'\\[nlp]',re.sub(r'\{[^}]*\}','',s))
lead=lambda t:len(t)-len(t.lstrip(' '))
bad=0;n=0
for i,ln in enumerate(open(sys.argv[1],encoding='utf-8'),1):
    ln=ln.rstrip('\n')
    if not ln.strip(): continue
    if '|' not in ln: print('line %d: no | separator'%i);bad+=1;continue
    k,en=ln.split('|',1);n+=1
    try:o=int(k,16);x=S[o]
    except Exception: print('line %d: unknown offset %s'%(i,k));bad+=1;continue
    p=[]
    try:b=encode(en)
    except Exception as e: p.append('bad character/code %r'%(e,))
    else:
        if len(b)>x['end']-o and not goodrefs(x): p.append('TOO LONG for FIXED string: %d bytes > budget %d'%(len(b),x['end']-o))
    if sorted(re.findall(r'\{[^}]*\}',x['text']))!=sorted(re.findall(r'\{[^}]*\}',en)): p.append('control codes differ from source')
    if lead(x['text'])!=lead(en): p.append('leading spaces differ (%d vs %d)'%(lead(x['text']),lead(en)))
    mx=max(max(len(l) for l in split(x['text'])),34)
    for l in split(en):
        if len(l)>mx+1: p.append('line too long (%d>%d): %s'%(len(l),mx,l))
    for q in p: print('line %d (%s): %s'%(i,k,q));bad+=1
print('%d entries checked, %d problems'%(n,bad));sys.exit(1 if bad else 0)
