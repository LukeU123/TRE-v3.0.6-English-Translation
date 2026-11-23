# How it works

Technical notes on how the patch is made. You don't need any of this to play.

## The ROM

*Team Rocket Edition v3.0.6* is a 32 MB GBA ROM built on [pokeemerald-expansion](https://github.com/rh-hideout/pokeemerald-expansion). The text uses the Gen 3 character encoding, and most of the graphics are compressed.

## Text

### Encoding
`tools/g3text.py` converts between ROM bytes and readable text. Control codes are written in braces:

| Bytes | Written as | Meaning |
|---|---|---|
| `FD xx` | `{Vxx}` | Variable (player name, Pokémon, item…) |
| `FC xx …` | `{C…}` | Colour, pause, sound, etc. (argument count depends on `xx`) |
| `F7` / `F8` / `F9` | `{Dxx}` / `{Kxx}` / `{Fxx}` | Dynamic text, button icons, extra symbols |
| `FE` / `FA` / `FB` | `\n` / `\l` / `\p` | New line / scroll line / new box |
| `FF` | (end) | End of string |

### Finding strings
1. Every 4-byte value in the ROM that looks like a pointer into ROM space is indexed.
2. Pointer targets that decode as valid text become candidate strings.
3. Extra scans pick up strings with no pointer (table entries, short labels, button-prompt lines).

This gives a local string index (offset, end, Spanish text, pointer locations). **It isn't committed**, because it contains the original team's script.

### Translation files
`translations/` holds one line per string:

```
2fc971|RECRUIT No. 2!!
```

Files are applied in name order, so later files (the `3xx_*` fix files) override earlier ones.

### Inserting
`tools/build.py` encodes each English string, then:
- **If it fits** in the Spanish string's space, writes it there and pads with `FF`.
- **If it's longer,** writes it to free space at the end of the ROM (from `0x1CDADC0`) and updates every *verified* pointer to it. Pointer locations are filtered to avoid rewriting values that only look like pointers.
- **If it's longer and has no pointer,** it can't be moved, so the build warns and the line is shortened by hand.

### Checks
- `tools/check.py`: control codes match the Spanish, leading spaces match, unpointed strings fit their space, and no line is longer than the Spanish allows.
- `tools/pxcheck.py`: measures each line in pixels using the game's own font width table, against the 216 px text box.
- `tools/rewrap.py`: re-wraps lines that are too wide by turning spaces into line breaks, so the byte length stays the same.

## Graphics

pokeemerald-expansion compresses most graphics with its own tANS-based "smol" format. `tools/smol.py` is a Python port of the engine's decompressor, used to find and decode the Spanish graphics.

The hack uses the engine's own layouts and palettes, so the engine's English versions drop straight in. The English art is compressed with standard GBA LZ77 (`tools/lz77enc.py`), which the engine's decompressor also accepts, and:
- if it fits, it's written in place;
- otherwise it goes in free space after the text, and the pointers to it are updated (each one is checked against the original value first).

`graphics/data/patches.json` lists each graphic: address, data file, and the pointers to update.

## Building

You need the original Spanish ROM at `rom/PkmnTeamRocket.gba` and the local string index. Then:

```sh
python3 tools/build.py
```

This writes `out/PkmnTeamRocket_EN.gba` and `out/PkmnTeamRocket_EN.bps`. Only the `.bps` is ever shared.
