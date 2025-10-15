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

**Table of operators' precedence**

| Precedence Group | Operator | Description | Associativity |
| :---: | :--- | :--- | :---: |
| 1 (Highest) | () [] . -> | Parentheses, Array Subscript, Member Access (Direct/Pointer) | Left-to-Right |
| 2 | ! ~ ++ -- + - (Unary) * (Dereference) & (Address of) sizeof (type) (Cast) | Unary Operators, Type Cast, sizeof | Right-to-Left |
| 3 | * / % | Multiplication, Division, Modulo (Arithmetic) | Left-to-Right |
| 4 | + - (Binary) | Addition, Subtraction (Arithmetic) | Left-to-Right |
| 5 | << >> | Bitwise Shift (Left/Right) | Left-to-Right |
| 6 | < <= > >= | Relational (Inequality) Operators | Left-to-Right |
| 7 | == != | Relational (Equality) Operators | Left-to-Right |
| 8 | & | Bitwise AND | Left-to-Right |
| 9 | ^ | Bitwise XOR | Left-to-Right |
| 10 | | | Bitwise OR | Left-to-Right |
| 11 | && | Logical AND | Left-to-Right |
| 12 | || | Logical OR | Left-to-Right |
| 13 | ?: | Conditional Operator (Ternary) | Right-to-Left |
| 14 | = += -= *= /= %= <<= >>= &= ^= |= | Assignment Operators (Simple and Compound) | Right-to-Left |
| 15 (Lowest) | , | Comma Operator | Left-to-Right |

# Lecture 3

## The *switch* statement

**Independent Case**

```C
switch ( ch ) {
  case 'Y': /* ch == 'Y' */
    /* do something */
    break ;
  case 'N' : /* ch == 'N' */
    /* do something else */
    break ;
  default : /* otherwise */
    /* do a third thing */
    break ;
}
```

**Falls Through Case**

When match found, starts executing inner code until `break;` reached. Execution "falls through" if `break;` not included.

```C
switch ( ch ) {
  case 'Y':
    /* do something if ch == 'Y' */
  case 'N' :
    /* do something if ch == 'Y' or ch == 'N' */
    break ;
}
```

## The do-while loop

Differs from `while` loop – condition evaluated after each iteration.

```C
char c;
do{
  /* loop body */
  /* some processing */
} while (c == 'y'/* condition */); //<--the end semicolon is essential 
```

## The *extern* keyword

The `extern` keyword informs compiler that variable defined somewhere else enables access/modifying of global variable from other source files.

The `extern` is writed in a header file.

```C
// function.h
extern int global_var;
void some_fn(void);
```

The global variable is actually define in corresponding source file of the header file.

```C
// function.c
int global_var = 1;
void some_fn(void){
  ++global_var;
}
```

The global variable can be modify or access in other source file that include the header file.

```C
// main.c
#include "function.h"
#include <stdio.h>

int main(){
  puts(global_var); // output>> 1
  some_fn();
  puts(global_var); // output>> 2
  global_var += 3;
  puts(global_var); // output>> 5
  return 0;
}
```

When compiler compile `main.c`, it needs a external reference of `global_var`.
Linker will let all references of `global_var` in `main.o` (comes from `main.c`) point to the only memory address which is distributed by `function.o` (comes from `function.c`).

## Compile with modules

If there are multiple modules is included, the source files need to be complie, too.
The following command is used to compile multiple source files:

```bash
gcc -g -O0 -Wall main.c <source-1>.c <source-2>.c -o output.o
```

## The *static* keyword

`static` keyword has two meanings, depending on where the static variable is declared:
  - Outside a function: `static` variables or functions can only be visible within that file, not globally (cannot be `extern`'ed).
  - Inside a function: The `static` variables are still local to the function. However, they are initialized only during program initialization.

```C
// function.c
void some_fn(void){
  static int var = 10;
  ++var;
}
```

The expression `static int var = 10;` may only be declared once when the program starts. After program initialization, the expression will `static int var = 10;` be ignored.

## The *register* keyword

Register is a kind of storage unit inside the CPU. The capacity of register is much smaller than RAM. Instead, it is extremely fast. When CPU execute some computation, data moves from RAM to register.

The C keyword `register` is used to optimize the performance of the program. However, there are some constraints:
  - The variable must be a simple type.
  - Only local variables and function arguments are eligible to use `register`.
  - `register` is a suggestion, not a requirement. Too many `register` declarations may be ignored, compiled as regular variables.
  - Registers do not reside in addressed memory. Pointer of a register is illegal.

# Lecture 4