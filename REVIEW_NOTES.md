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
- The "Nv" level glyph (the font tile for [Lv]; it should read "Lv")
- Naming screen: ELEGIR / OK / VOLVER header, plus the minús., SELEC., ATRÁS and BOTÓN B buttons
- PC storage screen: the EQUIPO PkMn (PARTY PKMN) and CERRAR CAJA (CLOSE BOX) buttons, and the INFO PkMn header
Fix approach (a separate task): find the LZ77-compressed tile sheets, decompress them, redraw the English labels in the same pixel font, recompress, then repoint or write them back. Mostly in the summary-screen, menu and font graphics.
