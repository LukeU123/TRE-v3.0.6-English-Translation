import sys;sys.path.insert(0,'/home/claude/tools');from gfxmatch import *
from PIL import Image
def compare(png,blob,out,scale=3):
    B=blobs();es=B[blob];en,tw=png4(png)
    im=Image.open(png);p=im.getpalette();pal=[tuple(p[(i)*3:(i)*3+3]) for i in range(16)]
    A=sheet(es[:len(en)] if len(es)>=len(en) else es,tw=tw,pal=pal);Bm=sheet(en,tw=tw,pal=pal)
    W=A.width+Bm.width+8;H=max(A.height,Bm.height)
    o=Image.new('RGB',(W,H),(255,0,0));o.paste(A,(0,0));o.paste(Bm,(A.width+8,0))
    o.resize((W*scale,H*scale),Image.NEAREST).save(out)
    n=len(en)//32;diff=[i for i in range(n) if es[i*32:i*32+32]!=en[i*32:i*32+32]]
    return len(es)//32,n,len(diff)
