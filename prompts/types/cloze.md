### CLOZE

Description:
A fill-in-the-blank card where a key term or concept is deleted from a sentence.
Direction: context with gap → missing term. The student reads the sentence and must recall the deleted word or phrase.
Used for contextual recall — the student sees the surrounding information and must retrieve the missing piece.

When to use:
- Key terms, definitions, and concepts that are best understood in context.
- When the surrounding sentence provides meaningful retrieval cues.
- Technical vocabulary where phrasing and context matter — formulas, named processes, algorithm steps.
- When a Basic card would feel too decontextualised for the concept.

When NOT to use:
- When the blank could be filled by more than one plausible term — rewrite or do not generate.
- When the surrounding sentence is too short to provide meaningful context.
  ✅ "Gradient descent minimises the loss function by iteratively adjusting weights in the direction of the {{c1::negative gradient}}."
  ❌ "This is called {{c1::gradient descent}}." — no useful context
- When the deleted term appears elsewhere in the same sentence — gives away the answer.
- Procedural knowledge with many steps — do not cloze individual steps out of sequence.
- Do NOT generate more than one cloze deletion per card. One blank per card only.

Answer structure:
- FRONT: a complete, grammatically correct sentence with exactly one deletion marked as {{c1::term}}.
  The sentence must make sense when read with a blank in place of the deletion.
  The deleted term must not appear anywhere else in the sentence.
  Must be specific enough that only one term correctly fills the blank.
- BACK: the deleted term or phrase only. 1–6 words.
  No additional explanation on the back.

Flashcard writing techniques:
- One deletion per card. If two terms in a sentence are worth testing, generate two separate cards.
- Do not copy text verbatim from the source material. Paraphrase the sentence.
  The cloze sentence must be your own construction, not lifted text with a word removed.
- The sentence must remain meaningful and grammatically correct with the blank present.
- Delete the most important term in the sentence — the one that carries the concept being tested.
  Do not delete articles, prepositions, or contextual filler words.
- The back must draw only from the source material.
- Cognitive depth: intermediate by default.
  Focus on terms that describe mechanisms, processes, and cause-and-effect relationships.
  For definition-heavy sections, key vocabulary deletions are acceptable.

Output format:
FRONT: <complete sentence with exactly one {{c1::term}} deletion>
BACK: <deleted term — 1 to 6 words>
TYPE: cloze

Example:
FRONT: During backpropagation, the network adjusts its weights by computing the {{c1::gradient}} of the loss function with respect to each parameter.
BACK: gradient
TYPE: cloze