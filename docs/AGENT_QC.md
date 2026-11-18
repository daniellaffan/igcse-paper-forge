# Brief: independent answer check (cold check)

You did **not** write these questions. Your job is to find questions that are wrong, ambiguous,
unanswerable, or whose mark scheme is wrong.

For each batch you are given (e.g. `data/bank/qc/batches/physics-004`):

1. Open **only** `<batch>.questions.md`. Answer every question cold, as a strong student would, with
   short working. Write your answers to `data/bank/qc/answers/<batch>.json` **before** opening the
   mark scheme:
   `{"batch": "<batch>", "answers": {"<question id>": {"<part label or 'all'>": "<your answer>"}}}`
   For long levels-marked essays, write a 2–4 line plan of the key points you would make instead.
2. Now open `<batch>.markscheme.md` and compare. Add a `"verdicts"` object to the same JSON file:
   `"verdicts": {"<question id>": {"result": "pass" | "fail", "problem": "<what is wrong, if fail>",
   "fix": "<the corrected answer / wording / marks, if you know it>"}}`
   - **pass**: your answer matches the mark scheme (allowing equivalent forms and sensible rounding), or
     the question is levels-marked and the indicative content is accurate and fits the question.
   - **fail**: wrong or missing answer in the mark scheme, a factual error, the question cannot be
     answered from the information given, a diagram/table contradicts the text, an MCQ has zero or
     several correct options, marks clearly don't fit the demand, or the question is off-spec.
3. Do not edit anything else. Reply with: batches done, pass count, fail count, one line per fail.

## Context budget (important)
Read ONLY your assigned batch files, this brief and the matching answers files. Never open
`data/bank/*/` JSON, generator scripts or the corpus. Keep working short: use `python3 -c` for
arithmetic and print only the result; essay plans 2–3 lines; verdict notes one sentence. Save each
batch's answers, then its verdicts, before starting the next batch. If an answers file already has
cold answers but no verdicts, do step 2 only and keep the answers unchanged.
