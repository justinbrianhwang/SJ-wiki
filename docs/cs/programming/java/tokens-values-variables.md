---
title: Tokens, Values, and Variables
sidebar_position: 3
---

# Tokens, Values, and Variables

Java's type system operates only after the source text has been divided into tokens and parsed. That ordering explains several errors that otherwise look arbitrary: a misplaced underscore can make a numeric literal illegal, a keyword cannot be rescued by its apparent context, and a local variable may have the right type yet still be rejected because one control-flow path leaves it unassigned.

Variables then connect the program's names to run-time values. A primitive variable contains a primitive value. A reference variable contains either `null` or a reference to an object or array. Java uses value semantics for assignment and argument passing in both cases; the value being copied may itself be an object reference.

## From characters to tokens

The compiler first performs lexical translation. Unicode escapes are processed very early, before comments and ordinary tokens are recognized. As a result, a Unicode escape can introduce a line terminator or comment delimiter. Using escapes to disguise source structure is legal only in limited forms and is hostile to review; reserve them for cases where they are genuinely needed in literals or identifiers.

After line terminators and input characters are established, the lexical grammar recognizes whitespace, comments, identifiers, keywords, literals, separators, and operators. Whitespace and comments separate tokens but otherwise do not participate in the parsed program.

```java
total += 12;
```

This short statement contains an identifier `total`, the compound-assignment operator `+=`, the integer literal `12`, and the separator `;`. The scanner generally takes the longest valid token. Thus `>>=` is one operator when that token is valid; it is not automatically three greater-than or assignment tokens merely because those characters could be read separately.

Comments come in three familiar forms:

```java
// continues to the line terminator

/* may span lines */

/** documentation comment processed by documentation tools */
```

Block comments do not nest. In `/* outer /* inner */ remainder */`, the first closing delimiter ends the comment, leaving `remainder */` to be tokenized as source and usually causing syntax errors.

## Names, keywords, and context

An **identifier** names a variable, method, type, package component, label, or another declared entity. Identifiers are case-sensitive: `count`, `Count`, and `COUNT` are distinct. Java permits many Unicode letters and a wider set of identifier characters after the first character. That supports natural-language names, but visually similar characters from different scripts can be difficult to distinguish during review.

Reserved keywords such as `class`, `if`, and `return` cannot be identifiers. The single underscore has been a keyword since Java 9 and cannot be used as a name. Java also has contextual keywords whose special meaning is limited to particular grammatical positions. Their treatment is determined by the language grammar, not by a convention that a programmer can override.

The spelling of a name does not by itself identify its declaration. Resolution uses its position, enclosing scopes, imports, inheritance, and member-access syntax. Local declarations may shadow fields:

```java
final class Meter {
    private int value;

    void setValue(int value) {
        this.value = value;
    }
}
```

Inside `setValue`, bare `value` refers to the parameter. `this.value` selects the field of the current object. The code is conventional because the qualification states the intended target. Less deliberate shadowing, especially between nested local scopes, makes traces needlessly hard.

Scope is a source-level property: it determines where a declaration's name may be used. Lifetime is a run-time property: it concerns how long a variable or object exists. Reachability is another run-time property: it asks whether a live reference chain can still reach an object. A local name can leave scope while its former object remains reachable through a field, collection, or returned reference.

## Literal notation carries type information

A **literal** is source notation for a value. Java has integer, floating-point, boolean, character, string, and null literals. The spelling affects the type available to later phases of compilation.

| Source form | Usual type or role | Detail that often matters |
|---|---|---|
| `42` | `int` | Must be representable according to integer-literal rules |
| `42L` | `long` | `L` is easier to distinguish from `1` than lowercase `l` |
| `3.5` | `double` | Decimal floating literals default to `double` |
| `3.5F` | `float` | Suffix requests `float` |
| `'A'` | `char` | Exactly one UTF-16 code unit after escape processing |
| `"A"` | `String` | A reference to a string object |
| `true`, `false` | `boolean` | Not interchangeable with numeric zero or one |
| `null` | null literal | Convertible to reference types, never to a primitive type |

