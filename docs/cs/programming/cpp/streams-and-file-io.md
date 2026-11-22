---
title: Streams and File I/O
sidebar_position: 11
---

# Streams and File I/O

Streams give C++ a uniform model for input and output. Keyboard input, screen output, file input, file output, and string parsing all use objects that move characters into or out of a program. Savitch emphasizes that once a stream is opened, file I/O looks much like the `cin` and `cout` operations used in early console programs.

The important design habit is to treat I/O as a stateful process that can fail. Opening a file can fail. Reading can fail. A loop can accidentally process stale data after an unsuccessful extraction. Good file programs check stream state and structure loops around successful reads.

## One interface for several data sources

An **input stream** provides data to a program. An **output stream** receives data from a program.

```cpp
std::cin  // standard input stream
std::cout // standard output stream
std::cerr // standard error stream
```

File streams are declared in `<fstream>`.

```cpp
#include <fstream>

std::ifstream input;
std::ofstream output;
```

Opening connects a stream variable to an external file name.

```cpp
input.open("scores.txt");
output.open("report.txt");
```

The constructor form opens at declaration:

```cpp
std::ifstream input("scores.txt");
std::ofstream output("report.txt");
```

The extraction operator `>>` reads formatted data. The insertion operator `<<` writes formatted data.

```cpp
int score;
input >> score;
output << score << '\n';
```

Character I/O uses functions such as `get`, `put`, `peek`, `putback`, and `ignore`.

```cpp
char ch;
input.get(ch);
output.put(ch);
```

`std::stringstream`, from `<sstream>`, treats a string as a stream. It is useful for parsing and formatting without files.

```cpp
#include <sstream>

std::stringstream parser("12 34");
int a;
int b;
parser >> a >> b;
```

Streams maintain a formatting state, a buffer, and status flags. An extraction first consults formatting rules, then attempts to consume characters, and finally updates status. The stream's conversion to Boolean reports whether neither `failbit` nor `badbit` is set, which is why it fits directly in `if` and `while` conditions.

The standard streams have different roles. `std::cout` is buffered ordinary output, `std::cerr` is intended for diagnostics and is configured to flush more eagerly, and `std::clog` is buffered diagnostic output. Buffering reduces operating-system writes. An ordinary newline does not universally force a flush; `std::endl` writes a newline and flushes, while a newline character is preferable when immediate delivery is unnecessary.

## Reads succeed or change the stream state

Always test whether opening succeeded:

```cpp
std::ifstream input("data.txt");
if (!input) {
    std::cerr << "Could not open data.txt\n";
    return 1;
}
```

The most reliable input loop is usually shaped around the read itself:

```cpp
int value;
while (input >> value) {
    // process value
}
```

This avoids the classic end-of-file error where a loop checks `eof()` too early. `eof()` becomes true only after an attempted read passes the end marker.

Output formatting is stream state. Once set, formatting remains active for that stream until changed.

```cpp
#include <iomanip>

std::cout << std::fixed << std::setprecision(2);
```

Appending to a file uses an open mode:

```cpp
std::ofstream log("events.txt", std::ios::app);
```

Streams generally should not be copied. If a function needs to read from or write to a stream, pass the stream by reference.

```cpp
void copyLines(std::istream& in, std::ostream& out);
```

Random access file operations use positions, such as `seekg`, `tellg`, `seekp`, and `tellp`, but many beginner file problems are sequential and should be solved sequentially first.

Four state queries distinguish common outcomes:

| Query | Meaning |
|---|---|
| `good()` | no state flag is set |
| `eof()` | an operation encountered end of input |
| `fail()` | formatted extraction or another operation failed |
| `bad()` | a serious I/O error occurred |

`eofbit` and `failbit` can both be set by an extraction that tries to read past the final token. After a loop ends, malformed text can be distinguished from normal exhaustion by considering what format was expected and examining the flags. Calling `clear()` resets flags but does not remove the offending characters; recovery normally also uses `ignore` or a line read.

Streams can be configured to throw `std::ios_base::failure` for selected state changes through `exceptions()`. The default state-testing style is often clearer for expected parse failures. Exception mode can fit code where an I/O failure must cross several layers, but the recovery boundary still needs to know whether partial output or partial parsing occurred.

Text and binary modes differ. Formatted operators encode textual representations and respect whitespace rules. `read` and `write` move a specified number of raw characters. Directly dumping a class object's bytes is rarely a portable serialization format because padding, byte order, pointer values, and class layout may differ across builds and machines.

