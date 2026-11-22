---
title: Control Flow, Arrays, and Strings
sidebar_position: 5
---

# Control Flow, Arrays, and Strings

Control flow determines which statements run, how often they run, and when a method returns. Java's constructs are familiar to C-family programmers: blocks, `if`, `switch`, `while`, `do`, `for`, labels, `break`, `continue`, and `return`. The source book emphasizes that these constructs are simple but precise. The right loop shape makes code easier to verify; the wrong one hides the condition that ends the computation.

Arrays and strings are the first compound data structures many Java programs use. An array is an object with a fixed length and indexed components. A `String` is an object representing a sequence of characters, and string operations create or use objects rather than changing a primitive value. Together, loops, arrays, and strings form the base of searching, counting, formatting, parsing, and many examples in later chapters.

## Branches, loops, and sequence types

The source combines Chapter 10 on statements and control flow, Chapter 7 on array variables, and Chapter 13 on strings and character sequences. Each construct fixes a scope, transfer rule, index range, or mutation model.

**Block.** A sequence of statements and local declarations enclosed in braces. It counts as one statement syntactically and creates a scope for its local variables.

**`if` statement.** A choice between a true branch and an optional false branch based on a boolean expression. Java does not use integers as boolean conditions.

**`switch` statement.** A selection among case labels based on a compatible expression value. In the source-era language, cases fall through unless `break`, `return`, or another transfer interrupts them.

**Loop.** A repeated statement. `while` tests before the body, `do` tests after it, and `for` groups initialization, test, and update in one header.

**Enhanced `for`.** A Java 5 loop over arrays and `Iterable` objects, useful when the index is not part of the algorithm.

**Array.** An object whose length is fixed at creation and whose components use zero-based integer indices. Every array has a `length` field.

**String.** An immutable character sequence. Concatenation and replacement produce new string values rather than changing the original object.

**`StringBuilder`.** A mutable builder for cases where repeated appending would create many intermediate `String` objects.

## Making termination and boundaries explicit

**Every loop needs a visible invariant.** A loop should make clear what remains true before and after each iteration. For an array scan, the invariant might be that all elements before index `i` have already been examined. Naming it helps place updates, `break`, and `continue` correctly.

**Fall-through is both feature and hazard.** `switch` fall-through can intentionally share code among cases, but an omitted `break` can silently run the next case. The source-era `switch` uses statement labels rather than isolated arms, so every fall-through should be obvious.

**Arrays are objects with fixed length.** Assigning an array variable copies a reference, not the contents. The length cannot change after creation. To grow a sequence, use a collection such as `ArrayList` or create a new array and copy components.

**Index boundaries are half-open in idiomatic loops.** The loop `for (int i = 0; i < a.length; i++)` visits indices `0` through `a.length - 1`. The first invalid index is exactly `a.length`. The same half-open convention appears in substrings and ranges.

**String immutability changes update strategy.** `s = s + part` computes a new string value and stores its reference in `s`; it does not mutate the original object. For repeated appends, `StringBuilder` states the intent and avoids unnecessary intermediate strings.

When debugging control flow, write down the exact transfer target of each `break`, `continue`, and `return`. An unlabeled `break` exits the nearest loop or `switch`; an unlabeled `continue` continues the nearest loop; a labeled form targets the labeled statement allowed by the language. When debugging arrays, write down the valid index interval `[0, length)`. When debugging strings, ask whether the operation returns a new string or mutates a builder. These habits turn vague runtime symptoms such as off-by-one errors, missing cases, and unexpected unchanged strings into concrete rule checks.

```mermaid
flowchart TD
  A[Start loop] --> B{"Index less than length?"}
  B -->|yes| C[Read array element]
  C --> D[Update result]
  D --> E[Increment index]
  E --> B
  B -->|no| F[Loop finished]
```

| Construct | Best fit | Key risk |
|---|---|---|
| `if` / `else` | One decision or small decision tree | Dangling or visually misleading branch |
| `switch` | Fixed set of cases | Accidental fall-through |
| `while` | Input- or condition-driven repetition | Condition never changes |
| `do` / `while` | Body must run at least once | Forgetting the post-test behavior |
| Classic `for` | Index or counter loop | Off-by-one condition |
| Enhanced `for` | Visit each element | Cannot naturally replace elements by index |

## Proving a maximum scan with an invariant

Problem: Given `int[] values = \{4, 9, 2, 9, 5\};`, find the maximum and show the loop invariant.

Method:

1. The array is nonempty, so initialize `max` with `values[0]`. At this point, `max` is the maximum of the examined prefix containing index `0`.
2. Start `i` at `1` because index `0` has already been included.
3. Before each iteration, the invariant is: `max` is the maximum among elements from index `0` through `i - 1`.
4. At `i = 1`, compare `values[1] = 9` with `max = 4`; update `max` to `9`.
5. At `i = 2`, compare `2` with `9`; keep `9`. At `i = 3`, compare `9` with `9`; keep `9`. At `i = 4`, compare `5` with `9`; keep `9`.
6. When `i == values.length`, the examined prefix is the whole array.

Checked answer: The maximum is `9`. The invariant proves the answer because the loop ends only after every valid index has been examined.

## Separators without a trailing comma

Problem: Build `red, green, blue` from `String[] names = \{"red", "green", "blue"\};` without leaving an extra comma.

Method:

1. Use `StringBuilder` because the algorithm appends several parts.
2. Loop over indices `0` through `names.length - 1`. The index is useful because the comma depends on position.
3. Before appending a name, check whether `i > 0`. If true, append `", "`; if false, append no separator.
4. Append `names[i]` after any needed separator.
5. After the loop, call `toString` to create the final immutable `String` result.

Checked answer: The result is `red, green, blue`. The separator rule is checked before each element after the first, so no leading or trailing comma appears.

## Scanning an array and assembling text

```java
public class ArrayStringDemo {
    public static void main(String[] args) {
        int[] values = { 4, 9, 2, 9, 5 };
        int max = values[0];
        for (int i = 1; i < values.length; i++) {
            if (values[i] > max) {
                max = values[i];
            }
        }

        String[] names = { "red", "green", "blue" };
        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < names.length; i++) {
            if (i > 0) {
                joined.append(", ");
            }
            joined.append(names[i]);
        }

        System.out.println("max = " + max);
        System.out.println(joined.toString());
    }
}
```

## Off-by-one and mutation mistakes

- Do not use `<= array.length` in an index loop. The valid index range ends at `array.length - 1`.
- Do not assume `switch` cases stop automatically. Add `break` unless fall-through is deliberate and obvious.
- Do not use an enhanced `for` loop when the algorithm needs the index for replacement, position-based separators, or neighboring elements.
- Do not expect `String` methods or concatenation to mutate an existing string object.
- Do not hide loop termination. A loop whose stopping condition is far from its update is harder to verify.

<div className="see-also">

See also:

- [Tokens, Values, and Variables](/cs/programming/java/tokens-values-variables): explains local variables, references, and array variables.
- [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions): explains boolean conditions and arithmetic updates.
- [Strings, Regular Expressions, Formatter, and Scanner](/cs/programming/java/strings-regex-formatter-scanner): develops string processing in detail.
- [Collections, Iteration, and Maps](/cs/programming/java/collections-iteration-maps): introduces growable collection alternatives to arrays.

</div>
