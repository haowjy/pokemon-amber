# Mechanical Prose Patterns (Chapters 1--17) --- Quantitative Catalog

<AI>

## Method (what got counted)

- Corpus: `story/chapter1/1chapter.txt` + `story/chapter2..17/*chapter.md` (chapters 1--17 only).
- YAML front matter excluded from counts.
- Fenced code blocks excluded from sentence/paragraph counts (to avoid Discord-log formatting skew).
- Sentence splitting is heuristic (split on `.?!` + whitespace); treat all numbers below as *approximate but comparable*.
- "Dialogue" counted two ways:
  - Paragraph-level: a paragraph contains at least one `"` character.
  - Word-level: words found inside simple `"..."` spans (also catches occasional non-dialogue quoted terms).

## Corpus snapshot (overall)

- Total words: ~49,267
- Sentences: ~4,050
- Prose paragraphs: 1,626
- Average sentences per paragraph: 2.49 (median 2)
- Single-sentence paragraphs: 442 / 1,626 = 27.2%

## Sentence patterns

### Sentence length + rhythm

- Sentence length (words): mean 12.1, median 11
- Percentiles: p10=3, p25=6, p75=17, p90=23
- Signature rhythm: frequent short punch-ins embedded between longer descriptive lines.
  - Fragment/beat example: `Nothing.` (Ch. 16)
  - Short emphatic sentence example: `But something was wrong.` (Ch. 16)
  - Long-with-asides example: `My Gyarados---level 40, carefully trained, survivor of multiple gym battles...---was down to just a sliver of health.` (Ch. 1)

### Sentence openers (how sentences start)

Counts below are per-sentence opener *category* (4054 sentences total):

- Proper/Name: 31.9% (often character-name subjects: `Kayla had dozed off twice...` (Ch. 9))
- Dialogue: 22.0% (`"What's your name?"` (Ch. 8))
- Determiner: 21.1% (setting/objects: `The convenience store's fluorescent lights buzzed overhead...` (Ch. 2))
- Pronoun: 13.6% (`I woke up to a throbbing headache.` (Ch. 17))
- Prepositional: 3.2% (`Through the mayhem, I caught glimpses of other tanks like mine...` (Ch. 1))
- Temporal: 2.9% (`As the sound of tires on dirt faded into the distance...` (Ch. 12))
- Conjunction: 2.8% (`But the street stretched empty in both directions.` (Ch. 1))
- Participial (-ing): 1.4% (`Moving left, I found a much more varied assortment of colors.` (Ch. 7))

### Opener variety *within* paragraphs

- Average unique opener-categories per paragraph: 1.88 (median 2)
- Among multi-sentence paragraphs (n=1184), 14.3% use the *same* opener-category for every sentence (often a "name/subject" run, or a dialogue run).
- Same-first-word runs are rare: only ~1.7% of multi-sentence paragraphs have a max run-length >=3 (e.g., three sentences starting with `I` / `He` / `"..."`).

## Paragraph structure

### Paragraph length (sentences per paragraph)

Distribution (1,626 paragraphs):

- 1 sentence: 442 (27.2%)
- 2 sentences: 515 (31.7%)
- 3 sentences: 341 (21.0%)
- 4 sentences: 187 (11.5%)
- 5+ sentences: 141 (8.7%)

What single-sentence paragraphs tend to do mechanically:

- Impact/verification beats: `Nothing.` (Ch. 16)
- Hard emotional turn: `But something was wrong.` (Ch. 16)
- Tone punctuation via kaomoji / symbol-only lines: `\\\[0.0\\]/` (Ch. 7)

### Paragraph transitions (how new paragraphs start)

First token of paragraph (very rough signal):

- Paragraphs starting with dialogue (`"`): 447 / 1,626 = 27.5%
- Temporal lead-ins (Then/When/After/Before/As/While/etc.): 65 paragraphs (~4.0%)
  - Example: `Then came a sound that defied description---...` (Ch. 1)