## The stream sits between characters and typed values

```mermaid
flowchart LR
  F[External file] -->|open ifstream| IN[input stream object]
  IN -->|"operator>> or get"| P[Program variables]
  P -->|"operator<< or put"| OUT[output stream object]
  OUT -->|open ofstream| G[External file]
```

| Task | Tool | Notes |
|---|---|---|
| read formatted numbers | `while (in >> x)` | safest basic loop |
| read one character | `in.get(ch)` | includes whitespace |
| read a line | `std::getline(in, line)` | use with `std::string` |
| skip rest of line | `in.ignore(...)` | useful after formatted extraction |
| append output | `std::ios::app` | preserves existing content |
| parse a string | `std::stringstream` | stream operations on memory text |

Formatted extraction for an integer skips leading whitespace, consumes a valid numeric prefix, and stops before the first character that cannot belong to the number. Reading `42xyz` into an integer succeeds with value `42`; the letters remain for the next operation. A parser that requires the entire field to be numeric must check for trailing non-whitespace characters.

## Worked example: summing numbers from a file

Problem: A file contains whitespace-separated integers. Compute their sum and count.

Method:

1. Open the file.
2. Check the stream state.
3. Initialize `sum = 0` and `count = 0`.
4. Use `while (input >> value)` so each iteration has a valid new integer.
5. Add the value and increment the count.
6. Print the result.

```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream input("numbers.txt");
    if (!input) {
        std::cerr << "Could not open numbers.txt\n";
        return 1;
    }

    int value;
    int sum = 0;
    int count = 0;

    while (input >> value) {
        sum += value;
        ++count;
    }

    std::cout << "Count: " << count << '\n';
    std::cout << "Sum: " << sum << '\n';
}
```

Checked answer: if `numbers.txt` contains `4 10 -3 9`, the loop runs four times.

$$
4 + 10 + (-3) + 9 = 20
$$

The program prints `Count: 4` and `Sum: 20`.

After the loop, a strict version should reject a non-integer token. If the next unread text is `oops`, extraction sets `failbit` without reaching normal end of file. The partial sum may still be useful for an interactive tool, but a batch calculation should report the malformed record and avoid presenting the partial result as complete. The sum itself can overflow `int`; input range and required total determine whether a wider or checked accumulator is needed.

## Worked example: numbering lines in an output file

Problem: Copy a text file line by line and prefix each line with its line number.

Method:

