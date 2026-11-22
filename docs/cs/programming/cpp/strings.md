---
title: Strings
sidebar_position: 5
---

# Strings

C++ has two major string traditions. The older C-style representation stores text in an array of `char` terminated by the null character `'\0'`. The modern standard-library representation uses the class `std::string`, which manages storage and exposes string operations through member functions and overloaded operators. Savitch covers both because C-strings still appear in string literals, command-line arguments, old libraries, and low-level character processing.

The practical rule is simple: use `std::string` for ordinary application code, but understand C-strings well enough to read, interoperate with, and safely maintain code that uses them.

## Definitions

A **character** is a value of type `char`, usually written with single quotes:

```cpp
char initial = 'S';
char newline = '\n';
```

A **C-string** is an array of `char` whose meaningful characters end at the first null character `'\0'`.

```cpp
char word[6] = "Hello";
```

The array contains six characters:

```text
'H' 'e' 'l' 'l' 'o' '\0'
```

A C-string variable needs one more array slot than the maximum visible length. A buffer that can hold a 20-character word must have at least 21 elements.

```cpp
char name[21];
```

The `<cstring>` library provides functions such as `std::strlen`, `std::strcpy`, `std::strncpy`, `std::strcmp`, and `std::strcat` in many implementations. Older C-style code may use the global names.

The **standard string class** is declared in `<string>`.

```cpp
#include <string>

std::string title = "Absolute C++";
```

`std::string` objects support assignment, comparison, concatenation, indexing, size queries, and line input.

```cpp
std::string first = "Ada";
std::string last = "Lovelace";
std::string full = first + " " + last;
```

Character input tools include `get`, `put`, `peek`, `putback`, and `ignore`. They are useful when whitespace matters.

```cpp
char ch;
std::cin.get(ch); // reads spaces and newlines too
```

## Key results

C-strings are arrays, so they do not behave like ordinary assignable values after declaration. This is illegal:

```cpp
char text[20];
// text = "hello"; // not allowed
```

Use a copying function, and ensure the destination has room:

```cpp
char text[20];
std::strncpy(text, "hello", 19);
text[19] = '\0';
```

C-string equality is not tested with `==` in the intended sense. `==` compares array addresses after array-to-pointer conversion. Use `std::strcmp(a, b) == 0`.

`std::string` fixes these problems by defining value-style operations:

```cpp
std::string a = "hello";
std::string b = "hel";
b += "lo";
if (a == b) {
    std::cout << "same\n";
}
```

The null terminator is the crucial invariant of C-strings:

$$\text{valid C-string} \Rightarrow \exists i \text{ such that } a[i] = '\backslash 0'$$

Many C-string functions scan until they see `'\0'`. If the terminator is missing, the function may read beyond the array.

`std::getline` for strings reads a whole line, including spaces, up to but not including the newline:

```cpp
std::string line;
std::getline(std::cin, line);
```

The common trap is mixing formatted extraction with line input. After `std::cin >> number`, the newline remains in the input buffer, so a following `getline` may read an empty line. Use `ignore` to discard the rest of the current line.

```cpp
#include <limits>

std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```

## Visual

```text
C-string storage for "cat" in char word[6]

index:    0     1     2     3      4      5
       +-----+-----+-----+------+------ +------+
value: | 'c' | 'a' | 't' | '\0' |  ??  |  ??  |
       +-----+-----+-----+------+------ +------+
                         terminator
```

| Operation | C-string style | `std::string` style | Main risk |
|---|---|---|---|
| assignment | `strcpy(dest, src)` | `dest = src` | C buffer overflow |
| equality | `strcmp(a, b) == 0` | `a == b` | C `==` compares addresses |
| length | `strlen(s)` | `s.size()` | C requires terminator |
| concatenate | `strcat(dest, src)` | `dest += src` | C destination capacity |
| line input | `cin.getline(buf, n)` | `getline(cin, s)` | leftover newline |

## Worked example 1: why C-string equality needs `strcmp`

Problem: Determine whether two C-string variables contain the same visible text.

```cpp
char a[6] = "Hello";
char b[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```

Method:

1. `a` and `b` are separate arrays.
2. The expression `a == b` does not compare all characters.
3. In most expressions, each array name converts to a pointer to its first element.
4. Since `a[0]` and `b[0]` live in different array objects, their addresses differ.
5. `a == b` is therefore false even though the character sequences match.
6. `std::strcmp(a, b)` compares character by character until a difference or `'\0'`.

```cpp
#include <cstring>
#include <iostream>

int main() {
    char a[6] = "Hello";
    char b[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

    std::cout << std::boolalpha;
    std::cout << "a == b: " << (a == b) << '\n';
    std::cout << "strcmp equal: " << (std::strcmp(a, b) == 0) << '\n';
}
```

