import sys,re,json;sys.path.insert(0,'/home/claude/tools');import pxcheck
def rewrap(v,limit):
    boxes=v.split('\\p');out=[]
    for b in boxes:
        words=re.split(r'(\\[nl])',b)
        text=''.join(' ' if w in ('\\n','\\l') else w for w in words)
        toks=text.split(' ');lines=[];cur=''
        for t in toks:
            cand=(cur+' '+t) if cur else t
            if cur and pxcheck.linew(cand)>limit: lines.append(cur);cur=t
            else: cur=cand
        lines.append(cur)
        s=lines[0]
        for i,l in enumerate(lines[1:]): s+=('\\n' if i==0 else '\\l')+l
        out.append(s)
    return '\\p'.join(out)