Integer literals may be decimal, hexadecimal, octal, or binary. Prefixes state the radix: `0x2A`, `052`, and `0b101010` all denote forty-two, though leading-zero octal is easy to overlook. Underscores can group digits:

```java
int mask = 0b1111_0000;
long population = 8_000_000_000L;
double avogadro = 6.022_140_76e23;
```

An underscore must occur between digits in the permitted part of the literal. It cannot sit immediately after a radix prefix, adjacent to a decimal point, or at the end. `0x_FF`, `1_.0`, and `100_` are invalid.

Literal typing affects overload selection and assignment. Given methods `f(int)` and `f(long)`, `f(1)` chooses the `int` overload while `f(1L)` chooses `long`. The assignment `float x = 1.0;` fails because `1.0` is a `double`; `float x = 1.0F;` supplies the intended type. Constant-expression narrowing permits a few otherwise surprising assignments, such as `byte b = 100`, because the compile-time constant fits in `byte`. Replacing `100` with a nonconstant `int` variable removes that special permission.

A `char` stores one 16-bit UTF-16 code unit, not an arbitrary Unicode character. Some characters require a surrogate pair and therefore cannot fit in one `char`. A `String` can contain that pair, and code-point APIs are needed when processing Unicode characters rather than code units.

## What each variable declaration establishes

A declaration introduces a variable with a compile-time type. That type restricts assignments, determines which members may be selected through the expression, and influences overload resolution. The variable's location determines how it is initialized.

| Variable kind | Declared in | Initial value rule |
|---|---|---|
| Local variable | Block, method, constructor, or initializer | Must be definitely assigned before each read |
| Parameter | Method, constructor, lambda, or exception handler | Receives a value when execution enters |
| Instance field | Class body without `static` | Gets the type's default value for each new object |
| Static field | Class body with `static` | Gets the type's default during class initialization |
| Array component | Array object | Gets the component type's default when the array is created |

Numeric fields and array components default to zero, `boolean` defaults to `false`, `char` defaults to the zero code unit, and references default to `null`. Default initialization prevents an undefined machine value from leaking into Java code. It does not establish a useful domain invariant. An order whose `quantity` remains zero or whose `customer` remains null may still be invalid even though every field has a defined JVM value.

Local variables deliberately have no readable default. The compiler performs **definite-assignment analysis** over control flow. Every path that reaches a read must have assigned the local.

```java
int fee;
if (isMember) {
    fee = 5;
}
System.out.println(fee); // compile-time error
```

Trace the paths separately:

1. If `isMember` is true, execution assigns `5`, then reaches `println`.
2. If it is false, execution skips the assignment and reaches the same read.
3. Because the second path has no assignment, the read is rejected.

Adding an `else` repairs the missing path:

```java
int fee;
if (isMember) {
    fee = 5;
} else {
    fee = 8;
}
System.out.println(fee);
```

An early `return` or `throw` on the unassigned path also satisfies the analysis because that path can no longer reach the read. Definite assignment is conservative and compile-time only; it does not execute conditions or infer every truth a human might prove from complex application logic.

## `var` infers a type, not a dynamic variable

For an initialized local variable, `var` asks the compiler to infer the static type from the initializer:

```java
var names = new ArrayList<String>(); // inferred as ArrayList<String>
var limit = 10;                      // inferred as int
```

The type does not change later. `limit = "ten"` remains a compile-time error. `var` cannot be used for an uninitialized local, a field, a method parameter, or a return type. It also cannot infer a useful type from the null literal alone:

```java
var missing = null; // compile-time error
```

Inference preserves the initializer's exact compile-time type, which can be narrower than the abstraction intended by the surrounding code. `List<String> names = new ArrayList<>();` exposes only the `List` contract, whereas `var names = new ArrayList<String>();` gives the local the concrete `ArrayList` type. Either can be correct; the declaration communicates a different dependency.

## Worked reference trace: copying a value can create aliasing

Java always passes and assigns values by value. For reference types, the copied value is a reference. Consider:

```java
int a = 3;
int b = a;

int[] x = new int[] { 3 };
int[] y = x;

b = 4;
y[0] = 9;
y = new int[] { 12 };
```

