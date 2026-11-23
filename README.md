# Pokémon Team Rocket Edition v3.0.6: English Translation (work in progress)

A fan translation of the Spanish romhack **Pokémon Team Rocket Edition v3.0.6** (Kanto, Sevii Islands, Johto, Johto DLC and Hoenn) into English. The latest official English release is v1.5, which only covers Kanto, the Sevii Islands and Johto.

**Status:** about 20,000 strings translated, covering the menus, the opening, battle text, items and moves, and most of the Kanto and Johto story. See `chunk_status.txt` for progress.
**Known issue:** the current patch stutters when fast-forwarding. See `REVIEW_NOTES.md`.

## Progress

### Done
- [x] Text tools: extracting, reinserting (moving lines that get longer in English and updating their pointers), validating, and building the patch
- [x] Title menu (New Game, Rocket Timeline), start menu, options, bag, shop, PC, summary-screen labels and Battle Frontier labels
- [x] The opening: intro narration, ARCHER's welcome, registering your name and GIOVANNI's introduction
- [x] Battle messages
- [x] Most item names and descriptions, berries, key items and Mega Stones
- [x] Most move names and descriptions, and about 340 Pokédex entries
- [x] Story and map dialogue, chunks c00–c18: the Kanto arc, Silph Co., the Elite Four, the Sevii Islands, the Johto conferences, the Radio Tower and Ecruteak

### In progress
- [x] Chunks c19–c21 and c25
- [x] Speaker name boxes, ability names, the title menu and the recruit lines
- [ ] Chunks c22–c24 and c26–c29 (partly translated, see `chunk_status.txt`)
- [ ] Chunks c33–c35 (items, moves and Pokédex text: the remaining lines)

### To do
- [ ] Chunks c30–c32: the rest of the story
- [ ] Chunks c36–c38: remaining Pokédex text, ability descriptions, nature names, location names, the clock and other system text
- [ ] Any other strings the extractor missed (found during playtesting)
- [ ] 27 strings to retranslate as full sentences (their pointers start mid-sentence)
- [ ] Check the fast-forward stutter (it didn't happen on a later run). The patched ROM stutters globally and the original doesn't. The suspected cause is false-positive pointer updates when lines are moved; see `REVIEW_NOTES.md`
- [ ] Consistency pass over names and terms that differ between chunks (`REVIEW_NOTES.md`), using US spelling throughout
- [ ] Full playtest
- [ ] Out of scope for now: text drawn as graphics (naming-screen buttons, type icons)

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
