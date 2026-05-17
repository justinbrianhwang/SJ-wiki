## MERMAID SYNTAX REVIEW POLICY

Walk every `.md` file in the target section. For each ```mermaid``` block, audit it for **runtime parse failures** that the markdown build does not catch (Mermaid renders client-side, so MDX build success ≠ valid Mermaid).

### Common bad patterns to fix

1. **Unquoted labels with special characters**. Mermaid label parser breaks on `[`, `]`, `{`, `}`, `(`, `)`, `=`, `:`, `,`, `<`, `>`, `&`, `|`, `'`, `"` if they appear inside an unquoted node label. Wrap the **whole** label in `"..."`. If the label already contains a literal `"`, replace internal `"` with the HTML entity `#quot;`.

   - ❌ `A[x_{t-1} from token, shape (B, T, D)]`
   - ✅ `A["x_{t-1} from token, shape (B, T, D)"]`

2. **Unsupported HTML entities**. Mermaid supports `#quot;` and a few decimal/hex numeric refs, but NOT named entities like `#lsqb;`, `#rsqb;`, `#lbrace;`. If you see `#lsqb;` or `#rsqb;`, replace with literal `(` and `)` (we already changed all known cases — be sure to catch any remaining).

3. **Tensor shapes in labels**. `[N, 100, 1, 1]` inside an unquoted label parses as a nested node definition. Convert square-bracket shapes to round brackets `(N, 100, 1, 1)` OR wrap the whole label in `"..."`.

4. **Subgraph titles with special chars** must be quoted:

   - ❌ `subgraph Stage1 (×3)`
   - ✅ `subgraph Stage1["Stage 1 (×3)"]`

5. **Edge labels with special chars** must be inside the `|...|`:

   - `A -->|"K, V (keys and values)"| B`

6. **`<br/>` in labels** must be inside quoted labels:

   - ✅ `A["line one<br/>line two"]`

7. **Stray `#quot;` artifacts** anywhere → strip and re-wrap.

8. **Sequence diagram `participant` names with spaces** must be quoted or aliased:

   - ❌ `participant Alice Quantum`
   - ✅ `participant Alice as "Alice Quantum"`

9. **State machine `state` names** with parens or special chars must be quoted similarly.

10. **Unbalanced brackets**: every `[` needs a `]`, every `(` needs a `)`, every `{` needs a `}` in a label.

### Validation approach for each block

For each ```mermaid block:

- Read first line to detect type: `flowchart`, `graph`, `stateDiagram-v2`, `sequenceDiagram`, `classDiagram`, `gantt`, etc.
- Walk node definitions and check each label.
- If any label contains the special characters listed in rule 1 AND is not wrapped in `"..."`, wrap it.
- If `#lsqb;`/`#rsqb;` still appears anywhere, replace with `(`/`)`.
- If any literal `"` appears inside an already-`"..."` label, replace internal `"` with `#quot;`.
- If subgraph or edge label has parens/special chars, quote.

### What NOT to touch

- Diagram content itself (structure, arrow directions, layout) — only fix **syntax errors and known parse-failing patterns**.
- Surrounding markdown (text, math `$..$`/`$$..$$`, code blocks) — leave alone.
- Already-correct diagrams.

### Output expectation

End-of-run summary: list how many files modified and how many distinct issues fixed (briefly categorized).

---

Section-specific instructions follow.

---

