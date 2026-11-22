---
title: Strings
sidebar_position: 5
---

# Strings

C++ has two major string traditions. The older C-style representation stores text in an array of `char` terminated by the null character `'\0'`. The modern standard-library representation uses the class `std::string`, which manages storage and exposes string operations through member functions and overloaded operators. Savitch covers both because C-strings still appear in string literals, command-line arguments, old libraries, and low-level character processing.

The default choice is simple: use `std::string` for ordinary application code, but understand C-strings well enough to read, interoperate with, and safely maintain code that uses them.

## Two representations with different invariants

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

A `std::string` stores its current size along with managed contiguous character storage. Since C++11, `&text[0]` for a nonempty string and `text.data()` expose contiguous elements suitable for APIs that accept a character range. `c_str()` supplies a null-terminated view for C interfaces. Pointers obtained from these functions are non-owning and may be invalidated when the string changes.

Unlike a C-string, an `std::string` can contain embedded null characters because its size is stored separately. Constructing from a C-string still stops at the first null unless an explicit length is supplied. Printing with stream insertion uses the string's length and can preserve embedded null bytes, though those bytes have no ordinary visible glyph.

## Length, capacity, and comparison

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

$$
\text{valid C-string} \Rightarrow \exists i \text{ such that } a[i] = '\backslash 0'
$$

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

`size()` counts `char` elements, which are bytes on ordinary implementations, not necessarily user-perceived characters. UTF-8 encodes many characters with multiple bytes, and a visible grapheme can contain several Unicode code points. Indexing a UTF-8 `std::string` therefore selects a code unit byte, not reliably a complete character. Unicode-aware segmentation and case conversion require a library or platform facility with an explicit encoding policy.

Like vector, string distinguishes size from capacity. Appending within available capacity can reuse storage; growth beyond it may allocate a new buffer and invalidate pointers, references, and iterators. `reserve` can reduce repeated allocations when the approximate final length is known. It does not change the logical size, and code must not write into merely reserved-but-not-sized elements.

Lexicographic comparison examines corresponding character values until a difference appears, then uses length if one string is a prefix of the other. That is a code-unit ordering, not locale-aware dictionary order. Uppercase, lowercase, accents, and numeric substrings may sort differently from human expectations.

## Where the terminator lives

```text
C-string storage for "cat" in char word[6]

index:    0     1     2     3      4      5
       +-----+-----+-----+------+------+------+
value: | 'c' | 'a' | 't' | '\0' |  ??  |  ??  |
       +-----+-----+-----+------+------+------+
                         terminator
```

| Operation | C-string style | `std::string` style | Main risk |
|---|---|---|---|
| assignment | `strcpy(dest, src)` | `dest = src` | C buffer overflow |
| equality | `strcmp(a, b) == 0` | `a == b` | C `==` compares addresses |
| length | `strlen(s)` | `s.size()` | C requires terminator |
| concatenate | `strcat(dest, src)` | `dest += src` | C destination capacity |
| line input | `cin.getline(buf, n)` | `getline(cin, s)` | leftover newline |

The unused C-array slots have no role in the string value. Library functions are allowed to read only through the terminator; they do not know the array's capacity. By contrast, `std::string` member functions know both size and allocation details and can grow the object when needed.

## Worked example: why C-string equality needs `strcmp`

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

`strcmp` returns a negative, zero, or positive integer; the magnitude is unspecified. Code should compare the result with zero rather than expect `-1` or `1`. The comparison also ends at the first null, so it cannot compare arbitrary byte buffers containing embedded zeros without a separate length.

## Worked example: fixing `cin >>` followed by `getline`

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

The extraction should also be tested. If the age is nonnumeric, the stream remains failed and `ignore` alone cannot recover; call `clear()` before discarding the malformed line, or report the error and stop. Input recovery is a stream-state problem as well as a string problem.

