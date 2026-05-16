---
title: References and Operator Overloading
sidebar_position: 7
---

# References and Operator Overloading

References and operator overloading make user-defined types feel like built-in types when used carefully. A reference gives another name for an existing object. Operator overloading lets a class define meanings for operators such as `+`, `==`, `<<`, `>>`, `[]`, and assignment. Savitch groups these ideas with friend functions because many useful operator overloads must either access private data or support conversions on both operands.

The goal is not to overload every possible operator. The goal is to make class objects obey the same mental model users already have for numbers, strings, streams, and arrays. A good overloaded operator is unsurprising, efficient enough, and consistent with the rest of the class interface.

## Definitions

A **reference** is an alias for an existing object.

```cpp
int value = 10;
int& alias = value;
alias = 20; // value is now 20
```

References must be initialized when declared and normally cannot be reseated to refer to another object.

A **const reference** can bind to an object for read-only access.

```cpp
void printMoney(const Money& amount);
```

An **overloaded operator** is a function whose name is `operator` followed by an operator symbol.

```cpp
Money operator+(const Money& left, const Money& right);
bool operator==(const Money& left, const Money& right);
```

An operator can be overloaded as a nonmember function, member function, or friend function. At least one operand must be a class or enumeration type. You cannot redefine built-in behavior for two plain `int` operands.

A **member operator** uses the left operand as the calling object.

```cpp
class Counter {
public:
    Counter operator+(const Counter& rhs) const;
};
```

A **friend function** is not a member, but it has access to private members because the class grants access.

```cpp
class Money {
    friend Money operator+(const Money& left, const Money& right);
private:
    int cents_;
};
```

Stream operators normally return the stream by reference so chaining works:

```cpp
std::ostream& operator<<(std::ostream& out, const Money& amount);
std::istream& operator>>(std::istream& in, Money& amount);
```

## Key results

Operator overloading is function overloading with operator syntax. The expression:

```cpp
sum = a + b;
```

can call:

```cpp
Money operator+(const Money& a, const Money& b);
```

For symmetric binary operators, nonmember functions are often better than members because automatic conversion can apply to both operands. If `Money` has a constructor from `int`, this works with a nonmember `operator+`:

```cpp
Money total = 25 + baseAmount;
```

If `operator+` is only a member of `Money`, then the left operand must already be a `Money` object, so `25 + baseAmount` will not match.

Use member operators when the operation must modify or select from the calling object, such as assignment, subscript, function call, or compound assignment:

```cpp
class Scores {
public:
    int& operator[](int index);
    const int& operator[](int index) const;
};
```

Assignment operators return `*this` by reference:

```cpp
T& T::operator=(const T& rhs);
```

This supports chaining such as `a = b = c`.

Avoid overloading operators whose built-in evaluation rules are too special. Savitch warns especially about `&&`, `||`, and comma because overloaded versions do not preserve the short-circuit or sequencing behavior programmers expect.

## Visual

| Operator | Usually member? | Usually nonmember/friend? | Reason |
|---|---:|---:|---|
| `=` | yes | no | must modify left object |
| `[]` | yes | no | left operand is container object |
| `()` | yes | no | object behaves like function |
| `+=` | yes | sometimes | modifies left object |
| `+` | sometimes | yes | symmetric value operation |
| `==` | sometimes | yes | symmetric comparison |
| `<<` | no | yes | left operand is stream |
| `>>` | no | yes | left operand is stream |

```mermaid
flowchart LR
  A[Expression a + b] --> B{"operator+ member?"}
  B -->|yes| C["a.operator+(b)"]
  B -->|no| D["operator+("#quot;#quot;a, b#quot;#quot;")"]
  D --> E{"friend?"}
  E -->|yes| F[Can read private members]
  E -->|no| G[Use public accessors]
```

## Worked example 1: adding money using cents

Problem: Represent money as total cents and overload `+` and `<<`.

Method:

1. Store one integer invariant: total cents.
2. To add two money objects, add their cents.

   $$\mathrm{sumCents} = \mathrm{leftCents} + \mathrm{rightCents}$$

3. Return a new `Money` object.
4. Print dollars as `cents / 100`.
5. Print cents as `abs(cents % 100)` with leading zero if needed.

```cpp
#include <cstdlib>
#include <iomanip>
#include <iostream>

class Money {
public:
    explicit Money(int cents = 0) : cents_(cents) {}

    int cents() const {
        return cents_;
    }

    friend Money operator+(const Money& left, const Money& right) {
        return Money(left.cents_ + right.cents_);
    }

    friend std::ostream& operator<<(std::ostream& out, const Money& amount) {
        int cents = amount.cents_;
        if (cents < 0) {
            out << "-";
            cents = -cents;
        }
        out << "$" << cents / 100 << "."
            << std::setw(2) << std::setfill('0') << cents % 100;
        return out;
    }

private:
    int cents_;
};

int main() {
    Money coffee(375);
    Money sandwich(825);
    std::cout << coffee + sandwich << '\n';
}
```