Track variables separately from heap objects:

1. `a` contains the primitive value `3`.
2. `b = a` copies `3` into `b`. The two primitive variables are independent.
3. Array creation allocates array object A with component `3`; `x` receives a reference to A.
4. `y = x` copies the reference. Both variables now refer to A.
5. `b = 4` replaces only the value in `b`; `a` remains `3`.
6. `y[0] = 9` mutates object A. Reading `x[0]` also yields `9` because `x` reaches A.
7. The final assignment creates array object B and changes `y` to refer to B. It does not move or copy A.

The final state is `a == 3`, `b == 4`, `x[0] == 9`, and `y[0] == 12`. There is no pass-by-reference mode in which a method can replace the caller's variable. A method can mutate an object through its copied reference, but assigning a new object to the parameter changes only the parameter.

```java
static void replace(int[] values) {
    values[0] = 7;             // caller observes mutation of shared array
    values = new int[] { 99 }; // caller does not observe parameter reassignment
}
```

## `final` freezes an assignment, not an object

A final variable may be assigned once. A blank final field can be assigned by a constructor, and the compiler checks that construction paths assign it correctly. For a primitive, final prevents replacement of the primitive value. For a reference, it prevents the variable from referring to a different object; it does not make the object immutable.

```java
final List<String> names = new ArrayList<>();
names.add("Ada");                 // allowed: object mutation
// names = new ArrayList<>();     // error: reference reassignment
```

Constants are commonly declared `static final`, but not every `static final` field is a compile-time constant. The initializer and type must satisfy the language's constant-variable rules. That distinction affects `switch` labels, annotation values, and whether a client may inline a value during compilation.

## Declared type and run-time class answer different questions

A reference variable's declared type controls which members the compiler permits through that expression. The object may belong to a more specific run-time class:

```java
List<String> names = new ArrayList<>();
names.add("Ada");
```

The variable `names` has declared type `List<String>`, while the created object is an `ArrayList`. Assignment copies the reference without changing the object. The interface type intentionally hides operations found only on the concrete class and lets a later implementation change without rewriting callers.

A cast does not convert the object into another class. It asks the compiler and run time to treat the same reference as a target type, failing with `ClassCastException` when the object is incompatible. `instanceof` can test compatibility, and pattern matching for `instanceof` can introduce a narrowed local only on the successful path.

Two reference variables can therefore have different declared types and still designate one object. Mutations through either alias affect that shared object, subject to the members exposed by each declared type. Reference equality with `==` asks whether references designate the same object or are both null; `equals` asks for the class-defined notion of value equality.

## Null and the boundary between value and object

`null` denotes the absence of an object reference. It is not an object with methods or fields, and it is not the same value as zero, `false`, an empty string, or an empty collection. Dereferencing it through field access, array access, unboxing, or an instance-method call throws `NullPointerException`.

Unboxing hides a common null edge:

```java
Integer boxed = null;
int value = boxed; // NullPointerException during unboxing
```

A null check establishes only that a reference is present. It says nothing about the referred object's internal validity. APIs often avoid ambiguous null meanings by using an empty collection, a domain-specific result, or `Optional` where absence is part of the return contract.

## Notes for tracing declarations

- Identify the exact declaration a name resolves to before reasoning about its value.
- Record declared type and current value separately. A variable of interface type may refer to an object of a more specific run-time class.
- Draw reference variables as arrows to objects. Do not draw an object inside each variable box after a reference assignment.
- Check all incoming control-flow paths for local initialization.
- Treat literal suffixes, radix prefixes, and casts as part of type reasoning, not cosmetic notation.
- Keep scopes narrow enough that a reader can see every use without searching an entire method.

<div className="see-also">

See also: [Primitives, Operators, and Conversions](/cs/programming/java/primitives-operators-conversions) · [Control Flow, Arrays, and Strings](/cs/programming/java/control-flow-arrays-strings) · [Classes, Objects, and Encapsulation](/cs/programming/java/classes-objects-encapsulation) · [Garbage Collection, References, and Memory](/cs/programming/java/garbage-collection-references-memory)

</div>
