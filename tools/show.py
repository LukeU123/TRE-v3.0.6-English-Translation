import json,sys
a=json.load(open('work/strings.json'))
lo,hi=int(sys.argv[1],16),int(sys.argv[2],16)
done=set()
import glob
for f in glob.glob('work/tr/*'):
    if f.endswith('.json'): done|=set(int(k,16) for k in json.load(open(f)))
    else: done|=set(int(l.split('|')[0],16) for l in open(f,encoding='utf-8') if '|' in l)
for x in a:
    if lo<=x['off']<hi and x['es']>=x['en'] and x['off'] not in done:
        print('%x|%d|%s'%(x['off'],x['end']-x['off'],x['text']))