1. Open input and output files.
2. Check both.
3. Read with `std::getline`, not `>>`, because spaces inside lines matter.
4. Maintain a line counter starting at `1`.
5. Write counter, colon, line text, and newline.

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream input("story.txt");
    std::ofstream output("numbered_story.txt");

    if (!input || !output) {
        std::cerr << "File open failed\n";
        return 1;
    }

    std::string line;
    int lineNumber = 1;

    while (std::getline(input, line)) {
        output << lineNumber << ": " << line << '\n';
        ++lineNumber;
    }
}
```

Checked answer: if `story.txt` contains:

```text
red
blue sky
```

then the output file contains:

```text
1: red
2: blue sky
```

The space in `blue sky` is preserved because `getline` reads the full line.

Successful writes can still be buffered when the loop ends. Destruction closes the stream and flushes its buffer, but errors during that final flush are difficult to report from a destructor. Code that must guarantee complete output should explicitly `flush` or `close`, then inspect stream state. Even a successful close does not necessarily imply physical media durability; that stronger guarantee is platform-specific.

## Parsing a deliberately simple comma-separated format

This program reads comma-separated `name,score` lines using `std::getline` and `std::stringstream`.

```cpp
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::ifstream input("scores.csv");
    if (!input) {
        std::cerr << "Could not open scores.csv\n";
        return 1;
    }

    std::string line;
    while (std::getline(input, line)) {
        std::stringstream row(line);
        std::string name;
        std::string scoreText;

        if (std::getline(row, name, ',') && std::getline(row, scoreText)) {
            std::stringstream scoreParser(scoreText);
            int score;
            if (scoreParser >> score) {
                scoreParser >> std::ws;
                if (!scoreParser.eof()) {
                    std::cerr << "Trailing text in score: " << scoreText << '\n';
                    continue;
                }
                std::cout << name << " scored " << score << '\n';
            }
        }
    }
}
```

The trailing check prevents a field such as `90points` from being accepted as score `90`. Blank lines and missing commas are skipped by this small example; a real importer should report line numbers and choose whether one bad row aborts the file.

This is not a complete CSV parser. Standard CSV-style data may quote fields, place commas inside quotes, and escape quote characters. Splitting at the first comma cannot implement those rules. For a controlled two-field format with unquoted names, the code is adequate; for general CSV, use a parser with an explicit dialect rather than adding ad hoc cases.

## State, buffering, and format traps

- Failing to check whether a file opened successfully.
- Writing `while (!input.eof())` and processing data after a failed read.
- Forgetting that opening an existing output file normally truncates it.
- Forgetting `std::ios::app` when the goal is appending.
- Passing file streams by value instead of by reference.
- Mixing `>>` and `getline` without consuming the leftover newline.
- Assuming `get` skips whitespace. It reads the next character exactly.
- Forgetting that stream formatting settings persist.

When diagnosing I/O:

- Always check that a file stream opened successfully before reading or writing. A failed open does not automatically stop the program, so later reads may silently fail.
- Separate parsing from processing. A function that reads one record and returns whether it succeeded is easier to test than a function that reads, computes, prints, and handles errors all at once.
- Know the difference between formatted extraction and line input. `operator>>` skips leading whitespace and stops at the next whitespace; `getline` reads through the newline.
- When switching from `>>` to `getline`, consume the leftover newline first. Otherwise the first `getline` may read an empty line that was already waiting in the input buffer.
- Treat end-of-file as a state discovered after a read attempt. The common loop pattern is "while reading succeeds, process the value," not "while not EOF, read."
- Use output formatting deliberately. `fixed`, `setprecision`, and field widths affect stream state and may remain in effect for later output.
- Close files explicitly when doing so clarifies the program, but remember that file stream destructors close their files automatically when the stream object goes out of scope.

Write the input loop in the form "while the read succeeds, process the value." For numbers, that may be `while (in >> value)`. For records, it may be a helper function that returns `true` only after reading every field. The shape avoids processing stale data after a failed read.

When output formatting looks wrong, remember that stream manipulators can be sticky. `fixed` and `setprecision(2)` continue affecting later floating-point output on the same stream. Either set formatting near the output that needs it or deliberately restore the stream state in larger programs.

File I/O bugs are often path bugs. Verify whether the program's working directory is the directory you expect, and print the filename being opened when debugging. A correct parser cannot read a file that was never opened.

The program should distinguish a file that did not open, a read that failed because the data format was wrong, and a read that ended normally at end-of-file. Treating all three as "no more input" hides important errors.

Destination independence is easy to test: write one program that reads from `cin`, then change only the stream object so it reads from an `ifstream`. Formatted extraction and line-reading code can often work with console and file input through the same operations.

For output, redirect results to `cout` first, then to an `ofstream`. Keeping the formatting code independent of the destination makes it easier to test before files are involved.

Test file programs with an empty file, a one-record file, a malformed file, and a missing file. Those four cases expose most stream-state mistakes before larger datasets hide them.

Opening an `ofstream` with the default mode truncates an existing file as part of opening it. When overwriting valuable data, a safer update writes a new temporary file, checks the complete write and close, and then replaces the destination using filesystem operations appropriate to the platform. Opening the target before validation can destroy the old contents even if later processing fails.

Mixing formatted extraction and `getline` is best handled by defining a record boundary. `std::getline(in >> std::ws, line)` discards leading whitespace, including blank lines, which may or may not match the file format. If empty lines are meaningful, consume exactly the pending newline after the formatted field rather than applying `std::ws` broadly.

Stream positions are opaque position types, not always simple byte indexes in text mode. Seeking to a previously obtained position is supported; calculating arbitrary text offsets is less portable because external encodings and newline translation can intervene. Binary mode is the usual choice for byte-exact offsets.

Output can fail after opening because a device fills, a connection closes, or a buffered write is rejected. Checking only the constructor misses those later errors. A report generator that promises a file should test the stream after its final write and close before announcing success. Input streams likewise may encounter a low-level error distinct from clean end of file; `bad()` identifies that stronger failure category.

<div className="see-also">

See also: [C++ basics and control flow](/cs/programming/cpp/cpp-basics-and-control-flow) · [strings](/cs/programming/cpp/strings) · [separate compilation and namespaces](/cs/programming/cpp/separate-compilation-and-namespaces) · [exception handling](/cs/programming/cpp/exception-handling) · [STL algorithms and iterators](/cs/programming/cpp/stl-algorithms-and-iterators)

</div>
