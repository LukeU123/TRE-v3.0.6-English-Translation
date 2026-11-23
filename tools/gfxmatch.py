import sys,struct,pickle,collections,numpy as np,os
sys.path.insert(0,'/home/claude/tools');import smol;from gfx import *
from PIL import Image
CACHE='/home/claude/gfx/blobs.pkl'
def blobs():
    if os.path.exists(CACHE): return pickle.load(open(CACHE,'rb'))
    d=rom();P=pickle.load(open('/home/claude/work/ptrs.pkl','rb'));out={}
    for t in P:
        if t%4 or t+8>len(d): continue
        w=struct.unpack_from('<I',d,t)[0];mode=w&15;size=((w>>4)&0x3fff)*4
        if 1<=mode<=6 and 0x40<=size<=0x10000:
            try: data,h=smol.decode(d,t)
            except Exception: continue
            if len(data)==size: out[t]=data
        elif d[t]==0x10:
            r=lz77(d,t)
            if r and 0x40<=len(r[0])<=0x10000: out[t]=r[0]
    pickle.dump(out,open(CACHE,'wb'));return out
def png4(f):
    a=np.array(Image.open(f))&15;h,w=a.shape;b=bytearray()
    for ty in range(h//8):
        for tx in range(w//8):
            for row in a[ty*8:ty*8+8,tx*8:tx*8+8]:
                for x in range(0,8,2): b.append(int(row[x])|(int(row[x+1])<<4))
    return bytes(b),w//8
def best(f,top=3):
    en,tw=png4(f);T=[en[i*32:i*32+32] for i in range(len(en)//32)];C=collections.Counter(T)
    tiles=set(t for t in T if C[t]==1 and len(set(t))>=4)
    res=[]
    for t,data in blobs().items():
        s=sum(data[i*32:i*32+32] in tiles for i in range(len(data)//32))
        if s: res.append((s,len(tiles),hex(t),len(data)//32,len(T)))
    res.sort(reverse=True);return res[:top]