Checked answer:

1. `coffee` stores `375`.
2. `sandwich` stores `825`.
3. Sum is `1200`.
4. `1200 / 100 == 12`, `1200 % 100 == 0`.
5. Output is `\$12.00`.

## Worked example 2: prefix and postfix increment

Problem: Define a counter that supports both `++c` and `c++`.

Method:

1. Prefix increment changes the object and returns the changed object by reference.
2. Postfix increment must return the old value.
3. C++ distinguishes postfix by a dummy `int` parameter.

```cpp
#include <iostream>

class Counter {
public:
    explicit Counter(int value = 0) : value_(value) {}

    Counter& operator++() {
        ++value_;
        return *this;
    }

    Counter operator++(int) {
        Counter old(*this);
        ++value_;
        return old;
    }

    int value() const {
        return value_;
    }

private:
    int value_;
};

int main() {
    Counter c(5);
    Counter before = c++;
    Counter after = ++c;

    std::cout << before.value() << " "
              << c.value() << " "
              << after.value() << '\n';
}
```

Step-by-step:

1. Start with `c == 5`.
2. `before = c++` stores old value `5`, then changes `c` to `6`.
3. `after = ++c` first changes `c` to `7`, then stores `7`.
4. Final output is `5 7 7`.

Checked answer: the postfix result preserves the pre-increment value, while prefix returns the updated value.

## Code

This class demonstrates `operator[]` with const and non-const overloads.

```cpp
#include <iostream>
#include <stdexcept>

class FixedTriple {
public:
    FixedTriple(int a, int b, int c) : data_{a, b, c} {}

    int& operator[](int index) {
        check(index);
        return data_[index];
    }

    const int& operator[](int index) const {
        check(index);
        return data_[index];
    }

private:
    void check(int index) const {
        if (index < 0 || index >= 3) {
            throw std::out_of_range("FixedTriple index");
        }
    }

    int data_[3];
};

int main() {
    FixedTriple values(10, 20, 30);
    values[1] = 99;

    const FixedTriple& view = values;
    std::cout << view[0] << " " << view[1] << " " << view[2] << '\n';
}
```

## Common pitfalls

- Returning references to local temporaries from overloaded operators.
- Making `operator+` modify the left operand. That surprises users; use `operator+=` for mutation.
- Forgetting to return `std::ostream&` or `std::istream&` from stream operators.
- Overloading `&&`, `||`, or comma and expecting built-in short-circuit or sequencing behavior.
- Implementing postfix `++` as if it were prefix `++`.
- Making every operator a friend when public accessors or member functions would suffice.
- Returning non-const references from const objects.
- Ignoring self-assignment in `operator=`.

Operator-design checks:

- Overload an operator only when the meaning is natural for the type. `+` for rational numbers is clear; `+` for opening a file or printing a report is surprising.
- Preserve expected algebraic behavior when possible. If `a + b` creates a new value, it should not mutate `a`; if `a += b` mutates `a`, it should return `*this` by reference.
- Use nonmember functions for symmetric binary operators when the left operand may need conversion. This is one reason `operator+` is often implemented in terms of `operator+=`.
- Use references to avoid unnecessary copies, but never return a reference to a local variable. Returning by value is correct for most arithmetic-like operators.
- Keep stream operators conventional: `operator<<` should return `ostream&`, and `operator>>` should return `istream&`, so chained operations keep working.
- Do not overload operators merely to make code shorter. The result should be more readable to someone who knows the mathematical or domain meaning.
- Remember that some operators cannot be overloaded and that overloading does not change precedence. A custom `operator*` still has multiplication precedence even if the operation is not numeric multiplication.

Quick self-test: compare the overloaded operator with the built-in operator it resembles. If `a + b + c` should work, `operator+` must return a value that can participate in another `+`. If `cout << x << y` should work, `operator<<` must return the same stream. Chaining behavior is often the easiest way to detect a wrong return type.

For reference parameters, ask whether `const` would still allow the function to do its job. If yes, use `const`. This one decision prevents many accidental mutations and lets the function accept temporaries, const objects, and ordinary variables with the same interface.

A final review question is whether the overloaded operator would surprise a reader in an expression. Operator syntax removes the function name, so the symbol itself must carry the meaning. If a named member function would be clearer, use the named function.

Extended practice: write both a named function and an operator for a small numeric class, then compare the client code. `add(a, b)` is explicit, while `a + b` is compact and conventional. Keep the operator only when the compact expression is still easier to read.

## Connections

- [functions and parameters](/cs/programming/cpp/functions-parameters-and-scope)
- [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)
- [constructors and copy semantics](/cs/programming/cpp/constructors-and-copy-semantics)
- [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory)
- [STL algorithms and iterators](/cs/programming/cpp/stl-algorithms-and-iterators)
