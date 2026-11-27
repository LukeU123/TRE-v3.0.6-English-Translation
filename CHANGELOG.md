# Changelog

All builds apply to the Spanish *Team Rocket Edition v3.0.6* ROM (MD5 `911e690484204ac1621211560aba356d`).

## 27 Nov 2026
- PC storage messages: "{Pokémon} selected/was deposited/was released" were still Spanish, as were a battle line ("acquired"), the Pokédex "has no alternate forms" line and a list "and". The extractor skipped lines that start with a placeholder.
- 10 move descriptions still in Spanish (Iron Head, Pay Day, Bind, Twineedle, Hydro Pump, Uproar, Overheat, Rock Climb, Infestation, Floaty Fall).
- 16 item descriptions still in Spanish (14 Pokéblock berries, the old Enigma Berry, Reins of Unity).
- 7 move names were still Spanish (Hiperrayo → Hyper Beam, A Bocajarro → Close Combat, Gigaimpacto → Giga Impact, Humareda → Lava Plume, Romperrocas → Rock Wrecker, A Defender → Defend Order, Ascensodraco → Dragon Ascent).
- TM100–TM246 were labelled "MT"; "Baya Enigma" → Enigma Berry; the "SILPH S.A." map name → SILPH CO.; "Tirar" in the item PC menu → Toss.

## 26 Nov 2026
- Type names in the move-learning screen ("Agua" → Water, plus Fairy and Stellar), now part of the fixed name tables.

## 25 Nov 2026: more missed descriptions
- 23 move descriptions (Sludge, Scald, Leaf Storm, Draco Meteor, Fire Spin…), the POKéBLOCK CASE description and 3 Pokédex entries were still Spanish. A stray character before each one had stopped the extractor finding it.

## 24 Nov 2026: playtest fixes (evening)
- Two-turn move descriptions (Dig, Dive, Solar Beam, Bounce, Skull Bash…) were still Spanish: the superscript in "1.er" stopped them being picked up. A few TM/item descriptions rewrapped to fit the bag box.
- Rocket Timeline info screen translated.
- Pokédex: fixed the garbled START menu (both versions), "P." → "WT", "Searching… Please wait.", translated the stat labels (PS/AT/DF/AE/DE/VL → HP/AT/DE/SA/SD/SP), the NATIONAL heading and "Modo A-Z" → "A-Z Mode".
- Trainer card header "FICHA ROCKET" → "ROCKET CARD". This graphic is unique to the hack, so it was redrawn by hand in the original lettering.
- Party screen HP bars showed "PS" (Spanish for HP). Now "HP", along with a second HP bar graphic.
- Bag/TM info panel: TYPE / POWER / ACCURACY / PP / EFFECT labels and its set of type icons were still Spanish.
- Pokémon markings menu: VALE / SALIR → OK / CANCEL.
- 129 more lines that were still Spanish, such as short exclamations ("¡Luke!"), Hoenn route signposts and POKéBLOCK dialogue. The extractor had skipped lines that start straight after a script command.
- 96 more menu lines that were still in Spanish: prize shops (COINS and prices), the egg shop, the three difficulty descriptions, Battle Frontier "Streak" and "LV. 50".
- Swept the whole ROM for uncompressed engine graphics that still differ from English; these were the only ones left.

## 24 Nov 2026: QA pass
**Fixes found by automated checks**
- Trainer classes: about 130 were still in Spanish (they're stored in a table the text extractor couldn't see). All now use the official English names (HIKER, FISHERMAN, BUG CATCHER…).
- Pokédex categories ("Seed POKéMON", "Mouse POKéMON"…) were all still Spanish. Now official English for every species, including forms.
- Spanish species names fixed: the 20 Paradox Pokémon (Great Tusk, Iron Valiant…), Type: Null, Unown King, Golden Unown and Armor Mewtwo.
- Fixed a build bug that broke one script (an NPC/sign near Mr. Briney's text) and slightly recoloured 5 palettes. The build now refuses both kinds of false pointer match.
- 16 more lines that were still in Spanish, including the Lilycove POKéBLOCK lecture.
- 14 Battle Frontier quotes trimmed to fit, and a few name fixes (SAPPHIRE, AMETHYST, JULIA).

**Verified**
- The stutter reported earlier wasn't caused by the patch. It only happens with mGBA on a second monitor running at a different refresh rate.
- Every byte the patch changes is accounted for (text, graphics, name tables or a checked pointer).
- All translated graphics read back correctly from the patched ROM.

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
