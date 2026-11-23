# Pokémon Team Rocket Edition v3.0.6: English Translation (work in progress)

> **Note on the official translation (23 Nov 2026):** the Team Rocket Edition developers have said their own official English translation, for **v3.1.0**, is close to completion and expected in the next 1–2 months.
> This project is an **unofficial** fan translation of **v3.0.6**. It isn't affiliated with or endorsed by the developers. Work continues in the meantime, but once the official v3.1.0 English release is out, please use and support that version. This project will then be kept only as an archive of the v3.0.6 translation.

A fan translation of the Spanish romhack **Pokémon Team Rocket Edition v3.0.6** (Kanto, Sevii Islands, Johto, Johto DLC and Hoenn) into English. The latest official English release is v1.5, which only covers Kanto, the Sevii Islands and Johto.

**Status:** every text chunk is translated (about 26,300 strings). Now in playtesting and polish. See the Progress section below.
**Known issue:** a fast-forward stutter was seen once but hasn't been reproduced since. See `REVIEW_NOTES.md`.

## Progress

**All text chunks are translated (about 26,300 strings).** What's left is testing and polish.

### Done
- [x] Text tools: extracting, reinserting (moving lines that get longer in English and updating their pointers), validating, and building the patch
- [x] Menus and UI: title menu (New Game, Rocket Timeline), start menu, options, bag, shop, PC, summary screen, Battle Frontier, clock setup
- [x] The opening: intro narration, ARCHER's welcome, registering your name and GIOVANNI's introduction
- [x] All story and map dialogue (chunks c00–c32): Kanto, the Sevii Islands, Johto, the Johto DLC, Hoenn and the Sinnoh areas
- [x] Battle messages and trainer battle quotes
- [x] Items, berries, key items and Mega Stones (names and descriptions)
- [x] Moves (names and descriptions) and abilities (names and descriptions)
- [x] Natures, place names and speaker name boxes (ATLAS → ARCHER and so on)
- [x] Pokédex entries
- [x] Strings repointed to their real start where the pointer landed mid-sentence
- [x] Consistency pass, round 1: KURT, COOLTRAINER, LEAGUE HQ, the DEVON admins, JANINE, US spelling
- [x] Playtest fixes: battle stat messages, Yes/No box, continue screen, trainer memo, Rocket Timeline menu, ~550 missed short lines, ARCHI7 → SEVII

### To do
- [ ] Full playtest
- [ ] Fix any strings the extractor missed or that turn up during playtesting
- [ ] Check the ~35 Pokédex entries that now run to 4 lines (the Spanish has 3) and make sure the Dex box shows them in full
- [ ] Translate two "Baya" (Berry) labels that only have room for 4 letters
- [ ] Final consistency pass (remaining items in `REVIEW_NOTES.md`)
- [ ] Keep an eye on the fast-forward stutter seen once (not reproduced since; see `REVIEW_NOTES.md`)

### Out of scope (for now)
- Text drawn as graphics: summary-screen headers (PERFIL, OBJETO, MOVIMIENTOS…), type icons, the "Nv" level glyph and the naming-screen buttons. Needs image editing; see REVIEW_NOTES.md

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
