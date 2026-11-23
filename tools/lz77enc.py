def compress(data,vram=True):
    """GBA LZ77 (type 0x10). vram=True forbids displacement 1 (16-bit VRAM writes)."""
    n=len(data);out=bytearray([0x10,n&255,(n>>8)&255,(n>>16)&255]);i=0
    mind=2 if vram else 1
    while i<n:
        flagpos=len(out);out.append(0);flags=0
        for b in range(8):
            if i>=n: break
            best=0;bd=0
            start=max(0,i-4096)
            for j in range(i-mind,start-1,-1):
                l=0
                while l<18 and i+l<n and data[j+l]==data[i+l]: l+=1
                if l>best: best=l;bd=i-j
                if best==18: break
            if best>=3:
                flags|=0x80>>b;dv=bd-1
                out.append(((best-3)<<4)|(dv>>8));out.append(dv&255);i+=best
            else: out.append(data[i]);i+=1
        out[flagpos]=flags
    while len(out)%4: out.append(0)
    return bytes(out)
