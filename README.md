# Pokémon Team Rocket Edition v3.0.6: English Translation (work in progress)

A fan translation of the Spanish romhack **Pokémon Team Rocket Edition v3.0.6** (Kanto, Sevii Islands, Johto, Johto DLC and Hoenn) into English. The latest official English release is v1.5, which only covers Kanto, the Sevii Islands and Johto.

**Status:** roughly half of the text is translated (about 17,000 strings), covering the menus, the opening, battle text, items and moves, and most of the Kanto and Johto story. See `chunk_status.txt` for progress.
**Known issue:** the current patch stutters when fast-forwarding. See `REVIEW_NOTES.md`.

## How to play
1. Get your own copy of the Spanish **Team Rocket Edition v3.0.6** ROM. No ROMs are provided here.
   Expected MD5: `911e690484204ac1621211560aba356d`
2. Apply `patch/TRE_v3.0.6_EN_WIP.bps` with [Floating IPS](https://www.romhacking.net/utilities/1040/) or [ROM Patcher JS](https://www.marcrobledo.com/RomPatcher.js/).
3. Play in mGBA or any GBA emulator.

## Repository contents
- `translations/`: English text, one `ROM-offset|English` line per string.
- `tools/`: Python scripts. `build.py` applies the translations to a ROM and produces the patch. `check.py` validates the text (box widths, control codes, byte budgets). `g3text.py` is the Gen 3 text codec.
- `GLOSSARY.md`: the naming conventions (official English names, plus terms the hack invented).

## Credits
- **Pokémon Team Rocket Edition** was created by its original Spanish development team. All credit for the game, story and design goes to them. This project only translates their text.
- English translation by LukeU123, with Claude.
- Pokémon is © Nintendo, Game Freak and The Pokémon Company. This is a non-commercial fan project.
