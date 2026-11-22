# Your job: translate one chunk of a Pokémon ROM hack from Spanish into English

You're one of several translators working in parallel on "Pokémon Team Rocket Edition", a Spanish fan hack of Pokémon Emerald. The extracting and reinserting are already done. **Your only job is to translate the text in your chunk file into natural, idiomatic English.**

1. Read `/home/claude/work/GLOSSARY.md` first and follow it exactly (official English names, control codes, length rules).
2. Your input is `/home/claude/work/chunks/cNN.txt`. Each line is `offset|byte_budget|MOV-or-FIXED|Spanish text`.
   - MOV = the string can grow (any length is fine, but keep each text line ≤ ~36 chars).
   - FIXED = the encoded English must fit within byte_budget (see GLOSSARY). Abbreviate if needed.
3. Work through the file in pieces of about 120 lines, using the Read tool with offset/limit. Don't try to read it all at once.
4. For each piece, append your translations to your output file `/home/claude/work/tr/2NN_cNN.txt` with Bash, using a quoted heredoc so the backslashes survive:
   ```
   cat >> /home/claude/work/tr/2NN_cNN.txt <<'EOF'
   20c762|English text with \n and \p codes kept
   EOF
   ```
   One line per string: `offset|English`. Leave out lines you skip (already English, identical names, junk, debug labels).
5. After each piece, run `python3 /home/claude/tools/check.py /home/claude/work/tr/2NN_cNN.txt` and fix every problem it reports. Edit the output file in place, e.g. with a small Python script, so you don't duplicate entries. Each offset may appear only once.
6. Carry on until the whole chunk is done. When the checker reports 0 problems on the complete file, stop.

Quality bar: it should read as if an English localisation team wrote it. Keep each character's voice and keep jokes working as jokes. Strings next to each other are often parts of the same conversation, so read the surrounding lines for context. Strings can also be sentence fragments that the game joins together; translate those so the pieces still join up.

If a line begins mid-word (the pointer lands partway into a sentence, e.g. "usta del mundo…"), SKIP it rather than guessing.

RESUMING: if your output file already exists, keep it, append to it, and skip every offset already in it (they're done). Check which offsets are present before you start.

Don't modify any other files. Don't run build.py. Don't touch the ROM.

Final reply (short): how many strings you translated and skipped, the checker result, and any names or terms you weren't sure about (Spanish → your choice), so the lead can keep the chunks consistent.
