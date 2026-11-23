import numpy as np
from PIL import Image
ROM=None
def rom():
    global ROM
    if ROM is None: ROM=open('/home/claude/rom/PkmnTeamRocket.gba','rb').read()
    return ROM
def tile4(b):
    a=np.frombuffer(b,dtype=np.uint8)
    px=np.empty(64,dtype=np.uint8);px[0::2]=a&15;px[1::2]=a>>4
    return px.reshape(8,8)
def sheet(data,tw=16,th=None,pal=None,sprite=None):
    """data: bytes of 4bpp tiles. tw: tiles per row. sprite=(w,h) in tiles to group 1D-mapped sprites."""
    n=len(data)//32
    tiles=[tile4(data[i*32:i*32+32]) for i in range(n)]
    if sprite:
        sw,sh=sprite;per=sw*sh;ns=n//per;cols=max(1,tw//sw);rows=(ns+cols-1)//cols
        img=np.zeros((rows*sh*8,cols*sw*8),dtype=np.uint8)
        for s in range(ns):
            r,c=divmod(s,cols)
            for k in range(per):
                ty,tx=divmod(k,sw)
                img[(r*sh+ty)*8:(r*sh+ty)*8+8,(c*sw+tx)*8:(c*sw+tx)*8+8]=tiles[s*per+k]
    else:
        rows=(n+tw-1)//tw;img=np.zeros((rows*8,tw*8),dtype=np.uint8)
        for i,t in enumerate(tiles):
            r,c=divmod(i,tw);img[r*8:r*8+8,c*8:c*8+8]=t
    if pal is None: pal=[(i*17,i*17,i*17) for i in range(16)]
    rgb=np.array(pal,dtype=np.uint8)[img]
    return Image.fromarray(rgb)
def gbapal(b):
    out=[]
    for i in range(0,32,2):
        v=b[i]|(b[i+1]<<8);out.append(((v&31)*8,((v>>5)&31)*8,((v>>10)&31)*8))
    return out
def lz77(d,o):
    if d[o]!=0x10: return None
    size=d[o+1]|(d[o+2]<<8)|(d[o+3]<<16);out=bytearray();i=o+4
    try:
        while len(out)<size:
            flags=d[i];i+=1
            for bit in range(8):
                if len(out)>=size: break
                if flags&(0x80>>bit):
                    b1,b2=d[i],d[i+1];i+=2
                    ln=(b1>>4)+3;disp=((b1&15)<<8|b2)+1
                    if disp>len(out): return None
                    for _ in range(ln): out.append(out[-disp])
                else: out.append(d[i]);i+=1
    except IndexError: return None
    return bytes(out),i-o
