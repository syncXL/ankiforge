### BASIC REVERSED

Description:
Identical content structure to Basic, but the recall direction is flipped.
Direction: definition/description → term. The student sees a description and must name the concept.
Front: definition, explanation, or description.
Back: the term, concept name, formula label, or classification being identified.

When to use:
- When bidirectional recall matters: a student should know both the term → definition
  direction AND the definition → term direction.
- Terminology-heavy subjects where both directions are actively tested: pharmacology,
  anatomy, law, biochemistry.
- When the back of a Basic card is distinctive enough to serve as a standalone prompt —
  reading the description should lead the student to exactly one answer.

When NOT to use:
- Do NOT generate a Basic Reversed card for every Basic card automatically.
  Only reverse a concept when the reverse direction is genuinely testable.
- When the description on the front could match multiple terms — do not reverse it.
  ✅ "The process by which glucose is broken down in the cytoplasm to produce pyruvate." → Glycolysis
  ❌ "A biological process." → too vague, points to many possible answers
- When the back of the Basic card is too long or too generic to serve as a useful front.

Answer structure:
- FRONT: the definition, description, or functional explanation.
  Must be specific and unambiguous — reading it must lead to exactly one answer.
  Must NOT contain the term being tested anywhere in the text.
  ✅ "The process by which glucose is broken down in the cytoplasm to produce pyruvate."
  ❌ "Glycolysis is the process by which glucose is broken down..." — gives away the answer
- BACK: the term, concept name, or label. Usually 1–5 words.
  Stage 2 will use FRONT and BACK to generate the hint and tags.

Flashcard writing techniques:
- The front must be written so that only one answer is correct.
  If two or more terms could satisfy the description, rewrite the front to be more specific
  or do not generate this card.
- Do not copy text verbatim from the source material. Paraphrase the description.
- The front must not contain the answer or any synonym of the answer.
- The back must draw only from the source material.
- A Basic card and a Basic Reversed card on the same concept are NOT duplicates —
  they test opposite directions. Both may appear in the same output batch.

Output format:
FRONT: <definition or description — must not contain the answer>
BACK: <term or concept name — 1 to 5 words>
TYPE: basic reversed

Example:
FRONT: A protein that lowers the activation energy of a chemical reaction without
       being consumed in the process.
BACK: Enzyme
TYPE: basic reversed