import json,re,bisect
es=[x for x in json.load(open('work/strings.json')) if x['es']>=x['en']]
EN=re.compile(r'\b(the|you|to|and|is|of|your|this|that|have|it|for|what|are|can|with|a|in|on)\b',re.I)
ESR=re.compile(r'\b(que|el|los|las|la|una|del|de|por|para|está|pero|con|y|en|se|lo|es|más)\b|[ñáéíóú¿¡]',re.I)
old=[x for x in json.load(open('work/old_strings.json')) if len(EN.findall(x['text']))>len(ESR.findall(x['text']))]
def feat(s):
    codes=tuple(sorted(re.findall(r'\{[^}]*\}',s)))
    caps=set(w for w in re.findall(r'\b[A-ZÉ]{3,}\b',s))
    nums=tuple(re.findall(r'\d+',s))
    return codes,s.count('\\p'),caps,nums,len(s)
EF=[feat(x['text']) for x in es];OF=[feat(x['text']) for x in old]
idx={}
for j,f in enumerate(OF): idx.setdefault((f[0],f[1]),[]).append(j)
pairs=[]
for i,f in enumerate(EF):
    for j in idx.get((f[0],f[1]),[]):
        g=OF[j];r=g[4]/max(f[4],1)
        if not 0.6<r<1.6: continue
        if f[3]!=g[3]: continue
        cj=len(f[2]&g[2])/max(len(f[2]|g[2]),1) if (f[2] or g[2]) else 0.5
        sc=cj+ (1-abs(1-r)) + 0.3*len(f[0]) + 0.3*f[1]
        if sc>1.0: pairs.append((i,j,sc))
print('candidate pairs',len(pairs))
# weighted LIS: increasing in i and j
pairs.sort(key=lambda p:(p[0],-p[1]))
# DP with BIT over j for max score
M=len(old)+1;tree=[(0,-1)]*(M+1);best=[None]*len(pairs)
def q(j):
    r=(0,-1)
    while j>0:
        if tree[j][0]>r[0]:r=tree[j]
        j-=j&-j
    return r
def u(j,v):
    while j<=M:
        if v[0]>tree[j][0]:tree[j]=v
        j+=j&-j
for k,(i,j,sc) in enumerate(pairs):
    pv=q(j)  # j indices < j (1-based j+1 -> query j)
    best[k]=(pv[0]+sc,pv[1]);u(j+1,(best[k][0],k))
k=max(range(len(pairs)),key=lambda k:best[k][0]);m={}
while k>=0:
    i,j,sc=pairs[k];m[i]=(j,sc);k=best[k][1]
print('matched',len(m),'of',len(es))
ref={'%x'%es[i]['off']:old[j]['text'] for i,(j,sc) in m.items()}
json.dump(ref,open('work/ref.json','w'),ensure_ascii=False)
import random;random.seed(5)
for i in random.sample(sorted(m),12):
    print('ES:',es[i]['text'][:90]);print('EN:',old[m[i][0]]['text'][:90]);print()
