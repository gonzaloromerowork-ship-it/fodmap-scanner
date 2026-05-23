#!/usr/bin/env python3
import os, struct, zlib, base64

os.makedirs('icons', exist_ok=True)

def make_png(size):
    # Simple solid green circle icon for FODMAP app
    img = []
    cx = cy = size / 2
    r = size * 0.42
    r2 = size * 0.28
    for y in range(size):
        row = []
        for x in range(size):
            dx, dy = x - cx, y - cy
            dist = (dx*dx + dy*dy) ** 0.5
            if dist <= r:
                # Dark green bg
                if dist > r - 2:
                    row.extend([15, 26, 18, 255])  # border
                elif dist <= r2:
                    # Inner lighter circle
                    row.extend([109, 222, 138, 255])  # accent green
                else:
                    row.extend([25, 42, 28, 255])  # bg2
            else:
                row.extend([15, 26, 18, 0])  # transparent
        img.append(bytes(row))

    def make_chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = make_chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))

    raw = b''
    for row in img:
        raw += b'\x00' + row
    idat = make_chunk(b'IDAT', zlib.compress(raw, 9))
    iend = make_chunk(b'IEND', b'')

    return sig + ihdr + idat + iend

for size in [192, 512]:
    with open(f'icons/icon-{size}.png', 'wb') as f:
        f.write(make_png(size))
    print(f'Generated icon-{size}.png')

print('Icons created successfully!')
