# Pokémon Team Rocket Edition v3.0.6: English Translation (work in progress)

> **Note on the official translation (23 Nov 2026):** the Team Rocket Edition developers have said their own official English translation, for **v3.1.0**, is close to completion and expected in the next 1–2 months.
> This project is an **unofficial** fan translation of **v3.0.6**. It isn't affiliated with or endorsed by the developers. Work continues in the meantime, but once the official v3.1.0 English release is out, please use and support that version. This project will then be kept only as an archive of the v3.0.6 translation.

A fan translation of the Spanish romhack **Pokémon Team Rocket Edition v3.0.6** (Kanto, Sevii Islands, Johto, Johto DLC and Hoenn) into English. The latest official English release is v1.5, which only covers Kanto, the Sevii Islands and Johto.

**Status:** about 25,700 strings translated, covering the menus, the opening, battle text, items and moves, and most of the Kanto and Johto story. See `chunk_status.txt` for progress.
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
- [x] Chunks c19–c22, c24 and c25
- [x] Speaker name boxes, ability names, the title menu and the recruit lines
- [x] Chunks c23 and c26–c31
- [x] Chunk c36 (Pokédex entries)
- [x] Consistency pass, round 1 (KURT, COOLTRAINER, LEAGUE HQ, the DEVON admins, JANINE, US spelling)
- [x] Redo of the mid-sentence strings (23 of 27; the rest are fragments or species names)
- [ ] Chunks c33–c35 (items, moves and Pokédex text: the remaining lines)

### To do
- [ ] Chunk c32: the last story chunk
- [x] Chunk c38: natures, ability descriptions, place names, bag/shop UI, trainer quotes
- [x] Chunk c37: Pokédex entries
- [ ] Any other strings the extractor missed (found during playtesting)
- [ ] Check the fast-forward stutter (it didn't happen on a later run). The patched ROM stutters globally and the original doesn't. The suspected cause is false-positive pointer updates when lines are moved; see `REVIEW_NOTES.md`
- [ ] Final consistency pass (`REVIEW_NOTES.md`)
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