Checked answer: `a == b` prints `false` on normal separate arrays, while `strcmp equal` prints `true`.

## Worked example 2: fixing `cin >>` followed by `getline`

Problem: Read an integer age and then a full name that may contain spaces.

Naive code:

```cpp
int age;
std::string name;
std::cin >> age;
std::getline(std::cin, name);
```

Method:

1. Suppose the user types `20` and presses Enter.
2. `std::cin >> age` reads the digits `2` and `0`.
3. The newline remains waiting in the stream.
4. `getline` sees that newline immediately and returns an empty string.
5. Discard the rest of the current input line before calling `getline`.

```cpp
#include <iostream>
#include <limits>
#include <string>

int main() {
    int age;
    std::string name;

    std::cout << "Age: ";
    std::cin >> age;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Full name: ";
    std::getline(std::cin, name);

    std::cout << name << " is " << age << '\n';
}
```

Checked answer: if the input is `20` followed by `Grace Hopper`, the program stores `age == 20` and `name == "Grace Hopper"`.

## Code

This program normalizes a line by keeping only letters and converting them to lowercase, then tests whether the result is a palindrome.

```cpp
#include <cctype>
#include <iostream>
#include <string>

std::string normalized(const std::string& input) {
    std::string result;
    for (char ch : input) {
        unsigned char uch = static_cast<unsigned char>(ch);
        if (std::isalpha(uch)) {
            result += static_cast<char>(std::tolower(uch));
        }
    }
    return result;
}

bool isPalindrome(const std::string& text) {
    int left = 0;
    int right = static_cast<int>(text.size()) - 1;

    while (left < right) {
        if (text[left] != text[right]) {
            return false;
        }
        ++left;
        --right;
    }
    return true;
}

int main() {
    std::string line;
    std::cout << "Text: ";
    std::getline(std::cin, line);

    std::string clean = normalized(line);
    std::cout << (isPalindrome(clean) ? "palindrome\n" : "not palindrome\n");
}
```

## Common pitfalls

- Allocating a C-string buffer with no room for `'\0'`.
- Destroying the null terminator while editing characters in a C-string.
- Using `=` to assign a C-string after declaration.
- Using `==` to test whether C-strings contain the same text.
- Calling `strcat` or `strcpy` without checking destination capacity.
- Forgetting that `std::cin.get(ch)` reads whitespace, including `'\n'`.
- Mixing `operator>>` and `getline` without handling the leftover newline.
- Passing a negative `char` value directly to `std::toupper`, `std::tolower`, or `std::isalpha`; cast to `unsigned char` first in portable code.

String-handling checks:

- Decide whether the data is text or a character buffer. If it is ordinary text in C++, prefer `std::string`; use C-strings mainly when interacting with older interfaces or studying representation.
- Remember that `std::string::length()` counts characters in the string value, while a C-string function such as `strlen` counts until it finds the first null character.
- Do not write past the end of a C-string array. The array must have room for every visible character plus the null terminator.
- Be careful when mixing `cin >> word` and `getline(cin, line)`. The formatted extraction leaves the newline behind; `getline` will consume it unless the program clears it first.
- Use member functions such as `find`, `substr`, and `replace` rather than manually walking indexes when the operation is naturally a string operation.
- Check the result of `find` against `string::npos`. Treating `npos` as a valid index can lead to very large unsigned values and confusing behavior.
- Avoid unnecessary conversion between `string` and C-string form. Each conversion adds a chance to lose length information or accidentally depend on null termination.

Quick self-test: trace both the logical length and the storage requirement. The string value `"cat"` has length `3`; a C-string array storing it needs `4` characters because of `'\0'`. This difference explains many one-character buffer overruns.

When searching inside a `std::string`, handle the "not found" case before using the position. A position returned by `find` is an unsigned size value; `string::npos` is not `-1` in the ordinary signed-integer sense, even though it is often described that way informally.

For parsing, decide whether whitespace is meaningful. If spaces are part of the data, use `getline`; if whitespace separates tokens, formatted extraction may be correct.

A final review question is whether the program needs ownership of text or only a temporary view of characters. Introductory C++ usually uses owning `std::string` values, which copy safely and manage memory automatically; raw character arrays require the programmer to manage both storage and termination.

## Connections

- [arrays](/cs/programming/cpp/arrays)
- [streams and file I/O](/cs/programming/cpp/streams-and-file-io)
- [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory)
- [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)
- [STL containers](/cs/programming/cpp/stl-containers)