- Contrast lead-ins (But/However/etc.): 22 paragraphs (~1.4%)
  - Example: `But the street stretched empty in both directions.` (Ch. 1)

Net effect: chapters rely more on *implicit* continuity (shared subject/space) than explicit transition words.

## Punctuation habits (counts normalized)

Counts below are across chapters 1--17 (front matter excluded; code fences excluded for the "prose-ish" line):

- Em dash marker `---`: 292 occurrences = 59.5 per 10k words
  - Aside insertion: `my world---one minute forty-five seconds.` (Ch. 1)
  - Parenthetical specificity: `My Gyarados---level 40...---was down...` (Ch. 1)
  - Interruption/cutoff: `"Those wings will---"` (Ch. 2)
  - Drumroll / list-snap: `Five options. Five ways... Five---` (Ch. 1)
- Ellipsis `...`: 217 occurrences = 44.3 per 10k words
  - Spoken trailing off: `"Hold on..."` (Ch. 8)
  - Hesitation: `"I..." I started, then stopped...` (Ch. 8)
  - Internal thought fragmentation: `This voice... wasn't mine.` (Ch. 1)
- Semicolons `;`: 4 occurrences = 0.82 per 10k words (rare)
  - Example: `His eyes were red and swollen; he looked at me...` (Ch. 1)
- Colons `:`: 46 occurrences = 9.38 per 10k words (moderate; often used for "definition/reframe" beats)
  - Example: `Physics asserted itself with elegant simplicity: mass plus velocity equals the end.` (Ch. 1)
  - Example: `...a hypothesis waiting to be proven: "Delia..."` (Ch. 6)
- Parentheses `(`: 9 occurrences = 1.84 per 10k words (very rare in narration; more common around emoticon beats)
  - Example: `...sneaking into the greenhouse (okay, that wasn't great)...` (Ch. 7)
  - Example: `(\~\_\~)` (Ch. 3)

## Dialogue mechanics

### How much dialogue (by paragraph + by word)

- Dialogue paragraphs (contain at least one `"`): 698 / 1,626 = 42.9%
- Quoted-word ratio: ~7,057 / 49,140 = 14.4% of words are inside `"..."` spans
  - Chapter-level quoted-word ratio ranges from ~3% (Ch. 1, Ch. 7) up to ~25% (Ch. 6, Ch. 17).

### Tags vs action beats vs untagged (approximate)

Heuristic: in dialogue paragraphs, look for a speech-verb (said/asked/muttered/etc.) within ~160 characters after a closing quote.

- Dialogue paragraphs with an explicit nearby tag verb: 224 / 698 = 32.1%
- Dialogue paragraphs with `said` or `asked` nearby: 121 / 698 = 17.3%
- Most common nearby tag verbs (counts of matches): `said` (100), `asked` (25), `muttered` (20), `shouted` (14), `called` (13), `whispered` (12)
  - Tag example: `"Sir," she said...` (Ch. 2)
  - Action-beat-heavy example: `"I..." I started, then stopped...` (Ch. 8)

Interpretation (mechanical, not evaluative): dialogue is frequently carried by *context + beats* rather than repeated `said/asked` tagging.

### Interleaving spoken dialogue with internal reaction

Heuristic: a dialogue paragraph is "mixed" if it contains quotes *and* at least ~5 words outside the quoted spans.

- Mixed dialogue paragraphs: ~83% of dialogue paragraphs
  - Example: `"I..." I started, then stopped, unsure of what to say next.` (Ch. 8)
  - Example: `"Don't worry!" he boomed...` + immediate physical reaction context (Ch. 17)

## Repetition + verbal tics (countable motifs)

### Repeated phrases (exact-string counts, case-insensitive)

- `for a moment`: 29
- `for a long moment`: 8
- `before I could`: 16
- `cut through the`: 19
- `through the air`: 15

Examples:

- `For a moment, I thought...` (Ch. 1)
- `...before I could stop...` (Ch. 14 / Ch. 15)
- `Dr. Fuji's voice knifed through the night.` (Ch. 15) (same construction-family as `cut through the`)

