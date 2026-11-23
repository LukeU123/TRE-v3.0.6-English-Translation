import numpy as np
from PIL import Image
def glyph(a,c,gw=16,gh=16):
    per=a.shape[1]//gw;r,cc=divmod(c,per);return a[r*gh:r*gh+gh,cc*gw:cc*gw+gw]
def enc(g):
    out=bytearray()
    for t in (g[0:8,0:8],g[0:8,8:16],g[8:16,0:8],g[8:16,8:16]):
        for row in t:
            v=0
            for x in range(8): v|=(int(row[x])&3)<<(2*(7-x))
            out+=v.to_bytes(2,'little')
    return bytes(out)
def dec(b):
    g=np.zeros((16,16),dtype=np.uint8);tiles=[(0,0),(0,8),(8,0),(8,8)]
    for ti,(y0,x0) in enumerate(tiles):
        for r in range(8):
            v=int.from_bytes(b[ti*16+r*2:ti*16+r*2+2],'little')
            for x in range(8): g[y0+r,x0+x]=(v>>(2*(7-x)))&3
    return g
