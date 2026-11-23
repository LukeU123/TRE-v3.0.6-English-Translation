import sys,json,glob,re;sys.path.insert(0,'/home/claude/tools');from g3text import *
W=json.load(open('/home/claude/work/gfx/normal_widths.json'))
VARW={'V01':42}
def linew(s):
    w=0;i=0
    while i<len(s):
        if s[i]=='{':
            j=s.index('}',i);tok=s[i+1:j]
            if tok[0]=='V': w+=VARW.get(tok,60)
            i=j+1;continue
        if s[i]=='[':
            j=s.index(']',i);w+=W[R[s[i:j+1]]];i=j+1;continue
        ch=s[i]
        if ch=="'":ch='’'
        if ch=='"':ch='”'
        w+=W[R[ch]] if ch in R else 6;i+=1
    return w
def lines(s): return re.split(r'\\[nlp]',s)
def check(files=None):
    S={x['off']:x for x in json.load(open('/home/claude/work/strings.json'))}
    out=[]
    for f in files or sorted(glob.glob('/home/claude/work/tr/*.txt')):
        for l in open(f,encoding='utf-8'):
            if '|' not in l: continue
            k,v=l.rstrip('\n').split('|',1);o=int(k,16)
            if o not in S: continue
            es=max(linew(x) for x in lines(S[o]['text']))
            lim=max(es,216)
            for x in lines(v):
                w=linew(x)
                if w>lim+2: out.append((f.split('/')[-1],k,w,lim,x));break
    return out
if __name__=='__main__':
    r=check(sys.argv[1:] or None);print(len(r))
    import collections;print(collections.Counter(a for a,*_ in r).most_common(40))
    for x in r[:25]: print(x)