### Body-language / perception motifs (bigram counts)

These are common enough to function as mechanical "camera anchors":

- `his voice`: 42
- `his eyes`: 36
- `her eyes`: 28
- `the air`: 41

Examples:

- `His voice sharpened.` (Ch. 2)
- `Our eyes met...` (Ch. 1)

### Hedges / uncertainty markers (exact counts, case-insensitive)

Across the corpus:

- `probably`: 31
- `kind of`: 27
- `maybe`: 23

Examples:

- `It had probably practiced that look in the mirror.` (Ch. 1)
- `...you could kinda tell it was me.` (Ch. 8)

## Chapter structure (open/close + scene signaling)

### How chapters open (first sentence opener category)

Across 17 chapters:

- Determiner: 9 chapters (setting-object openers)
  - Example: `The world beyond my container was a blur...` (Ch. 1)
- Pronoun: 3 chapters (immediate narrator state)
  - Example: `I woke up to a throbbing headache.` (Ch. 17)
- Proper/Name: 2 chapters (start on a named character)
  - Example: `Kayla had dozed off twice...` (Ch. 9)
- Temporal: 2 chapters (time-hook)
  - Example: `Today's dress hung on my closet door like a ghost.` (Ch. 11)
- Dialogue: 1 chapter
  - Example: `"What's your name?"` (Ch. 8)

### How chapters close (last sentence end-shape)

After stripping trailing quotes/slashes for punctuation classification:

- Period endings: 12 / 17
  - Example: `Fuji's frown.` (Ch. 10)
- Exclamation endings: 2 / 17
  - Example: `Onwards to the Celadon Gym!` (Ch. 3)
- Question endings: 1 / 17
  - Example: `"Delia?"` (Ch. 14)
- Ellipsis endings: 1 / 17
  - Example: `..."Delia..."` (Ch. 6)
- Non-punctuation / symbol endings: 1 / 17
  - Example: `\\\[0.0\\]/` (Ch. 7)

### Scene breaks (explicit markers)

- Explicit scene-break lines are almost absent:
  - Only Ch. 1 uses a distinct marker: `-[?.?]-` (hard cut from lab-tank opening to phone/game scene).
  - No recurring `***` / `---`-as-separator patterns inside chapters (beyond YAML front matter).
- Practical implication: scene shifts are usually carried by paragraph breaks + subject/setting pivots, not typographic dividers.

## Per-chapter quick table

| Ch | Words | Mean sent len (wds) | Median sent len | 1-sent par % | Dialogue par % |
|---:|------:|-------------------:|---------------:|-------------:|--------------:|
| 1 | 2420 | 13.06 | 12 | 22.4% | 22.4% |
| 2 | 2715 | 9.16 | 6 | 28.7% | 20.9% |
| 3 | 2929 | 13.34 | 12 | 29.8% | 32.1% |
| 4 | 2213 | 12.26 | 11 | 17.4% | 52.2% |
| 5 | 2215 | 15.58 | 14 | 16.1% | 41.1% |
| 6 | 3253 | 11.81 | 10 | 22.4% | 60.2% |
| 7 | 2306 | 16.09 | 16 | 24.1% | 36.2% |
| 8 | 2255 | 15.39 | 14 | 28.6% | 53.6% |
| 9 | 3440 | 14.68 | 13 | 23.9% | 52.3% |
| 10 | 4003 | 13.33 | 13 | 25.6% | 52.8% |
| 11 | 2601 | 12.19 | 11 | 15.2% | 30.3% |
| 12 | 2217 | 11.83 | 11 | 24.3% | 51.4% |
| 13 | 1748 | 10.07 | 10 | 15.1% | 35.8% |
| 14 | 4157 | 10.98 | 10 | 30.0% | 55.0% |
| 15 | 3054 | 11.77 | 11 | 31.2% | 37.5% |
| 16 | 4140 | 11.14 | 9 | 38.2% | 33.7% |
| 17 | 3601 | 10.10 | 9 | 34.0% | 49.7% |

</AI>
