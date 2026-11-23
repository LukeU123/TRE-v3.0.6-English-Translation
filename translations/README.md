# Translations

One string per line: `ROM offset (hex)|English text`. Lines starting with `#` are comments.

| Files | Contents |
|---|---|
| `000`–`013` | Pilot and UI (menus, options, bag, PC, summary screen) |
| `200`–`238` | The main script, chunks c00–c38 (story, battles, items, moves, Pokédex, place names) |
| `300_manual_fixes` | Name boxes, Options, Yes/No, admin names and other hand fixes |
| `301_abilities` | Ability names and descriptions |
| `302_redo` | Strings re-keyed to their real start and redone |
| `303`–`305` | Trainer memo and lines found by later scans |
| `306_battle_templates` | Stat-change messages, type labels, placeholders |
| `307_timeline_and_heads` | Rocket Timeline menu, headings |
| `308_button_text` | Lines with button icons |
| `309_leftovers` | Final sweep |

Files are applied in name order, so a later file overrides an earlier one for the same offset.

Control codes like `{V01}`, `{C…}` and `\n` / `\l` / `\p` must stay the same as in the original. See [../docs/HOW_IT_WORKS.md](../docs/HOW_IT_WORKS.md) and the naming rules in [../docs/GLOSSARY.md](../docs/GLOSSARY.md).
