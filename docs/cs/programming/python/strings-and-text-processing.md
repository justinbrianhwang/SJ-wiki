---
title: Strings and Text Processing
sidebar_position: 6
---

# Strings and Text Processing

Strings appear early in Python because the first program usually prints text. The textbook introduces strings with quotes, indexing, slicing, `len()`, case conversion, replacement, splitting, and input. Those operations are enough to build many useful scripts: clean a line of data, parse a simple record, format a report, or ask a user for information.

Python strings are more than arrays of characters. They are immutable Unicode text objects with a rich method library. Once you understand immutability, indexing, slicing, formatting, and the difference between text and bytes, string processing becomes predictable. The goal is not to memorize every method; it is to recognize the small set of transformations that show up repeatedly.

## Definitions

A **string** is an instance of `str`, written with single quotes, double quotes, or triple quotes:

```python
name = "Python"
same = 'Python'
message = """multiple
lines"""
```

Python strings are **immutable**. Methods such as `.lower()` and `.replace()` return new strings; they do not modify the original object.

An **index** selects one character by position. Python uses zero-based indexing:

```python
word = "Python"
word[0]  # "P"
word[1]  # "y"
word[-1] # "n"
```

A **slice** selects a range:

```python
word[1:4]  # "yth"
word[:2]   # "Py"
word[2:]   # "thon"
```

The stop index is excluded. This rule makes slice lengths easy: `word[a:b]` has length `b - a` when the indices are in range.

An **escape sequence** represents a character that is hard to type directly. Common examples are `\n` for newline and `\t` for tab. A **raw string**, prefixed with `r`, treats backslashes more literally and is often used for regular expressions and Windows paths:

```python
pattern = r"\d+"
```

An **f-string** is a formatted string literal:

```python
temperature = 21.456
print(f"{temperature:.1f} C")
```

The expression inside braces is evaluated, and format specifiers control presentation.

## Key results

The first key result is that string operations return new values. If you write:

```python
text = " Hello "
text.strip()
```

`text` is still `" Hello "`. You need:

```python
text = text.strip()
```

The second result is that splitting and joining are inverse patterns. `.split()` turns one string into a list of pieces. `.join()` turns many strings into one string:

```python
fields = "a,b,c".split(",")
line = ",".join(fields)
```

This pair is central to simple file processing.

The third result is that formatting should be separated from calculation. Keep numbers as numbers while computing, then format them at the output boundary. A value such as `"3.14"` is text; it cannot be used safely in numeric formulas until converted.

The fourth result is that text matching has levels. Use `in`, `.startswith()`, and `.endswith()` for simple checks. Use `.split()` for simple delimiters. Use the `csv` module for comma-separated data with quoting rules. Use `re` only when a real pattern language is needed.

The fifth result is that `str` and `bytes` are different. Files opened in text mode return strings. Files opened in binary mode return bytes. Encoding, usually UTF-8, is the mapping between them. Most beginner scripts should open text files with an explicit encoding:

```python
open("data.txt", encoding="utf-8")
```

## Visual

```text
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
Neg:    -6 -5 -4 -3 -2 -1

word[1:4] includes indexes 1, 2, 3:

P [y  t  h] o  n  -> "yth"
```

| Method | Purpose | Example | Result |
|---|---|---|---|
| `.strip()` | Remove surrounding whitespace | `" hi \n".strip()` | `"hi"` |
| `.lower()` | Normalize case | `"Py".lower()` | `"py"` |
| `.replace(a, b)` | Replace substrings | `"2020-01".replace("-", "/")` | `"2020/01"` |
| `.split(sep)` | Break into list | `"a,b".split(",")` | `["a", "b"]` |
| `sep.join(parts)` | Combine strings | `"-".join(["a", "b"])` | `"a-b"` |
| `.find(sub)` | Return index or `-1` | `"abc".find("b")` | `1` |
| `.startswith(prefix)` | Prefix test | `"data.csv".startswith("data")` | `True` |

## Worked example 1: parse a simple sensor line

Problem: parse the line `"time=10,temp=22.5,status=OK"` into useful values.

Method:

1. Split the line on commas to get fields.
2. Split each field on the first equals sign.
3. Store keys and values in a dictionary.
4. Convert numeric fields after parsing.

Work:

```python
line = "time=10,temp=22.5,status=OK"
fields = line.split(",")
record = {}

for field in fields:
    key, value = field.split("=", 1)
    record[key] = value

time_s = int(record["time"])
temp_c = float(record["temp"])
status = record["status"]
```

Step-by-step:

1. `line.split(",")` gives `["time=10", "temp=22.5", "status=OK"]`.
2. `"time=10".split("=", 1)` gives `["time", "10"]`, so store `"time": "10"`.
3. `"temp=22.5"` becomes `"temp": "22.5"`.
4. `"status=OK"` becomes `"status": "OK"`.
5. Convert `"10"` to integer `10`.
6. Convert `"22.5"` to float `22.5`.

Checked answer:

```python
time_s == 10
temp_c == 22.5
status == "OK"
```

This is a simple format. If the format allowed quoted commas, use the `csv` module instead of manual splitting.

## Worked example 2: format a report line

Problem: print a table of temperatures with aligned names and one decimal place.

Data:

```python
rows = [("Oslo", 4.25), ("Seoul", 21.8), ("Cairo", 30.125)]
```

Method:

1. Choose column widths.
2. Use an f-string for alignment and numeric precision.
3. Keep the original values numeric.

Work:

```python
for city, temp in rows:
    print(f"{city:<10} {temp:>6.1f} C")
```

Step-by-step:

1. `{city:<10}` means left-align the city in a field of width `10`.
2. `{temp:>6.1f}` means right-align the number in width `6` with one digit after the decimal point.
3. `"Oslo"` becomes `"Oslo      "`.
4. `4.25` rounds to `4.2` for display because one decimal place is requested.
5. `30.125` displays as `30.1` under usual binary floating-point and formatting behavior.

Checked output:

```text
Oslo          4.2 C
Seoul        21.8 C
Cairo        30.1 C
```

The numbers are still stored as floats in `rows`; only the printed representation is rounded.

## Code

```python
def normalize_name(text):
    parts = text.strip().split()
    return " ".join(part.capitalize() for part in parts)


def parse_key_value_line(line):
    result = {}
    for field in line.strip().split(","):
        if not field:
            continue
        key, value = field.split("=", 1)
        result[key.strip().lower()] = value.strip()
    return result


name = normalize_name("  ada   lovelace ")
record = parse_key_value_line("time=10, temp=22.5, status=OK")

print(name)
print(record)
```

The code demonstrates whitespace normalization, splitting, joining, generator expressions, case normalization, and defensive handling of empty fields.

## Common pitfalls

- Expecting string methods to modify the original string. Assign the returned value.
- Forgetting that indexes start at zero and that slice stop positions are excluded.
- Using manual string splitting for full CSV, JSON, or XML formats. Use the standard library parsers.
- Converting numbers to strings too early, then needing arithmetic later.
- Building long output with repeated `+` concatenation in a loop. Accumulate pieces and use `"".join(parts)` or write directly to a file.
- Forgetting explicit encodings when reading and writing text files across machines.
- Overusing regular expressions for simple prefix, suffix, or delimiter problems.

## Connections

- [Syntax, Variables, and Types](/cs/programming/python/syntax-variables-and-types)
- [Operators and Expressions](/cs/programming/python/operators-and-expressions)
- [Files and Context Managers](/cs/programming/python/files-and-context-managers)
- [Standard Library Highlights](/cs/programming/python/standard-library-highlights)
