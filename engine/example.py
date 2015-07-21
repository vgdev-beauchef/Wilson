"""Writes a 256x256 grayscale simplex noise texture file in pgm format
(see http://netpbm.sourceforge.net/doc/pgm.html)
"""
# $Id: 2dtexture.py 21 2008-05-21 07:52:29Z casey.duncan $

import sys
from noise import pnoise2, snoise2

if len(sys.argv) not in (2, 3) or '--help' in sys.argv or '-h' in sys.argv:
    print('2dtexture.py FILE [OCTAVES]')
    print()
    print(__doc__)
    raise SystemExit

f = open(sys.argv[1]+".pgm", 'wt')
if len(sys.argv) > 2:
    octaves = int(sys.argv[2])
else:
    octaves = 1
freq = 16.0 * octaves
width = 10
height = 10
scale = 10
f.write('P2\n')
f.write('%d %d\n' % (width, height))
f.write('255\n')
for y in range(height):
    for x in range(width):
        u = float(x) / (width - 1)
        v = float(y) / (height - 1)
        #f.write("%s\n" %
        #        int(pnoise2(u*scale, v*scale, 1, 0.5, 2.0, 1024, 1024, 0)*127 + 127))
        if x > 0:
        	f.write(" ")
        f.write("%s" %
                int((u + v)*0.5*255))
    f.write("\n")
f.close()
