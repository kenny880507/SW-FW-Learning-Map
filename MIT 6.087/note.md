# Lecture 1

## Evironment

Platform: Windows Subsystem for Linux
OS: Ubuntu 22.04.5 LTS
Complier: gcc (version 11.4.0)
Debugger: GNU gdb (version 12.1), valgrind (version 3.18.1)

Platform: Mac
OS: MacOS ???
Complier: gcc (version 15.2.0)
Debugger: gdb (version ???)

## Comiple

The standard compile command for WSL is below:

```bash
gcc -g -O0 -Wall <source>.c -o <executable-file>.o
```

The standard compile command for WSL is below:

```bash
gcc-15 -g -O0 -Wall <source>.c -o
 <executable-file>.o
```

Where the arguments have some denotation:

- `-g`: Embed debugging information in executable file. Debugger cann't work without this argument.
- `-O0`: Disable optimization.
- `-Wall`: Enables most compiler warnings.
- `-o`: Declare executable file name.

`<source>.c` is the source code. `<executable-file>.o` is the executable file. Although `.o` file is object file in general, it is defined as executable file in this course.

## Debug

To open executable file with debugger, use command below:

```bash
gdb <executable-file>.o
```

For memory debbuging, use valgrind:

```bash
valgrind <executable-file>.o
```

Here are some useful commands for the GDB console:

- `break <line-number>`: Create breakpoint at specified line.
- `break <file>:<line-number>`: Create breakpoint at line in file.
- `run`: Run program.
- `c`: Continue execution.
- `next`: Execute next line.
- `step`: Execute next line or step into function.
- `quit`: Quit gdb.
- `print <expression>`: Print current value of the specified expression.
- `help <command>`: In-program help.

## Macro

`#` is the notation in front of macro. Macro is used to create symbolic constants or inline code snippets that improve readability and reduce repetition. They are processed by the preprocessor before compilation.

The following table shows several commonly used macro:

| Macro | Syntax | Description | Remarks |
| :--- | :--- | :--- | :--- |
| `#include` | `#include <stdio.h>` or `#include "file.h"` | Reads the contents of a header file and inserts them into the current source file. | Angle brackets (<>) are for standard library headers; double quotes ("") check the current directory first. |
| `#define` | `#define msg "text"` or `#define add3(x,y,z) ((x)+(y)+(z))` | Defines a macro for text substitution. Can define constants or function-like expression macros. | Arguments in expression macros should be protected by parentheses to ensure order of operations. It performs inline replacement and is not suitable for recursion. |
| `#undef` | `#undef msg` | Removes the definition of a macro at compile time. | Used to restrict a macro's scope or to safely redefine a macro. |
| `#pragma` | `#pragma directive` | A preprocessor directive used to pass specific instructions to the compiler. | Often used to control compiler behavior (e.g., optimization or warnings). |
| `#error` | `#error <message>` | Triggers a custom compiler error, forcing compilation to stop. | Used to check if necessary preconditions (like macro definitions) are met before compilation continues. |
| `#warning` | `#warning <message>` | Triggers a custom compiler warning message. | Used to alert the developer to potential issues without halting the compilation process. |
| `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#endif` | `#ifdef MACRO` / `#if CONST_EXPR` / `#endif` | Conditional preprocessor macros used to control which lines of code are compiled. | Conditions must be preprocessor defines or literals (integer constant expressions), evaluated before the code is compiled. Often used in header files to prevent multiple inclusion. |

# Lecture 2

Key point:
- C is a weakly typed language. It allows implicit conversion and forced casting for datatypes.
- Operators specify how an object can be manipulated (e.g., numeric vs. string operations).
- `Big endian`: the most significant bits (MSBs) occupy the lower address. This representation is used in the powerpc processor. Networks generally use big-endian order, and thus it is called network order.
- `Little endian`: the least signficant bits (LSBs) occupy the lower address. This representation is used on all x86 compatible processors.
- Expression of constants:
  - Integer:
    - `int i = 3;`: `3` is an int by default.
    - `long i = 3;`: `3` is an int by default and is implicitly converted to long.
    - `unsigned long i = 3UL`: The postfix `UL` instructs the compiler to treat `3` as unsigned long.
    - `int i = 0xA`: The prefix `0x` indicates that contant `A` is a hexadecimal number.
    - `int i = 012`: The prefix `0` indicates that contant `12` is a octal number.
  - Floating Point:
    - `float pi = 3.14`: `3.14` is an float by default.
    - `float pi = 3.14f`: The prefix `f` indicates that contant `3.14` is float type.
    - `double pi = 3.14l`: The prefix `l` indicates that contant `3.14` is double type.
  - Character:
    - `'A'`: Character.
    - `'\x41'`: Character specified in hex.
    - `'0101'`: Character specified in octal.
  - String:
    - `"ab"`: String literal.
    - `"a""b"`: Same as `"ab"`.
  - Enumeration:
    - `enum BOLL{NO,YES}`: NO=0, YES=1.
    - `enum COLOR{R=1,G,B,Y=10}`: R=1, G=2, B=3, Y=10.

# Lecture 3

