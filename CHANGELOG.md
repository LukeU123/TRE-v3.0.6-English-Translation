# Changelog

All builds apply to the Spanish *Team Rocket Edition v3.0.6* ROM (MD5 `911e690484204ac1621211560aba356d`).

## 23 Nov 2026: graphics pass and polish
**Graphics**
- Translated text graphics taken from the engine's English assets: type icons, HP/Lv labels, status icons, summary screen headers, PC storage, naming screen buttons and header, Pokédex interface, bag HM label.

**Text**
- Line-width pass: 27 lines re-wrapped so they fit the text box at real pixel widths.
- Sweep for leftovers: Rocket Timeline menu, button-prompt lines (e.g. naming screen "CHOOSE / OK / BACK"), half-translated headings, "galeón" → Ship.
- ARCHI7 → SEVII everywhere (it's the Sevii Islands, not a name).

## 22 Nov 2026: playtest fixes
- Battle stat-change messages, "It doesn't affect…", move-type labels.
- Yes/No box, continue screen, Options, Player name label.
- Trainer memo, recruit lines, speaker name boxes (ATLAS → ARCHER, etc.).
- About 550 short lines the first extraction missed, found by extra scans.
- Consistency pass: KURT, COOLTRAINER, LEAGUE HQ, SUPER NERD MIGUEL, the DEVON admins, JANINE, CANDICE, ALTERING CAVE, US spelling.

## 21–22 Nov 2026: full script
- All 39 text chunks translated: story and map dialogue, battle text, items, moves, abilities, natures, place names and Pokédex entries.
- Strings that get longer in English are moved to free space and their pointers updated.
- Strings whose pointer started mid-sentence were re-keyed to their real start.

## Pilot
- First patch: intro narration, ARCHER's welcome, name registration, title and start menus.
