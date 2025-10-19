# Lecture 1

## Evironment

Platform: Windows Subsystem for Linux
OS: Ubuntu 22.04.5 LTS
Complier: gcc (version 11.4.0)
Debugger: GNU gdb (version 12.1), valgrind (version 3.18.1)

Platform: Mac
OS: MacOS 15.6.1
Complier: gcc (version 15.2.0)
Debugger: gdb (version 16.3)

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

The following table campare the bit number and range of different numerical data types:

| Data Type | Total Bits (Bytes) | Sign, Exponent, Mantissa Bits (Floating Point Only) | Approximate Range / Min & Max Values |
| :--- | :--- | :--- | :--- |
| short (signed) | 16 bits (2 Bytes) | N/A | -32,768 ~ +32,767 (Minimum C Standard) |
| unsigned short | 16 bits (2 Bytes) | N/A | 0 ~ 65,535 (Minimum C Standard) |
| int (default signed) | 32 bits (4 Bytes) (Common) | N/A | -2,147,483,648 ~ +2,147,483,647 |
| unsigned int | 32 bits (4 Bytes) (Common) | N/A | 0 ~ 4,294,967,295 |
| long (signed) | 32 or 64 bits (4 or 8 Bytes) | N/A | +/- 2.1e9 (if 32-bit) OR +/- 9.2e18 (if 64-bit) |
| unsigned long | 32 or 64 bits (4 or 8 Bytes) | N/A | 0 ~ 4.2e9 (if 32-bit) OR 1.8e19 (if 64-bit) |
| float | 32 bits (4 Bytes) | Sign: 1, Exponent: 8, Mantissa: 23 | Max: 3.4e+38, Min (non-zero): 1.17e-38 |
| double | 64 bits (8 Bytes) | Sign: 1, Exponent: 11, Mantissa: 52 | Max: 1.8e+308, Min (non-zero): 2.2e-308 |
| char (signed) | 8 bits (1 Byte) (Common) | N/A | -128 ~ +127 (Minimum C Standard) |
| unsigned char | 8 bits (1 Byte) (Common) | N/A | 0 ~ 255 |

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

## goto

`goto` provides a way to unconditionally jump to arbitrary position of code.

```C
for(...){
  for(...){
    /* some expression */
    if(condition) goto error;
  }
}
error:
/* keep going from gere */
```
**notice**: The readability of code decreases when the number of `goto` increases. More `goto` may cause debug harder.

## <stdio.h>

`int putchar(int)`: Puts the character on the standard output. Then, returns the character printed or EOF on error.
`int getchar()`: Returns the next character from standard input. If error occured, returns EOF.

If a executable file `a.out` needs standard input, `<` operator can use a file as standard input.

```bash
./a.out < file.txt
```

`int printf(char format[],arg1,arg2 ,...)` provides a formatted way to print variables. Returns the number of characters printed.

```C
printf("hello world\n");
printf("%d\n",10);
printf("Prices: %d and %d", 10, 20);
```

The `%` symbol can be followed by some components to specify the output format.

```C
%[flag][width][.precision][modifier]<type>
```

**flag:**

| format | output |
|---|---|
| printf ("%d, %+d, %+d",10, -10) | 10, +10, -10 |
| printf ("%04d",10) | 0010 |
| printf ("%7s", "hello") | bbhello |
| printf ("%-7s", "hello") | hellobb |

**width:**

| format | output |
|---|---|
| printf ("%d",10) | "10" |
| printf ("%4d",10) | bb10 (b:space) |
| printf ("%s","hello") | hello |
| printf ("%7s","hello") | bbhello |


**precision:**

| format | output |
|---|---|
| printf ("%.2f, %.0f", 1.141, 1.141) | 1.14, 1 |
| printf ("%.2e, %.0e", 1.141, 100.00) | 1.14e+00, 1e+02 |
| printf ("%.4s", "hello") | hell |
| printf ("%.1s", "hello") | h |

**modifier:**

| modifier | meaning |
|---|---|
| h | interpreted as short. Use with i,d,o,u,x |
| l | interpreted as long. Use with i,d,o,u,x |
| L | interpreted as double. Use with e,f,g |

**type:**

| Type | Meaning | Example |
| :--- | :--- | :--- |
| d, i | integer | printf ("%d", 10); /*prints 10*/ |
| x, X | integer (hex) | printf ("%x", 10); /*prints 0xa*/ |
| u | unsigned integer | printf ("%u", 10); /*prints 10*/ |
| c | character | printf ("%c", 'A'); /*prints A*/ |
| s | string | printf ("%s", "hello"); /*prints hello*/ |
| f | float | printf ("%f", 2.3); /*prints 2.3*/ |
| d | double | printf ("%d", 2.3); /*prints 2.3*/ |
| e, E | float(exp) | 1e3, 1.2E3, 1E-3 |
| % | literal % | printf ("%d %%", 10); /*prints 10%*/ |

`int scanf(char* format[],...)` is the input analog of printf. The format specification is the same as that for `printf()`.
  >**Important**: 
  > - `scanf()` ignores white spaces.
  > - Arguments have to be address of variables.

| printf | scanf |
|---|---|
| printf ("%d",x) | scanf ("%d",&x) |
| printf ("%10d",x) | scanf ("%d",&x) |
| printf ("%f",f) | scanf ("%f",&f) |
| printf ("%s",str) | scanf ("%s",str) /*note no & required*/ |
| printf ("%s",str) | scanf ("%20s",str) /*note no & required*/ |
| printf ("%s %s",fname,lname) | scanf ("%20s %20s",fname,lname) |

`printf` and `scanf` input data from either keyboard or file in command line. They have similar functions that input from string:

```C
int sprintf(char string [], char format[], arg1, arg2)
int sscanf(char str [], char format[], arg1, arg2)
```

C use `fopen()` to read data from text or binary files:

```C
FILE* fopen(char name[],char mode[])
```

- mode can be "r" (read only),"w" (write only),"a" (append) among other options.
- fopen returns a pointer to the file stream if it exists or `NULL` otherwise.
  
`fclose()` is used to close the stream (releases OS resources):

```C
int fclose(FILE* fp)
```

If the file stream `fp` is open.
- `getc()` reads a single character from stream.
- `fgets()` reads a single line.
- `putc()` writes a single character into stream.
- `fputs()` writes a single line.
- `fscanf` reads formated data from stream. Similar to `scanf()` and `sscanf()`.

```C
int getc(FILE* fp)
char[] fgets(char line [], int maxlen, FILE* fp)
int putc(int c, FILE* fp)
int fputs(char line [], FILE* fp)
int fscanf(FILE* fp, char format[], arg1, arg2)
```

`main()` can read the input from command line:

```C
int main(int argc, char* argv[])
```

| command line | argc | argv[0] | argv[1] | argv[2] |
| :--- | :--- | :--- | :--- | :--- |
| `./cat a.txt b.txt` | 3 | "cat" | "a.txt" | "b.txt" |
| `./cat` | 1 | "cat" | - | - |

# Lecture 5

## Memory

**Physical memory**: Physical resources where data can be stored and accessed by your computer
  - CPU cache
  - RAM
  - hard disk
  - removable device

**Virtual memory**: When program initializes, it may ask some memory address to store data. OS will distribute memory from RAM and hard disk to be the virtual memory. Virtual memory is sequence, and the virtual address starts from 0. 

Every variable residing in memory has an address except for
  - register variables
  - constants/literals/preprocessor defines
  - expressions (unless result is a variable)

`&` operator can access the address of variable. When data type is declared and followed by a `*`, it is a pointer of the data type.

```C
int n = 1; // n is a int variable
int* pn = &n; // pn is the pointer of n
double pi = 3.14; // pi is a double variable
double* ppi = &pi; // ppi is the pointer of pi
```

`*` operator followed by a pointer can dereference the pointer and access the value at corresponding address.

```C
printf("%d", *ppi); // output >> 3.14
```

Dereferenced pointer can operate just like variable.

```C
*ppi = *ppi + *pn; // pi is equal to 4.14 now
```

A pointer can be explicitly cast to any other type pointer by `()` operater.

```C
int var = 1;
int* p_int = &var;
double* p_double = (double*)p_int;
```

After above operation, `var` is still a `int` variable. Only when `p_double` is dereferenced that will treat the bits of `var` as `double`.

Functions can only return at most 1 variable in C. An alternative way to output multiple results is to pass pointers into the function.

```C
int a = 10, x, y;
int any_fn(a, &x, &y); // pass the pointers of x and y into function
```

Now `any_fn()` can modify the values of `x` and `y` by dereferencing the pointers.

Operator `sizeof()` is used to return size of type or variable in bytes.

```C
int int_size = sizeof(int); // int_size is 4 bytes in 64-bit system
int arr[8]; // arr is an integer array contains 8 integer element in sequential memory addresses
int arr_size = sizeof(arr); // arr_size is 32 (4 times 8) bytes
```

When `arr` is called without `[]` or `*` operator, it returns a pointer points to the first element of the array. `arr[i]` returns the i-th (i starts from 0) element and is equivalent to `*(arr+i)`. As mentioned above, `arr` is a pointer, and `arr+i` returns the i-th address behind the `arr`.

```C
int* parr = arr; // assume pa = 0x00
int a = arr[3]; // a equals to the int value stored in 0x0C
```

`<string.h>` contains some useful function for string manupulation:
  - `char* strcpy(strto,strfrom)`: Copy `strfrom` to `strto`.
  - `char* strncpy(strto,strfrom,n)`: Copy `n` chars from`strfrom` to `strto`.
  - `int strcmp(str1,str2)`: Compare `str1` and `str2`. Return 0 if equal, positive if `str1>str2`, negative if `str1<str2`.
  - `int strncmp(ste1,str2,n)`: Compare first `n` element of `str1` and `str2`.
  - `int strlen(str)`: Returns the length of `str`.
  - `char* strcat(strto,strfrom)`: Add `strfrom` to the end of `strto`.
  - `char* strncat(strto,strfrom,n)`: Add n chars from `strfrom` to the end of `strto`.
  - `char* strchr(str,c)`: Find char `c` in `str`. Returns pointer to the first occurrence, or `NULL` if not found.
  - `char* strrchr(str,c)`: Find char `c` in `str`. Returns pointer to the last occurrence, or `NULL` if not found.

## Quick sort

Quick sort is used to sort an array. It has average time comlexity `O(nlogn)` and worst time comlexity `O(n^2)`.

There are three main step of quick sort:
  1. Choose a pivot (the mid point generally), and classify the array into two. The left part consists of the elements smaller than the pivot, and the right part constists of the elements larger than the pivot.
  2. Quick sort the left part.
  3. Quick sort the right part.

The code of quick sort in recursive way is shown below:

```C
void quick_sort(int* left, int* right){
  if(left>=right) return;
  int pivot = *(left+(right-left)/2);
  swap(left,left+(right-left)/2);
  int* current, left_current = left;
  for(currrent=left+1;current<=right;++current)
    if(*current<pivot) swap(current,++left_current);
  int* mid = left_current;
  swap(mid,left);
  if(left_current>left) quick_sort(left,mid-1);
  if(left_current<right) quick_sort(mid+1,right);
}
```

