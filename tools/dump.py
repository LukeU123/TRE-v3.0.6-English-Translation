import sys,pickle,re,json;sys.path.insert(0,'tools');from g3text import *
d=open('rom/PkmnTeamRocket.gba','rb').read()
ptrs=pickle.load(open('work/ptrs.pkl','rb'))
ES=re.compile(r'\b(que|el|los|las|una|del|por|para|está|eres|tienes|aquí|pero|puedes|quieres|Equipo|también|muy|con|esto|hay|mi|tu|sí|no)\b|[ñáéíóú¿¡]')
EN=re.compile(r'\b(the|you|to|and|is|of|your|this|that|have|it|for|what|are|can|with)\b')
out=[]
for t in sorted(ptrs):
    if t>=len(d):continue
    s,e=decode(d,t)
    if not s or len(s)<4:continue
    letters=sum(c.isalpha() for c in s)
    if letters<3 or letters/len(s)<0.4:continue
    es=len(ES.findall(s));en=len(EN.findall(s))
    out.append(dict(off=t,end=e,refs=ptrs[t],text=s,es=es,en=en))
json.dump(out,open('work/all.json','w'),ensure_ascii=False)
print(len(out),sum(1 for x in out if x['es']>x['en']),sum(1 for x in out if x['en']>x['es']))
