# Copyright (C) 2026, KurobaM
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations
from io import BytesIO
import os
import sys

if __name__ == '__main__':
    print('Import font data...')
    if len(sys.argv) < 3:
        print('Invalid arguments')
    else:
        rom_path = sys.argv[1]
        export_path = sys.argv[2]
    if not os.path.isfile(rom_path):
       print('Invalid arguments')
       sys.exit(-1)
    print(f'Original file: {rom_path}')
    with open(rom_path, 'rb') as f:
        rom = f.read()
    
    if (rom[0xa0:0xaf] != b'CRAFTSWORD HB3C'):
        print('Invalid ROM')
        sys.exit(-1)

    folder = os.path.join(os.path.dirname(__file__), 'data')

    with open(os.path.join(folder, 'font.bit'), 'rb') as f:
        font_data = f.read()

    out = BytesIO(rom)
    out.seek(0x14d5c6c)
    out.write(font_data)
    with open(export_path, 'wb') as f:
        f.write(out.getvalue())
    print(f'Output file path: {export_path}')
