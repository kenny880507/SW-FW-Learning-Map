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

# Lecture 6

## Structure

A `struct` defines a new datatype. The variables declared within a `struct` are called its `members`. Individual members can be accessed using `.` operator.

```C
struct new_type{
  int member1;
  float member2;
  // ...
};
struct new_type a={10, 3.14f};
struct new_type* pa = &a;
int b = a.member1;
float c = pa->member2;
```

`typedef` can be used to simply the syntax of struct declaration.

```C
struct new_type{
  int member1;
  float member2;
  // ...
};
typedef struct new_type NewType;
NewType a={10, 3.14f};
NewType* pa = &a;
int b = a.member1;
float c = pa->member2;
```

or

```C
typedef struct{
  int member1;
  float member2;
  // ...
}NewType;
NewType a={10, 3.14f};
NewType* pa = &a;
int b = a.member1;
float c = pa->member2;
```

The name of the structure is optional. A `struct` without type name is called anonymous struct. Anonymous struct must declare at least one variable at the end of definition.

```C
struct{
  int member1;
  float member2;
  // ...
}a, b, c;
```

In the above example, `a`, `b`, `c` is the only 3 three variables of this `struct`.

The size of a `struct` is greater than or equal to the sum of the sizes of its `members`. The arrangement of members is sequential in the memory. However, it might be filled by some useless bytes to match the specific alignment of memory for the consideration of CPU efficiency.


## Union

A `union` is a datatype that may hold objects of different types/sizes in the same memory location.

```C
union data{
  int i;
  float f;
  char* s;
};
union data d1;
d1.i = 10; // d1 stores int data;
d1.f = 2.1f;  // the int data in d1 is overwrited by float data;
```

The size of a `union` is the largest size of the members. `union` may only store the last assignment. However, you can read the data as other datatype. Using `char[]` is one way to inspect or manipulate the bytes of raw data.

## Bit field

A `bit-field` is a set of adjacent bits.

```C
unsigned int BOOL:1; // use a bit to represent for true or false
```

`unsigned int` is a convention that can prevent sign bit.

Another purpose of `bit-field` is to save the memory. If a variable only stores an integer ranges from 1 to 10, a large portion of `int` bytes will be wasted. Instead, using only 4-bit `int` to store it may be a reasonable way.

## Dynamic memory allocation

`void* malloc(size_t size)`:
  - Returns a pointer to **uninitialized** block of memory on success.
  - Returns NULL on failure.
  - The returned value should be cast to appropriate type. `int* ptr=(int*)malloc(sizeof(int)*100)`

`void* calloc(size_t n, size_t size)`:
  - Allocates an array of `n` elements each of which is `size` bytes.

`void* free(void*)`:
  - Frees memory allocated by `malloc()`.