## Normalizing ASCII-like text for a palindrome test

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
    std::size_t left = 0;
    std::size_t right = text.size();

    while (left < right) {
        --right;
        if (text[left] != text[right]) {
            return false;
        }
        ++left;
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

Using a half-open interval `[left, right)` avoids subtracting one from zero for an empty string and avoids narrowing a potentially large `size_t` into `int`. Each iteration changes the interval only after establishing that it is nonempty. For odd lengths, the two positions meet at the middle element, which needs no comparison with itself.

Casting through `unsigned char` before the `<cctype>` calls avoids undefined behavior for negative plain `char` values. Even so, these functions under the default C locale do not provide general Unicode case folding. The normalization is suitable for ASCII-like input under a chosen locale, not for every written language.

## Buffer errors and text-model assumptions

- Allocating a C-string buffer with no room for `'\0'`.
- Destroying the null terminator while editing characters in a C-string.
- Using `=` to assign a C-string after declaration.
- Using `==` to test whether C-strings contain the same text.
- Calling `strcat` or `strcpy` without checking destination capacity.
- Forgetting that `std::cin.get(ch)` reads whitespace, including `'\n'`.
- Mixing `operator>>` and `getline` without handling the leftover newline.
- Passing a negative `char` value directly to `std::toupper`, `std::tolower`, or `std::isalpha`; cast to `unsigned char` first in portable code.

For text-handling code:

- Decide whether the data is text or a character buffer. If it is ordinary text in C++, prefer `std::string`; use C-strings mainly when interacting with older interfaces or studying representation.
- Remember that `std::string::length()` counts characters in the string value, while a C-string function such as `strlen` counts until it finds the first null character.
- Do not write past the end of a C-string array. The array must have room for every visible character plus the null terminator.
- Be careful when mixing `cin >> word` and `getline(cin, line)`. The formatted extraction leaves the newline behind; `getline` will consume it unless the program clears it first.
- Use member functions such as `find`, `substr`, and `replace` rather than manually walking indexes when the operation is naturally a string operation.
- Check the result of `find` against `string::npos`. Treating `npos` as a valid index can lead to very large unsigned values and confusing behavior.
- Avoid unnecessary conversion between `string` and C-string form. Each conversion adds a chance to lose length information or accidentally depend on null termination.

Trace both the logical length and the storage requirement. The string value `"cat"` has length `3`; a C-string array storing it needs `4` characters because of `'\0'`. The difference explains many one-character buffer overruns.

When searching inside a `std::string`, handle the "not found" case before using the position. A position returned by `find` is an unsigned size value; `string::npos` is not `-1` in the ordinary signed-integer sense, even though it is often described that way informally.

For parsing, decide whether whitespace is meaningful. If spaces are part of the data, use `getline`; if whitespace separates tokens, formatted extraction may be correct.

Choose explicitly between ownership of text and a temporary view of characters. Introductory C++ usually uses owning `std::string` values, which copy safely and manage memory automatically; raw character arrays require the programmer to manage both storage and termination.

`std::string_view` can express a non-owning contiguous character sequence without copying. It may refer to a string, literal, or substring and stores a length, so it need not be null-terminated. Its small size makes it useful for read-only parameters, but it can dangle when the source string is destroyed or reallocated. Returning a view into a local string is invalid for the same lifetime reason as returning a pointer to a local array.

Substring operations deserve a cost check. `substr` creates a new string and copies characters. Repeated concatenation at the front or repeated substring copying can turn a linear-looking parser into quadratic work. Index ranges or string views avoid copies when ownership is not needed; `reserve` helps when constructing one output incrementally.

The bounded-looking `strncpy` has awkward semantics: it pads the destination with zeros when the source is short and does not append a terminator when the source length reaches the bound. Explicitly writing the final null, as the earlier example does, prevents unterminated output but also truncates. Interfaces carrying both pointer and capacity are safer than a bare destination pointer, while `std::string` remains the ordinary default.

Search positions use `std::string::size_type`, commonly the same unsigned type as `std::size_t`. Adding to `npos` wraps, and subtracting positions without first establishing their order can also wrap. Check for failure and validate range endpoints before arithmetic. Member functions such as `erase`, `insert`, and `replace` accept position-and-count forms whose count may be clipped at the end, but an invalid starting position can throw `std::out_of_range`.

Appending one character at a time is amortized linear because string capacity grows geometrically on typical conforming implementations, though the exact growth policy is unspecified. Inserting repeatedly at the beginning remains costly because existing characters move on each operation. When the final pieces are already known, compute or estimate the total length, reserve once, and append in forward order.

Converting numbers with `std::to_string` is convenient for simple output; parsing with `std::stoi` reports errors through exceptions and can return the position where parsing stopped. String streams provide locale-aware formatted parsing, while `std::from_chars` offers a low-level, locale-independent conversion for supported types without allocation. The right tool depends on whether trailing text, locale, and error representation matter.

C-string interfaces often accept a pointer with no capacity because they predate safer range conventions. Before calling one, identify whether the function reads, writes, or may retain the pointer after return. `std::string::c_str()` is suitable for a read-only call that does not retain it. Casting away constness or letting a C function store the pointer invites mutation or lifetime errors.

Case-insensitive comparison is not obtained safely by lowercasing bytes in every language. Even ASCII-oriented code should cast through `unsigned char`; international text additionally needs Unicode normalization and case-folding rules. State the accepted character set when a parser or identifier comparison deliberately uses ASCII rules.

## Related pages

- [arrays](/cs/programming/cpp/arrays)
- [streams and file I/O](/cs/programming/cpp/streams-and-file-io)
- [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory)
- [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)
- [STL containers](/cs/programming/cpp/stl-containers)
