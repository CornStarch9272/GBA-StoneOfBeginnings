# Summon Night - Craft Sword Monogatari ~Hajimari no Ishi~ Font Editor

## Run

```
python font_editor.py
```

## Usage:

- Global hotkey `Ctrl-E` or `Ctrl-Enter` or `Ctrl-Return` for edit selected glyph
- Global hotkey `Ctrl-W` for write font data to file
- Global hotkey `Ctrl-R` for generate random preview text
- Other hotkeys only work when specific widget is in focus

### Glyph browser:

- Can be search by character or index
- ASCII mode only show ASCII character (box checked)
- View All mode show all character in font but ***do not allow edit width*** (box uncheck)

### Glyph Editor:

- Press `Preview` button show glyph with 4×, 2×, and 1× original size
- Preview image in top left corner is 3× original size
- Blue vertical line show left boundary and right boundary
- Brown line divide cell
- Glyph max size is 16×12
- `Ctrl-Z` to undo, `Ctrl-Y` to redo, `Ctrl-N` to clear glyph (create new blank glyph)
- `Ctrl-S` to save glyph (memory only, no change is written to file), `Ctrl-P` for preview
- Drag mouse or click at cell to change
- Guides: add visual aid by enter comma separated values in `Guides`
- Horizontal guides: add `h` before row number, example: `h1, h4`, max = 12
- Vertical guides: add `v` before column number, example: `v5, v6`, max = 16
- Guide color: add 32bit hexadecimal RGBA color value, example: for red color add `0xff0000ff`
- `Ctrl-Up` change glyph to next glyph in font (view all mode) or next ascii glyph (ascii mode)
- `Ctrl-Down` change glyph to previous glyph in font (view all mode) or previous ascii glyph (ascii mode)
- `Ctrl-Left` decrease width
- `Ctrl-Right` increase width
- `Up` shift glyph up 1 row
- `Down` shift glyph down 1 row
- `Left` shift glyph left 1 column
- `Right` shift glyph right 1 column

### Preview:

- Enter text into line to view sample text with original color in ROM (need press enter)
- Text display at 2× original size
- Use zoom to change text size

## Changelog

- Version 1.7: `Ctrl-R` generate random text
- Version 1.6: change how hotkey `Up`, `Down`, `Left`, `Right` work, add hotkey `Ctrl-Up`, `Ctrl-Down`, `Ctrl-Left`, `Ctrl-Right`
- Version 1.5: add hotkey `Ctrl-S`, `Ctrl-P`, `Ctrl-W`
- Version 1.4: add hotkey `Up`, `Down`, `Left`, `Right` for Glyph Editor
- Version 1.3: allow undo `Ctrl-N`, bug fix, increase undo redo step to 32
- Version 1.2: add `Ctrl-N` hotkey, add zoom for text preview
- Version 1.1: add guidelines for editor
- Version 1.0: first release