> [!NOTE]
> The note about data structure might be skipped.  
> Another repo of mine contains more complete illustration. Please check out [here](https://github.com/kenny880507/Data-Structures-And-Algorithms-Log.git).

## Linked list

(skip)

## Binary tree

(skip)

# Lecture 7

## Struct: the order of member matters

The order of member may influence the memory size of the `struct`.

```C
struct foo{
  short s; // 2 bytes + 2 padding bytes = 4 bytes
  union{ // 4 bytes
    int i; // size of union determined by int
    char c;
  }u;
  unsigned int flag_s:1; // 1 bit
  unsigned int flag_u:2; // 2 bit, align with flag_s and pad to 4 bytes
  unsigned int bar; // 4 bytes
}
```

As the above example, total size of `foo` is 4+4+4+4=16 bytes. However, if the order of the `struct` changes, total size of `foo` can reduce to 12 bytes.

```C
struct foo{
  union{ // 4 bytes
    int i; // size of union determined by int
    char c;
  }u;
  unsigned int bar; // 4 bytes
  // below 3 members are aligned in 4 bytes
  short s; // 2 bytes
  unsigned int flag_s:1; // 1 bit
  unsigned int flag_u:2; // 2 bit
}
```

## Pointer array

There is an `int` array contains 100 elements.

```C
int arr[100];
```

If we want to sort the array without modifying array itself. We can use a pointer array `int*` containing pointers to elements of array and sort the pointers.

```C
int* ptr[100];
```

An array of strings stores pointers to the first `char` address (which is also a pointer) of each string.

```C
char str1[] = "hello";
char str2[] = "goodbye";
char* strArr[] = {str1,str2};
```

## Multidimensional arrays

C also permits multidimensional arrays:

```C
int arr[20][30]; // a 20x30 int array
```

Multidimensional arrays are rectangular; pointer arrays can be arbitrary shaped.

## Stack

(skip)

## Queue

(skip)

## Prefix, infix, postfix notation

Stacks and queues allow us to design a simple expression evaluator.

| Infix | Prefix | Postfix |
| :--- | :--- | :--- |
| A+B | +AB | AB+|
| A*B+C | -*ABC | AB*C- |
| (A+B)*(C-D) | *+AB-CD | AB+CD-* |

Infix more natural to write, postfix easier to evaluate.

# Lecture 8

## Void pointers

C allows `void` pointers. Void pointers can be used to point to any data type.

```C
int i;
void* pi = &i;
float f;
void* pf = &f;
```

`void` pointers cannot be dereferenced. The pointers should always be cast before dereferencing. 

```C
void* p;
printf("%d",*p); // invalid
printf("%d",*(int*)p); // valid
```

## Function pointers

In some programming languages, functions are first class variables (can be passed to functions, returned from functions etc.).

In C, function itself is not a variable. But it is possible to declare pointer to functions.

```C
int (*pf)(int);
```

## Callback

Definition: Callback is a piece of executable code passed to functions. In C, callbacks are implemented by passing function pointers.

```C
void qsort(void* arr, int num, int size, int (*fp)(void* pa, void* pb))
```

`qsort()` function from the standard library can sort an array of any datatype. It calls a function whenever a comparison needs to be done. The function takes two arguments and returns (<0,0,>0) depending on the relative order of the two items.

```C
int arr[] = {10,9,8,1,2,3,5};
int asc(void* pa, void* pb){
  return (*(int*)pa-*(int*)pb);
}
int desc(void* pa, void* pb){
  return (*(int*)pb-*(int*)pa);
}
qsort(arr,sizeof(arr)/sizeof(int),sizeof(int),asc); // sort in ascending order
qsort(arr,sizeof(arr)/sizeof(int),sizeof(int),desc); // sort in descending order
```

## Array of function pointers

Consider the case where different functions are called based on a value.

```C
enum TYPE{SQUARE,RECT,CIRCILE,POLYGON};
struct shape {
float params[MAX];
enum TYPE type;
};

void draw(struct shape* ps){
  switch(ps−>type){
    case SQUARE:
    draw_square(ps); break;
    case RECT:
    draw_rect(ps); break;
    //...
  }
} 
```

The same can be done using an array of function pointers instead.

```C
void (*fp[4])(struct shape* ps)={&draw_square,&draw_rec,&draw_circ,&draw_poly};
void draw(struct shape* ps){
  fp[ps->type](ps);
}
```

## Hash table

(skip)

# Lecture 9

## Symbols and libraries

Programs access libraries’ functions and variables via identifiers known as symbols. Header file declarations/prototypes mapped to symbols at compile time. Symbols linked to definitions in external libraries during linking.

```C
#include <stdio.h>

const char msg[] = "hello world!";

int main(void){
  puts(msg);
  return 0;
}
```

The functions `main()`, `puts()` and the variable `msg` are global and known as symbols.

The following command can produce `.o` file without linking:

```bash
gcc -Wall -c hello.c -o hello.o
```

- `-c`: compile without linking. The output `.o` file is not executable.
- Addresses for lines of code and static and global variables not yet assigned.
- Need to perform link step on `.o` (using `gcc` or `ld`) to assign memory to each symbol.
- Linking resolves symbols defined elsewhere and makes the code executable.

Use `nm` (Name List) command to list all symbols in the binary file.

```bash
nm hello.o
```

The output will be:

```bash
0000000000000000 T main
0000000000000000 R msg
                 U puts
```

- `T` means text (code). `R` means read-only memory. `U` means undefined symbol.
- Addresses are all zero before linking, and symbols are not allocated memory yet.
- Undefined symbols are defined externally and resolved during linking.

Instead, if we compile with linking:

```bash
gcc -Wall hello.o -o hello
nm hello
```

The output will be:

```bash
⋮
0000000000001149 T main
0000000000002008 R msg
                 U puts@GLIBC_2.2.5
```

- Addresses for static (allocated at compile time) symbols.
- Symbol `puts` located in shared library GLIBC_2.2.5 (GNU C standard library)
- Shared symbol `puts` not assigned memory until run time.

## Static and dynamic linkage

Memory can be allocated at compile time (static) or at run time (dynamic).

- Static linkage: Symbols in same file, other `.o` files, or static libraries `.a`.
- Dynamic linkage: Symbols in shared libraries `.so`.

`gcc` links against shared libraries by default, can force static linkage using `-static` flag.

If we complie with `-static` flag:

```bash
gcc -Wall -static hello.c -o hello
```

The output will be:

```bash
⋮
0000000000401775 T main
⋮
0000000000498008 R msg
⋮
000000000040c180 W puts
⋮
```

`W` means linked to another symbol.

### Static linkage

- At link time, statically linked symbols added to executable.
- Results in much larger executable file (static – 688K, dynamic – 10K).
- Resulting executable does not depend on locating external library files at run time.
- To use newer version of library, have to recompile main program.

### Dynamic linkage

- Dynamic linkage occurs at run-time.
- During compile, linker just looks for symbol in external shared libraries.
- Shared library symbols loaded as part of program startup (before `main()`).
- Requires external library to define symbol exactly as expected from header file declaration

### Linking external libraries

- Programs linked against C standard library by default.
- To link against library `libnamespec.so` (dynamic) or `libnamespec.a` (static) use compiler flag `-lnamespec` to link against library.
- Library must be in library path or specified using `-L <directory>` compiler flag

### Loading shared libraries

- Shared library located during compile-time linkage, but needs to be located again during run-time loading.
- Shared libraries located at run-time using linker library `ld.so`.
- Whenever shared libraries on system change, need to run `ldconfig` to update links seen by `ld.so`.
- During loading, symbols in dynamic library are allocated memory and loaded from shared library file.

### Loading shared libraries in .c

- In Linux, can load symbols from shared libraries on demand using functions in `dlfcn.h`.
- Open a shared library for loading:
  - `void* dlopen(const char* file, int mode)`
  - values for mode: combination of RTLD_LAZY (lazy loading of library), RTLD_NOW (load now), RTLD_GLOBAL (make symbols in library available to other libraries yet to be loaded), RTLD_LOCAL (symbols loaded are accessible only to your code)
- Get the address of a symbol loaded from the library:
  - `void* dlsym(void* handle, const char* symbol_name)`
  - `handle` from call to `dlopen()`; returned address is pointer to variable or function identified by `symbol_name`
- Need to close shared library file handle after done with symbols in library:
  - `int dlclose(void* handle)`
- These functions are not part of C standard library; need to link against library `libdl: -ldl` compiler flag.

### Creating libraries

| Action | Command line | Notes |
| :--- | :--- | :--- |
| compile `.o` | `gcc -g -Wall -c infile.c -o outfile.o` |
| create `.a` by `.o` | `ar -rcs libname.a outfile1.o outfile2.o` |
| compile `.o` (for `.so`) | `gcc -g -Wall -fPIC -c infile.c -o outfile.o` | `-fPIC`: create  position-independent code, since code will be repositioned during loading |
| create `.so` by `.o` | `ld -shared -soname libname.so -o libname.so.version -lc outfile1.o outfile2.o` | `-lc`: find the library named `libc.so` |

> [!NOTE]
> `-l` flag is used to find the lib that matches naming convention of Linux.  
> The `.so` file who mathches `lib<name>.so` can be find by `-l` flag.  
> `-la` will find `liba.so`; `-labc` will find `libabc.so`.

### Summary of compile process

1. Compile `.c` files to `.o` files.
2. (optional) Pack `.o` files to a dynamic library `.a` by `ar` (archiver) tool. Link `.o` files to a static library `.so` by `gcc` or `ld` (linker).
3. Compile executable, and link it to `.o`, `.a`, `.so`. 
    > `-L <dir>` is a flag for linker to find the libraries.  
    > Executable distribute memory to symbols from `.o` and `.a`.  
    > The `U` symbols will be labeled with the name of `.so`.
4. At the beginning of the program, the static symbols (from `.o` and `.a`) are already in the memory. Dynamic Loader will find the `.so` files from `rpath`, LD_LIBRARY_PATH, system cache, etc. Then, load the `.so` into virtual memory. The `U` symbol will fix-up and point to the address at `.so` (in virtual memory).

## B-tree

(skip)

## Priority queue

(skip)

# Lecture 10

## <stdio.h>

```C
FILE* fopen(const char* filename, const char* mode)
```

- `mode` can be "r" (read), "w" (write), "a" (append)
- 'b' can be appended for binary input/output (unnecessary in Linux)
- returns NULL on error

```C
FILE* freopen(const char* filename, const char* mode, FILE* stream)
```

- redirects the stream to the file
- returns NULL on error

```C
int fflush(FILE* stream)
```

- flushes any unwritten data
- if stream is NULL flush all output streams
- returns EOF on error

```C
int remove(const char* filename)
```

- removes the file from the file system
- returns non-zero on error

```C
int rename(const char* oldname, const char* newname)
```

- renames file
- returns non-zero on error

```C
FILE* tmpfile(void)
```

- create a temporary file with mode "wb+"
- the file is removed automatically when program terminates

```C
char* tmpnam(char s[L_tmpnam])
```

- creates a string that is not the name of existing file
- return reference to internal static array if `s` is NULL or populate `s` otherwise
- generates a new name every call

```C
size_t fread(void* ptr, size_t size, size_t nobj, FILE* stream)
```

- reads at most `nobj` (number of object) items of size `size` from stream into `ptr`
- returns the number of items read
- `feof()` and `ferror()` must be used to test end of file

```C
size_t fwrite(const void* ptr, size_t size, size_t nobj, FILE* stream)
```

- write at most `nobj` items of size `size` from `ptr` onto `stream`
- returns number of objects written

```C
int fseek(FILE* stream, long offset, int origin)
```

- sets file position in the stream
- `origin` can be `SEEK_SET`, `SEEK_CUR`, `SEEK_END`
- returns non-zero on error

```C
long ftell(FILE* stream)
```

- returns the current position within the file
- returns -1L on error

```C
int rewind(FILE* stream)
```

- sets the file pointer at beginning
- equivalent to `fseek(stream,0L,SEEK_SET)

```C
void clearerr(FILE* stream)
```

- clears EOF and other error indicators on stream

```C
int feof(FILE* stream)
```

- returns non-zero if end of file indicator is set for stream
- only way to test end of file for functions such as `fwrite()`, `fread()`

```C
int ferror(FILE* stream)
```

- returns non-zero if any error indicator is set for stream

## <ctype.h>

| function | true condition |
| :--- | :--- |
| isalnum(c) | isalpha(c) || isdigit(c) |
| iscntrl(c) | control characters |
| isdigit(c) | 0~9 |
| islower(c) | 'a'~'z' |
| isprint(c) | printable character (includes space) |
| ispunct(c) | punctuation |
| isspace(c) | space, tab or new line |
| isupper(c) | 'A'~'Z' |

## <string.h>

```C
void* memcpy(void* dst, const void* src, size_t n)
```

- copies `n` bytes from `src` to `dst`
- returns a pointer to `dst`
- `src` and `dst` can not overlap

```C
void* move(void* dst, const void* src, size_t n)
```

- behaves same as `memcpy()`
- `src` and `dst` can overlap

```C
int memcmp(const void* cs, const void* ct, int n)
```

- compares first `n` bytes of `cs` and `ct`

```C
void* memset(void* dst, int c, int n)
```

- fills first `n` bytes of `dst` with the value `c`
- returns a pointer to `dst`

## <stdlib.h>

```C
double atof(const char* s)
int atoi(const char* s)
long atol(const char* s)
```

- converts character or string to float, integer, long

```C
int rand()
```

- returns a psudo-random numbers betweem 0 and RAND_MAX

```C
void srand(unsigned int seed)
```

- sets the seed for the psudo-random generator

```C
void abort(void)
```

- causes the program to terminate abnormally

```C
void exit(int status)
```

- causes normal program termination
- `status` is returned to operating system
- 0 (EXIT_SUCCESS) indicates successful termination
- Any other value indicates failure (EXIT_FAILURE)

```C
int atexit(void (*fcn)(void))
``` 

- registers a function fcn to be called when the program terminates normally
- returns non zero when registration cannot be made
- after `exit()` is called, the functions are called in reverse order of registration

```C
int system(const char* cmd)
```

- execute the command in string `cmd`
- if `cmd` is not null, the program executed the command and returns exit status returned by the command

```C
void* bsearch(const void* key, const void* base, size_t n, size_t size, int (*cmp)(const void* keyval, const void datum))
```

- binary-searches `base[0]` through `base[n-1]` for `*key`
- can only operate normally for sorted array
- `cmp()` is used to perform comparison
- returns a pointer to the matching item if exits and NULL otherwise

```C
void qsort(void* base, size_t n, size_t sz, void (*cmp)(const void*, const void*))
```

- sorts `base[0]` through `base[n-1]` in ascending/descending order (determined by `cmp()`)

## <assert.h>

```C
void assert(int expression)
```

- used to check for invariants/code consistency during debugging
- does nothing when expression is true
- prints an error message indicating, expression, filename and line number
  > macros `__FILE__` and `__LINE__` are frequently used for debugging  
  > `__FILE__` returns `const char*` that stores the file name  
  > `__LINE__` returns `int` that represents the line number in the file  

## <stdarg.h>

Variable argument lists:
  - functions can accept variable number of arguments
  - the data type of the argument can be different for each argument
  - atleast one mandatory argument is required

```C
va_list ap
```

- `va_list` is a data type defined in <stdarg.h>
- `ap` defines an iterator that will point to the variable argument
- before using, it has to be initialized using `va_start()`

```C
va_start(va_list ap, lastarg)
```

- lastarg refers to the **name** of the last named argument
- va_start is a macro

```C
va_arg(va_list ap, type)
```

- each call of `va_arg()` points `ap` to the next argument
- type has to be inferred from the fixed argument or determined based on previous argument

```C
va_end(va_list ap)
```

- must be called before the function is exited

```C
int sum(int num, ...){
  va_list ap; int total = 0;
  va_start(ap, num);
  while (num>0){
    total += va_arg(ap, int) ;
    num−−;
  }
  va_end(ap);
  return total;
}
int suma=sum(4, 1, 2, 3, 4);
int sumb=sum(2, 1, 2);
```

## <time.h>

`time_t`, `clock_t`, `struct tm` are data types associated with time.

`struct tm`:
| member | meaning |
| --- | --- |
| `int tm_sec` | seconds |
| `int tm_min` | minutes |
| `int tm_hour` | hour since midnight (0,23) |
| `int tm_mday` | day of the month (1,31) |
| `int tm_mon` | month |
| `int tm_year` | years since 1900 |
| `int tm_wday` | day since sunday (0,6) |
| `int tm_yday` | day since Jan 1 (0,365) |
| `int tm_isdst` | DST flag |

```C
clock_t clock()
```

- returns processor time used since beginning of program
- divided by CLOCKS_PER_SEC to get time in seconds 

```C
time_t time(time_t* tp)
```

- returns current time (seconds since Jan 1 1970)
- if `tp` is not NULL, also populates `tp`.

```C
double difftime(time_t t1,time_t t2)
```

- returns difference in seconds

```C
time_t mktime(struct tm* tp)
```

- converts the structure to a time_t object
- returns -1 if conversion is not possible

```C
char* asctime(const struct tm* tp)
```

- returns string representation of the form "Sun Jan 3 15:14:13 1988"
- returns static reference (can be overwritten by other calls)

```C
struct tm* localtime(const time_t* tp)
```

- converts calendar time to local time

```C
char* ctime(const time_t* tp)
```

- converts calendar time to string representation of local time
- equivalent to asctime(localtime(tp))

```C
size_t strftim(char* s, size_t smax, const char* fmt, const struct tm* tp)
```

- returns the successfully written number of characters
- format time string is write on `s`
- does not write more than smax characters into the string s

| `fmt` representation | meaning |
| --- | --- |
| `%a` | abbreviated weekday name |
| `%A` | full weekday name |
| `%b` | abbreviated month name |
| `%B` | full month name |
| `%d` | day of the month |
| `%H` | hour (0-23) |
| `%I` | hour (0-12) |
| `%m` | month |
| `%M` | minute |
| `%p` | AM/PM |
| `%S` | second |

# Lecture 11

## Dynamic memory allocation

`mmap()` in <sys/mman.h> is used to creates a new mapping in the virtual address. Virtual memory can be returned to OS using `munmap()`.

The process of memory allocation:
  1. `mmap()` distributes new virtual memory in page table. The virtual memory is mapping to back memory now.
    > Back memory is either file (in disk) or demand-zero memory (in RAM).
  2. When the variable is called, "page fault" occurs.
  3. Initialize new page frame, demand-zero memory is initialized to 0 and file is populate to RAM.
  4. Update page table, the virtual memory is mapping to the new page frame now.

```C
void* mmap(void* start, size_t length, int prot, int flags, int fd, off_t offset)
```

- asks OS to map virtual memory of specified length, using specified physical memory (file or demand-zero)
- `fd` is file descriptor (integer referring to a file, not a file stream) for physical memory (i.e. file) to load into memory
- for demand-zero, including the heap, use `MMAP_ANON` flag
- `start` – suggested starting address of mapped memory, usually NULL

```C
int munmap(void* start, size_t length)
```

- returns 0 on success or -1 on failure

## Heap

> [!IMPORTANT]
> The "heap" mentioned in memory management is different from the heap in data structure.

### Fundamental concept

- **What is heap?** Heap is private section of virtual memory used to allocate memory dynamically. The heap is mapping to demand-zero memory.
- **How to grow up?** A heap is initially empty and has 0 size. `brk` is an OS pointer to the top of heap.
- **Expand heap region:** `sbrk()` is used to resize heap.
- **Duty of allocator:** Dynamic memory allocators divide heap into blocks.

### Requirements

A good memory allocator must meet the following requirements:
  - Must be able to allocate, free memory in any order.
  - Auxiliary data structure must be on heap.
  - Allocated memory cannot be moved.
  - Attempt to minimize fragmentation.

### Fragmentation

Fragmentation is a major challenge in heap management:
  - Internal fragmentation: block size larger than allocated variable in block.
  - External fragmentation: free blocks spread out on heap. To minimize external fragmentation, fewer larger free blocks is prefered.

### Design choice

To achieve the above requirements and solve the fragmentation problem, the allocator must make the following design choices:
  - Data structure to track blocks
  - Algorithm for positioning a new allocation
  - Splitting/joining free blocks

### Tracking blocks

A block can be separated to two sections — metadata and payload. Metadata stores the information about the block itself. Payload stores the pointer to the next free block (if it is explicit free list) or the data occupied by the program.

According to the expression of free state, there two kinds of free list:
  - Implicit free list: Free state is stored in the metadata.
  - Explicit free list: Each free block stores the pointer to the next free block, and the head pointer to the first free block is stored outside the heap. Segmented free list is an optimized version of explicit free list. It uses a list to classify different size of the block and shorten search time.
    > The next pointer is stored in payload region. When the memory is distributed, the data will directly overwrite the memory of it.

### Positioning allocations

There are three strategy to find the block:
  - Fist fit: Start at the head of the list.
  - Next fit: Start at the end of last search.
  - Best fit: Traverse entire list to find the best matched block.

### Splitting and joining blocks

- At allocation, can use entire free block, or part of it, splitting the block in two.
- Splitting reduces internal fragmentation, but more complicated to implement.
- To join (coalesce) adjacent free blocks during (or after) freeing can reduce external fragmentation.
- The footer of a block stores the pointer to the header of that block, allows the successive block to find address of previous block.

### Relationship between heap, block and page

The hierarchy level:

**`heap`>`block` and `heap`>`page`**

`page` is the smallest unit in virtual memory and has a fixed size detemined by the system. A `page` maps to a real memory called `page frame`. The size of a `page frame` is same as `page`.

A `block` is formed by dividing `pages` and sequential in virtual memory. A `page` can be devided into many `block`. A `block` can also across many `pages`.

The `heap` is filled with `blocks`. `allocator` use `heap` to manage `blocks`.

## Using `malloc()`

- Minimize overhead – use fewer, larger allocations.
- Minimize fragmentation – reuse memory allocations as much as possible.
- Growing memory – using realloc() can reduce fragmentation.
- Repeated allocation and freeing of variables can lead to poor performance from unnecessary splitting/coalescing (depending on implementation of malloc()).

## `valgrind` tools

Usage:

```bash
valgrind --tool=memcheck --leak-check=yes program.o
```

- Tools:
  - `memcheck`: Runs program using virtual machine and tracks memory leaks.
  - `cachegrind`: Counts cache misses for each line of code.
  - `callgrind`: Counts function calls and costs in program.
  - `massif`: Tracks overall heap usage.

## Garbage collection

- C implements no garbage collector.
- Memory not freed remains in virtual memory until program terminates.
- Other languages like Java implement garbage collectors to free unreferenced memory.

# Lecture 12

## Parallelism vs Concurrency

- **Parallelism**: Capable of executing tasks concurrently across multiple hardware units.
  - Instruction level (pipelining)
  - Data parallelism (SIMD)
  - Task parallelism (embarrassingly parallel)
- **Concurrency**: Multiple tasks can be handled concurrently in software without necessarily requiring multiple hardware units.

## Process vs. Threads

Process is an instance of executing program. Each process must own a main thread. Threads can be created by process and are the tasks that need to be executed by cpu. Scheduler will assign threads to cpu cores to execute parallelly.

## <pthread.h>

`<pthread.h>` is a header file to use multithreads in POSIX system. A flag `-pthread` is used to compile source files that include `<pthread.h>`.

```bash
gcc -g -O0 -Wall <source>.c -o <output>.o -pthread
```

### Data type

There are 4 commonly used data type about pthread:

- `pthread_t`: Used to reference the thread after successful creation with pthread_create.
- `pthread_attr_t`: Passed to pthread_create to specify thread attributes like detach state or stack size.
- `pthread_mutex_t`: Ensures that only one thread can enter the critical section at any given time.
- `pthread_cond_t`: Allows threads to sleep efficiently while waiting for a condition, avoiding busy waiting (polling).

### pthread_t

```C
int pthread__create(pthread_t* thread, const pthread_attr_t* attr, void *(*start_routine)(void*), void* arg)
```

- Creates a new thread with the attributes specified by `attr`.
- Default attributes are used if `attr` is `NULL`.
- On success, stores the thread into `thread`.
- Calls function `start_routine(arg)` on a separate thread of execution.
- Returns zero on success, non-zero on error.

```C
void pthread_exit(void* value_ptr)
```

- Called implicitly when thread function exits.
- Analogous to `exit()`.

```C
int pthread_join(pthread_t thread, void **value_ptr)
```

- `pthread_join()` blocks the calling thread until the specified thread terminates.
- If `value_ptr` is not null, it will contain the return status of the called thread.
- The `attr` of `thread` must be JOINABLE.
  > If the `attr` of `thread` is DETACHED, source will release automatically.

### pthread_attr_t

```C
int pthread_attr_init(pthread_attr_t* attr)
```

- Initialize the `pthread_attr_t` instance by the pointer.

```C
int pthread_attr_setdetachstate(pthread_attr_t *attr, int detachstate)
```

- Set the detach state which may be `PTHREAD_CREATE_DETACHED` or `PTHREAD_CREATE_JOINABLE` (default).

```C
int pthread_attr_destroy(pthread_attr_t *attr)
```

- Destroy the target `pthread_attr_t`.
- The threads created by `attr` will not be destroyed.

### pthread_mutex_t

Mutex (mutual exclusion) acts as a "lock" protecting access to the shared resource. Only one thread can "own" the mutex at a time. Threads must take turns to lock the mutex.

```C
int pthread_mutex_init(pthread_mutex_t* mutex, const pthread_mutexattr_t* mutexattr)
```

-  If mutexattr is `NULL`, default are used.
-  The macro `PTHREAD_MUTEX_INITIALIZER` can be used to initialize static mutexes.

```C
int pthread_mutex_destroy(pthread_mutex_t* mutex)
```

- Destroy the target `pthread_mutex_t`.

```C
int pthread_mutex_lock(pthread_mutex_t* mutex)
int pthread_mutex_trylock(pthread_mutex_t* mutex)
int pthread_mutex_unlock(pthread_mutex_t* mutex)
```

- `pthread_mutex_lock()` locks the given mutex. If the mutex is locked, the function is blocked until it becomes available.
- `pthread_mutex_trylock()` is the non-blocking version. If the mutex is currently locked the call will return immediately.
- `pthread_mutex_unlock()` unlocks the mutex.

### pthread_cond_t

```C
int pthread_cond_init(pthread_cond_t* cond, const pthread_condattr_t* attr)
pthread_cond_t cond = PTHREAD_COND_INITIALIZER
```

- Two ways to initialize `pthread_cond_t`.

```C
int pthread_cond_destroy(pthread_cond_t* cond);
```

- Destroy (uninitialize) the target `pthread_cond_t`.
- Destroying a `pthread_cond_t` upon which other threads are currently blocked results in undefined behavior.

```C
int pthread_cond_wait(pthread_cond_t* cond, pthread_mutex_t* mutex);
```

- Blocks on a condition variable.
- Must be called with the mutex already locked otherwise behavior undefined.
- Automatically releases mutex.
- When `pthread_cond_broadcast(cond)` or `pthread_cond_signal(cond)` executed, the mutex will be automatically locked again.

```C
int pthread_cond_broadcast(pthread_cond_t* cond)
int pthread_cond_signal(pthread_cond_t* cond)
```

- `pthread_cond_broadcast()` unlocks all threads that are waiting.
- `pthread_cond_broadcast()` unlocks one of the waiting threads.

# Lecture 13





# Lecture 14