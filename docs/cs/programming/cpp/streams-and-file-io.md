---
title: Streams and File I/O
sidebar_position: 11
---

# Streams and File I/O

Streams give C++ a uniform model for input and output. Keyboard input, screen output, file input, file output, and string parsing all use objects that move characters into or out of a program. Savitch emphasizes that once a stream is opened, file I/O looks much like the `cin` and `cout` operations used in early console programs.

The important design habit is to treat I/O as a stateful process that can fail. Opening a file can fail. Reading can fail. A loop can accidentally process stale data after an unsuccessful extraction. Good file programs check stream state and structure loops around successful reads.

## Definitions

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

## Key results

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

## Visual

```mermaid
flowchart LR
  F[External file] -->|open ifstream| IN[input stream object]
  IN -->|operator>> or get| P[Program variables]
  P -->|operator<< or put| OUT[output stream object]
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

## Worked example 1: summing numbers from a file

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

$$4 + 10 + (-3) + 9 = 20$$

The program prints `Count: 4` and `Sum: 20`.

## Worked example 2: cleaning line numbers into an output file

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

## Code

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
                std::cout << name << " scored " << score << '\n';
            }
        }
    }
}
```

## Common pitfalls

- Failing to check whether a file opened successfully.
- Writing `while (!input.eof())` and processing data after a failed read.
- Forgetting that opening an existing output file normally truncates it.
- Forgetting `std::ios::app` when the goal is appending.
- Passing file streams by value instead of by reference.
- Mixing `>>` and `getline` without consuming the leftover newline.
- Assuming `get` skips whitespace. It reads the next character exactly.
- Forgetting that stream formatting settings persist.

I/O diagnostic checks:

- Always check that a file stream opened successfully before reading or writing. A failed open does not automatically stop the program, so later reads may silently fail.
- Separate parsing from processing. A function that reads one record and returns whether it succeeded is easier to test than a function that reads, computes, prints, and handles errors all at once.
- Know the difference between formatted extraction and line input. `operator>>` skips leading whitespace and stops at the next whitespace; `getline` reads through the newline.
- When switching from `>>` to `getline`, consume the leftover newline first. Otherwise the first `getline` may read an empty line that was already waiting in the input buffer.
- Treat end-of-file as a state discovered after a read attempt. The common loop pattern is "while reading succeeds, process the value," not "while not EOF, read."
- Use output formatting deliberately. `fixed`, `setprecision`, and field widths affect stream state and may remain in effect for later output.
- Close files explicitly when doing so clarifies the program, but remember that file stream destructors close their files automatically when the stream object goes out of scope.

Quick self-test: write the input loop in the form "while the read succeeds, process the value." For numbers, that may be `while (in >> value)`. For records, it may be a helper function that returns `true` only after reading every field. This pattern avoids processing stale data after a failed read.

When output formatting looks wrong, remember that stream manipulators can be sticky. `fixed` and `setprecision(2)` continue affecting later floating-point output on the same stream. Either set formatting near the output that needs it or deliberately restore the stream state in larger programs.

File I/O bugs are often path bugs. Verify whether the program's working directory is the directory you expect, and print the filename being opened when debugging. A correct parser cannot read a file that was never opened.

A final review question is whether the program distinguishes three different states: a file that did not open, a read that failed because the data format was wrong, and a read that ended normally at end-of-file. Treating all three as "no more input" hides important errors.

Extended practice: write one program that reads from `cin`, then change only the stream object so it reads from an `ifstream`. This demonstrates why stream interfaces are powerful: formatted extraction and line-reading code can often work with console input and file input using the same operations.

For output, redirect results to `cout` first, then to an `ofstream`. Keeping the formatting code independent of the destination makes it easier to test before files are involved.

One last check: test file programs with an empty file, a one-record file, a malformed file, and a missing file. Those four cases expose most stream-state mistakes before larger datasets hide them.

## Connections

- [C++ basics and control flow](/cs/programming/cpp/cpp-basics-and-control-flow)
- [strings](/cs/programming/cpp/strings)
- [separate compilation and namespaces](/cs/programming/cpp/separate-compilation-and-namespaces)
- [exception handling](/cs/programming/cpp/exception-handling)
- [STL algorithms and iterators](/cs/programming/cpp/stl-algorithms-and-iterators)
