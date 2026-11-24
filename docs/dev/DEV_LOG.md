- Trainer pair names: c03 mapped TULA/ILDA -> ANNA/MEG and c04 mapped ANI/MATI -> ANNA/MEG (conflict, review in consistency pass)
- NUEVO ORDEN: c06 "NEW ORDER" vs c05 "new order" -> unify to NEW ORDER
- ENTRENADOR GUAY: c05 COOLTRAINER vs c06 COOL TRAINER -> unify to COOLTRAINER
- CÉSAR: c05 used CESAR, c08 used KURT (César is Kurt's official Spanish name) -> unify to KURT
- SCIENTIST MIGUEL (c13) -> SUPER NERD MIGUEL
- Spelling: c14 used British spelling (organisation, honour); official games use US spelling -> unify to US in consistency pass

## From Luke's playtest (22 Nov) — fix next session
MISSED BY EXTRACTOR (not in strings.json; add them and translate in place, they're unpointed so must fit):
- Title menu "Opciones" at 0x8ecf58 (next to "Nuevo juego" 0x8ecf48) -> "Options"
- "¡¡RECLUTA N.º 2!!" etc. at 0x2fc971 / 0x2fc986 / 0x2fc99b (Archer calling recruits) -> "RECRUIT No. 2!!"
- Ability names table around 0xe66bec ("Allanamiento" = Infiltrator) - check the whole ability-name table near there
- Speaker NAME BOX "ATLAS" (shows above text box) - find the name-box string table, -> ARCHER (and other name-box names)
- "NOTAS ENTR." (summary screen) not found as text - may be graphics or another encoding
NOT YET DONE (in chunk c38, untranslated): clock "¿Esta es la hora correcta?" (0xe85b8c), RENOM. (0xe859f4), nature names (0xe65768), map/location names like ALMACÉN ROCKET (0xe71178)
GRAPHICS, not text (would need tile editing, out of scope unless Luke asks): naming-screen header "ELEGIR / OK / VOLVER", buttons "minús.", "SELEC.", "ATRÁS", "BOTÓN B"; type icons VENENO / VOLAD.
Luke's verdict so far: "looking pretty good".

## Fast-forward stutter (Luke, 22 Nov): patched ROM stutters when fast-forwarding in mGBA; original ROM doesn't
Not yet investigated. Things to check, in order:
1. Same mGBA settings for both ROMs (fast-forward speed, rewind, sync to video/audio). Luke's screenshots show ~120 fps on the patched ROM.
2. Whether the free-space region used for repointed strings (0x1CDADC0 onward, inside an FF block starting 0x1CDADA0) is really unused. If the hack reads or streams data from there at runtime (or the FF block is padding the engine relies on), moving text there could cause it. Test: build a patch with ONLY in-place strings (skip every "moved" one) and see whether the stutter goes away.
3. Whether the stutter appears only during text boxes or all the time. Text speed and the "instant text" option interact with fast-forward.
4. A stale .sav from another build (try a fresh save on the patched ROM).
5. Compare against the pilot patch (also used repointing) to narrow down when it started.
UPDATE (Luke, 21:07): it was a fair test. Both ROMs fresh with no save and identical mGBA settings, and the patched one stutters on EVERYTHING: text, sprite movement, menus. So it is global, not text-only, which rules out checks 1, 3 and 4 above.
Leading suspect now: build.py updates every "reference" to a moved string, and some of those references are probably FALSE POSITIVES. These are 4-byte-aligned values that happen to equal the string's address but are really code or data. Overwriting them could corrupt a table or literal the game uses every frame.
To diagnose:
(a) Build with no moved strings (in place only) and confirm the stutter disappears.
(b) List every pointer write build.py makes (address, old value, new value). Flag any outside the script region 0x1E0000-0x500000 or the known text tables, and any whose address falls in the code area (below ~0x1E0000, e.g. 0x0006xxxx and 0x0011xxxx hits seen for UI strings).
(c) Bisect the moved strings to find the culprit or culprits.
Safer long-term fix: only repoint a reference when the referencing context is verified (a script opcode, or a known string-pointer table). Otherwise shorten the English so it fits in place.
UPDATE (Luke, 23 Nov): he started the patched ROM again later and there was NO stutter, so it may have been something else on his PC. Lower priority; keep an eye on it.
Quick check (23 Nov): the bytes changed outside text are pointer updates. Most are in the script region (0x200000+). There are a few dozen in the code and data area (0x06xxxx, 0x0Exxxx-0x1Axxxx); these are literal-pool pointers to UI strings, which is expected. Nothing obviously wrong.
- Name box: ESMERALDA kept (dialogue keeps it) while RUBÍ/ZAFIRO became RUBY/SAPPHIRE; MORFEO, INVERNA, VALENTE kept; consider unifying
- C.MIGUEL/CIENTÍFICO MIGUEL rendered as S.N.MIGUEL, C.MIGUEL, SCIENTIST MIGUEL and MIGUEL in different chunks -> unify (suggest SUPER NERD MIGUEL / MIGUEL)
- DEVON admins: c28 made AMATISTA -> AMETHYST and ESMERALDA -> EMERALD, but other chunks and the name boxes keep AMATISTA and ESMERALDA (RUBÍ/ZAFIRO -> RUBY/SAPPHIRE everywhere). Pick one: suggest RUBY/SAPPHIRE/EMERALD/AMETHYST everywhere, including the name boxes.
- SACHIKO: c08 and the name box use JANINE, c28 kept SACHIKO -> unify to JANINE
- CUEVA CAMBIANTE: c08 and c16 use ALTERING CAVE (official FRLG), c30 uses SHIFTING CAVE -> unify to ALTERING CAVE
- "Inventar diálogo" placeholder: c31 translated it as "Write dialogue", c30 skipped it (left Spanish) -> pick one (suggest "Write dialogue" everywhere)
- OLGA: c30 used JULIA (Sunyshore ribbon lady), c31 kept OLGA -> check
- INVERNA = CANDICE (c27). Name box 300_manual_fixes still maps INVERNA->INVERNA: change it to CANDICE after the consistency pass finishes
- Pokédex entries (c36): about 35 run to 4 lines where the Spanish has 3. Check in-game whether the Dex box shows 4 lines; if not, shorten them
- e85ae2 '  Baya' and e8a60e '   Baya' left in Spanish: only 4 letters fit (the leading spaces are padding, so they can't be removed). Options: 'Bery' (no), repoint, or accept Spanish
- Placeholder 'Inventar diálogo' is now 'Dialogue TBD' (c31, c32); c30 left the Spanish placeholder
- Stutter update (Luke, 23 Nov 18:39): it happened again, but saving and restarting the game made it go away. It's intermittent and clears on restart, so it's most likely an emulator or host issue (mGBA audio/video sync drift) rather than corrupted data in the patch. Still worth testing the original ROM for an equally long session to compare.

## GRAPHICS (text drawn as images; can't be fixed by editing text). Luke's screenshots, 23 Nov
- Summary-screen section headers: PERFIL, HABILIDAD, NOTAS ENTR., OBJETO, CINTAS, CARACT., EXPERIEN., MOVIMIENTOS, DESCRIPCIÓN
- Type icons: VENENO, VOLAD., SINIE., PLANTA, ... (all 18 types plus "?")
- The "Nv" level glyph (the font tile for [Lv], plus the battle healthbox "Nv" tile) and the "PS" label on the HP bar (should read "HP"). Top priority: they appear in every battle and on the summary screen
- Naming screen: ELEGIR / OK / VOLVER header, plus the minús., SELEC., ATRÁS and BOTÓN B buttons
- PC storage screen: the EQUIPO PkMn (PARTY PKMN) and CERRAR CAJA (CLOSE BOX) buttons, and the INFO PkMn header
Fix approach (a separate task): find the LZ77-compressed tile sheets, decompress them, redraw the English labels in the same pixel font, recompress, then repoint or write them back. Mostly in the summary-screen, menu and font graphics.
- Stutter (23 Nov 18:53): it's back after a ~5 minute session; other GBA ROMs don't do it. Test plan sent to Luke: (1) the ORIGINAL Spanish ROM for 5+ minutes; (2) TEST_inplace_only.bps (built with NOMOVE=1 OUT=out/TEST_inplace_only python3 tools/build.py; it skips the 6,002 moved strings, so no pointer edits) for 5+ minutes; (3) the full patch. Original stutters too = the hack itself. Only the full patch stutters = pointer updates or free-space use -> bisect the moved strings.

## NEXT FIX (Luke's screenshot, 23 Nov 19:08): stat-change format strings still Spanish
Battle shows "¡ATTACK de Zubat fell!". These short battle templates were missed (mostly codes). Translate them as "{mon}'s {stat}\n{change}!", reordering the codes:
- 4c5e30, 4c5e40, 4c5e50, 4c7610: '¡{V00} de {V10}\n{V01}!' -> '{V10}'s {V00}\n{V01}!' (14-byte FIXED unless refs: 's adds 2 bytes, so check budget/refs, or repoint)
- 4c2664 '¡{V00} de {V13} aumentó!' -> "{V13}'s {V00} rose!"
- 4c3d0c / 4c6f84 '...\nno subirá más!' -> "{V10}'s {V00}\nwon't go any higher!"
- 4c6f68 '...\nno bajará más!' -> "won't go any lower!"
- 4c4f88 '¡{V1A} de {V13}\nlo hizo ineficaz!' -> "{V13}'s {V1A}\nmade it ineffective!"
- 4c53d0 '...\nprevino que su {V00} baje!' -> "{V13}'s {V1A}\nprevents {V00} loss!"
- 4c7000 '¡{V00} de {V13} paralizó a {V40}, quizás no se mueva!' -> "{V13}'s {V00} paralyzed {V40}! It may be unable to move!"
Then scan the battle region 0x4b0000-0x4d0000 for any other '¡{Vxx} de {Vxx}' / ' de {V' patterns (regex rb'\x52\xfd.\x00\xd8\xd9\x00\xfd'), plus other short Spanish templates.
- ROCKET TIMELINE menu screen (Luke, 23 Nov 19:53): still Spanish: "Bienvenido/a a Efemérides Rocket." / "Comenzar" / "Info y FaQ" / "Volver atrás". Missed by both scans; search the raw bytes (e.g. encode('Comenzar')) and translate as "Welcome to Rocket Timeline." / "Start" / "Info & FAQ" / "Go back". Check the rest of that feature's text (FAQ pages) too.
- IDEA (Luke): produce a "Pokémon by route" sheet from the ROM's wild encounter tables (pokeemerald-expansion gWildMonHeaders: map group/num -> land/water/rock/fishing tables of species, levels and rates). Do this later, as a Sheets artifact.
  Reference format Luke likes: https://docs.google.com/spreadsheets/d/1PyGm-yrit5Ow6cns2tBA9VEMwLVMzn3YhDRipABjLUM/edit?gid=55717469 (open it first and match its layout)
- ARCHI7 (Luke, 23 Nov 20:18): it's the hack's shorthand for "Archipiélago" of the 7 (Sete) islands, i.e. the SEVII ISLANDS. The helpers kept "ARCHI7" as a made-up name. Replace with SEVII (or SEVII ISLANDS where it fits) everywhere: dialogue, badge screen ("Archi7:" -> "Sevii:"), region labels (e866e0 "ARCHI7"), Pokédex region text. Watch the FIXED budgets: "SEVII" is 5 letters vs 6, so it always fits.

## Done 23 Nov (late, PC off)
- Stat-change battle templates ("Zubat's ATTACK fell!"), "It doesn't affect…", the move-type labels ("a Rock move" etc.), "&" join, "{V16} snapped it out of its confusion!"
- Rocket Timeline menu ("Welcome to Rocket Timeline." / Start / Info & FAQ / Go back / Season / Confirm)
- 6 half-translated lines fixed (Spanish head + English tail): 2101cf, 2261ef, 241bb1, 3dafe4 + dex 9c0be2 + save prompt 2a6077
- ARCHI7 -> SEVII everywhere (about 60 lines plus labels); glossary updated
- "Inventar diálogo" placeholders in c30 -> "Dialogue TBD" (now consistent)
- New QA scan of the patched ROM for leftover Spanish: most hits are dead copies of moved strings (the original Spanish left behind, which the game never shows). The real leftovers were the items above.
- Codec: added F7 {Dxx} (summary memo placeholders), F8 {Kxx} (button icons) and F9 {Fxx}

## GRAPHICS PASS: started 23 Nov (PC off)
How the hack stores graphics: pokeemerald-expansion "smol" compression (tANS). tools/smol.py is a Python port of the engine's decompressor (src/decompress.c), and it works. To write graphics back, use LZ77 (header 0x10 = MODE_LZ77, which the engine's DecompressDataWithHeader also accepts): tools/lz77enc.py. Put the result in free space (0x1F00000+) and repoint the sprite-sheet record. build.py applies work/gfx/patches.json automatically.
Reference English art: sparse clone of rh-hideout/pokeemerald-expansion graphics/ (in /home/claude/pex; re-clone if needed). The hack uses the same palette indices as the engine's PNGs, so they drop straight in.
DONE: move type icons (sheet at 0x82a5e8, 26 icons, record at 0x97475c, tag 0x7532) -> 18 icons replaced with the engine's English art; ???, STELLR and the contest icons were already English.
NEXT: the summary screen tiles (gSummaryScreen_Gfx, smol; find via the same scan, contains the PERFIL/HABILIDAD/OBJETO... headers) + the page tilemaps; the healthbox "PS" (hpbar.4bpp, uncompressed gHealthboxElementsGfxTable); the "Nv" glyph in the latin fonts (uncompressed latfont, find by matching unchanged glyphs from pex/graphics/fonts); the PC storage buttons; the naming screen.

## GRAPHICS PASS: done 23 Nov (late)
All the graphics on the list are replaced with the engine's own English art (same palette indices, same layout). Applied by build.py from work/gfx/patches.json:
- type icons (smol sheet 0x82a5e8 -> LZ77 at 0x1F00000, record 0x97475c)
- battle HP label "PS" -> "HP" (uncompressed hpbar tiles 1-2 at 0x8b131c)
- "Nv" -> "Lv": glyphs 0x34 and 0x105 in latin_normal (0x7a78d4), latin_small (0x7bfed4), latin_short (0x7afad4)
- summary screen tileset (smol 0x7effe4 -> LZ77 at 0x1F01000, ref 0x1875f4): PROFILE/ABILITY/ITEM/RIBBON/STATS/EXP./MOVES/EFFECT/DESCRIPTION/TRAINER MEMO
- PC storage menu (smol 0x7f0764 -> LZ77 at 0x1F02000, ref 0x18159c): PKMN DATA / PARTY POKéMON / CANCEL / CLOSE BOX
- naming screen (uncompressed): BACK / B BUTTON button (0x7e5ab8), others/lower/UPPER labels, SELECT frame (0x7e5c98)
- 18 text lines with button-icon codes (F8): naming header "CHOOSE OK BACK", Rocket Timeline help, difficulty descriptions, etc. (308_button_text.txt)
None of this has been tested in-game yet. LZ77 repacking relies on the engine's DecompressDataWithHeader accepting MODE_LZ77; if a screen shows garbage, that graphic needs smol re-encoding instead.

## 23 Nov (late): items 3/4/5
- Pixel-width check (tools/pxcheck.py, real font widths from the ROM table at 0x7a7774; message box 216px; Pokédex 240px): 27 overflowing lines re-wrapped (tools/rewrap.py only swaps spaces for line breaks, so byte length is unchanged). 2 stat-sheet lists split by hand. Remaining flags are trainer battle quotes that are just as long in the Spanish, plus Pokédex entries under 240px. The Spanish Pokédex mostly uses 4 lines (948 entries), so 4-line English entries are fine.
- Graphics sweep (all engine interface PNGs vs ROM): newly fixed: status icons (party/summary sheet 0x82b25c) and the 4 healthbox status sets (0x8b159c, 0x8b1c3c, 0x8b1e7c, 0x8b20bc); Pokédex search (0x9655e8), list (0x967480) and info SEEN/OWN tiles (0x9670e0, keeping the hack's own "REGIONAL" label); bag "MO" -> "HM" (0x7f1324). Checked and fine: party menu bg, Pokédex menu3 (no text differences).
- Leftovers: "galeón" -> "Ship", 2a031d translated. LEFT AS SPANISH: the two "Baya" labels (e85ae2, e8a60e: only 4 letters fit and no pointer was found, so they can't be moved), and the " son" fragments (4c06eb/4c06f0: unknown context).

## QA pass (24 Nov, while Luke at work)
- POINTER AUDIT: every byte the build changes outside text/graphics is now accounted for as a pointer update. Found and fixed 6 bad writes:
  - 0x2104f7: an unaligned "pointer" that overlapped a real msgbox command (0F 00 + pointer). The build overwrote the loadword opcode, breaking that script (a sign/NPC near Mr. Briney text). build.py now skips any unaligned ref that overlaps a real script command pointer.
  - 5 aligned matches deep in the data area (0xb115a0, 0xb1189c, 0x161afec, 0xbb7654, 0xace174) were palette colours that happened to equal a dialogue string address; the build was recolouring 5 palettes. build.py now never rewrites refs >=0x500000 to map dialogue (0x1E0000-0x4B0000).
  - Neither explains the stutter (one only fires when that script runs, the others are colours).
- GRAPHICS: all 7 repacked graphics read back from the built ROM decode to the right size (same as the Spanish originals) and the right English tiles (docs/images/graphics_readback.png). No overlaps in the 0x1F00000 area.
- MISSED TABLES (inline names with no pointers, so the extractor never saw them):
  - Trainer class names at 0x4be810 (148 x 16-byte entries, 13-byte name): ~130 were still Spanish (MONTAÑERO, PESCADOR…). Now official English. Applied from work/tr_tables.json.
  - Pokédex categories in gSpeciesInfo (base 0x9758df, stride 0xA8, category at +0, name at +13): all Spanish. Mapped to official English from pokeemerald-expansion source by species name; hack fakemon categories translated by hand.
  - Spanish species names fixed: the 20 Paradox Pokémon (Colmilargo -> Great Tusk etc.), Código Cero -> Type: Null, Rey Unown, Unown Áureo, Mewtwo Arm.
- 9 more missed strings (POKéBLOCK glyph bytes 55-59 and short {C19xx} lines broke the extractor) + 7 untranslated real lines -> 311_missed3.txt. g3text now knows [PO][Ké][BL][OC][K] and [UP]/[DOWN]/[LEFT]/[RIGHT].
- 14 Battle Frontier/brain quotes trimmed to be no wider than the Spanish; Mr. Briney sign shortened to fit (it lost its only "pointer").
- Names: ZAFIRO -> SAPPHIRE, AMATISTA -> AMETHYST, OLGA -> JULIA (Sunyshore ribbon lady).
- Pokédex: no entry exceeds 4 lines, and 500+ Spanish entries already use 4, so the box handles it. Item closed.
- STUTTER RESOLVED (24 Nov): not the patch. It only happens when mGBA is on Luke's second monitor (refresh-rate mismatch). Patched ROM on his PC verified identical to the build (MD5 f0ab8b615925786d3e9e630a309dcbaa).
- 24 Nov evening: Luke saw "¡Luke!" (Spanish ¡). Found 129 more missed strings: short speaker lines like {C19xx}¡{V01}!, route signs with arrow glyphs, POKéBLOCK lines. The extractor skipped strings that start right after script bytes rather than after FF, and any with arrow/POKéBLOCK glyphs. All in 312_missed4.txt. Pokémon cries ("Zap…", "Khan…") and English test strings left as they are.
- Bag/TM info panel (menu_info, uncompressed at 0x7F13A4), markings menu (0x7f1004) and a 2nd HP bar (0x8b12fc) were uncompressed graphics the first sweep missed; a raw-tile sweep of the whole ROM found them. Patched in place.
- Pokédex (24 Nov): garbled start menu because the hack's Spanish tilemaps index the tileset in the Spanish layout, and I'd swapped the tileset to English. Fixed by also swapping the 4 list-screen tilemaps (list, underlay, start menu, start menu for search results) for the engine's English ones (LZ77, at 0x1F09000+). The hack's tilemaps are smolTM (mode 8), which the engine also accepts as LZ77. If the hack had customised those screens, that customisation is lost. Stat labels PS/AT/DF/AE/DE/VL are an uncompressed sheet at 0x963274 and 0x9641c8 -> English HP/AT/DE/SA/SD/SP. "Modo A-Z" -> "A-Z Mode".
- 24 Nov: Pokédex START menu tilemaps were the wrong way round (0x9654a0 = search-results version, 0x965558 = main); swapped. "P." -> "WT". A scan of the UI area found 96 missed menu strings with no clean start or with $ / digits: prize shop lists (FICHAS/MONEDAS -> COINS, prices in $x,xxx format), egg shop, the three difficulty descriptions, "Vic. seg." -> "Streak", "NV. 50" -> "LV. 50", "Buscando… Espere." -> 313_ui_missed.txt. Footprint box in the Pokédex is empty: not touched by the patch (likely the same on the Spanish ROM).
