# JavaScript vs Python – Quick Interview Revision Checklist

Use this table for quick revision of Basics & Syntax, Variables, Data Types, Type Conversion, and Operators. Each row covers an important rule, example, and why it works.

\| ✓ | Topic / Rule             | Python             | JavaScript           | Why / Explanation |
\| ☐ | 1. Syntax – print output | `print("Hello")`   | `console.log("Hello")`| Both display output, but use different functions. |\
\| ☐ | Case sensitivity         | `name` and `Name` are different             | `name` and `Name` are different | Both languages are case-sensitive. |\
\| ☐ | Statement ending | `a = 10` | `let a = 10;` | Python doesn't require `;`. JS commonly uses it. |\
\| ☐ | Code blocks | Indentation defines blocks | `{ }` define blocks | Python depends on indentation; JS uses braces. |\
\| ☐ | Comments | `# comment` | `// comment` | Single-line comment syntax differs. |\
\| ☐ | Multiline comments | `""" comment """` | `/* comment */` | Python triple quotes are strings, not technically comments. |\
\| ☐ | Boolean keywords | `True`, `False` | `true`, `false` | Python uses capital letters. |\
\| ☐ | Null value | `None` | `null` | Both represent absence of a value. |\
\| ☐ | Undefined value | No built-in `undefined` | `undefined` | JS has a special value for an unassigned variable. |\
\| ☐ | Logical AND | `and` | `&&` | Both require both conditions to be truthy. |\
\| ☐ | Logical OR | `or` | `||` | Both return a truthy result if at least one operand is truthy. |\
\| ☐ | Logical NOT | `not a` | `!a` | Reverses Boolean truthiness. |\


\| ☐ | 2. Variable declaration | `a = 10` | `let a = 10;` | Python creates a variable by assignment; JS uses declarations. |\
\| ☐ | Reassignment | `a = 20` | `a = 20;` | Changes the value associated with the variable. |\
\| ☐ | Declaration | `a = 10` | `let a;` | Python has no separate declaration statement. |\
\| ☐ | Constant | `PI = 3.14` | `const PI = 3.14;` | Python uppercase is a naming convention; JS `const` prevents reassignment. |\
\| ☐ | `const` reassignment | `PI = 4` allowed | `PI = 4` → TypeError | Python doesn't enforce constants. |\
\| ☐ | `const` object mutation | `data["x"] = 20` allowed | `data.x = 20` allowed | JS `const` prevents reassignment, not object mutation. |\
\| ☐ | `let` redeclaration | `a = 20` allowed | `let a = 20` → SyntaxError in same scope | Python assignment is not redeclaration. |\
\| ☐ | `var` | No equivalent | `var a = 10;` | `var` is function-scoped and can be redeclared. |\
\| ☐ | Variable without value | `a = None` | `let a;` → `undefined` | Python requires assigning a value; JS declaration can leave it undefined. |\
\| ☐ | Scope | Function and block behavior differs | `let`/`const` block-scoped | Python has no separate block scope for `if` or `for`. |\


\| ☐ | 3. Integer | `a = 10` → `int` | `a = 10` → `number` | JS has one standard Number type for integers and floats. |\
\| ☐ | Float / decimal | `a = 10.5` → `float` | `a = 10.5` → `number` | Python distinguishes `int` and `float`. |\
\| ☐ | String | `"Hello"` → `str` | `"Hello"` → `string` | Both represent text. |\
\| ☐ | Boolean | `True` → `bool` | `true` → `boolean` | Different capitalization. |\
\| ☐ | List / Array | `[1, 2, 3]` → `list` | `[1, 2, 3]` → `Array` | Both store multiple values; Python lists and JS arrays are mutable. |\
\| ☐ | Tuple | `(1, 2, 3)` → `tuple` | No built-in tuple | Python tuple is immutable; JS uses arrays or other structures. |\
\| ☐ | Dictionary / Object | `{"a": 10}` → `dict` | `{a: 10}` → Object | Both store key-value pairs. |\
\| ☐ | Set | `{1, 2, 3}` → `set` | `new Set([1,2,3])` | Both store unique values. |\
\| ☐ | Check type | `type(a)` | `typeof a` | Different syntax and output formats. |\
\| ☐ | Type of null | `type(None)` → `NoneType` | `typeof null` → `"object"` | JS historical behavior; `null` is not really an object. |\
\| ☐ | Type of array | `type([1,2])` → `list` | `typeof [1,2]` → `"object"` | Use `Array.isArray()` in JS. |\


\| ☐ | 4. Explicit conversion | `int("10")` | `Number("10")` | Both convert string to number. |\
\| ☐ | Convert to string | `str(10)` → `"10"` | `String(10)` → `"10"` | Converts value to text. |\
\| ☐ | Convert to float | `float("2.5")` | `Number("2.5")` | Python has `float()`; JS Number handles decimals too. |\
\| ☐ | Convert to integer | `int(2.9)` → `2` | `parseInt("2.9")` → `2` | Python truncates decimal; JS `parseInt` parses integer portion. |\
\| ☐ | Convert Boolean | `bool(0)` → `False` | `Boolean(0)` → `false` | Both convert truthiness. |\
\| ☐ | Boolean of string `"False"` | `bool("False")` → `True` | `Boolean("false")` → `true` | Non-empty strings are truthy in both. |\
\| ☐ | Empty string | `bool("")` → `False` | `Boolean("")` → `false` | Empty strings are falsy. |\
\| ☐ | Convert invalid number | `int("hello")` → ValueError | `Number("hello")` → `NaN` | Python throws an error; JS returns NaN. |\
\| ☐ | Convert `"12abc"` | `int("12abc")` → ValueError | `parseInt("12abc")` → `12` | `parseInt` parses a valid initial integer portion. |\
\| ☐ | Convert `"12.5"` | `float("12.5")` → `12.5` | `Number("12.5")` → `12.5` | Both parse valid decimal text. |\

\| ☐ | Implicit conversion | `"10" + 2` → `"102"` | `"10" + 2` → `"102"` | `+` joins text when a string is involved. |\
\| ☐ | String minus number | `"10" - 2` → `8` | `"10" - 2` → `8` | JS converts string to number; Python raises TypeError. |\
\| ☐ | String times number | `"Hi" * 3` → `"HiHiHi"` | `"Hi" * 3` → NaN | Python supports string repetition; JS doesn't. |\

\| ☐ | 5. Addition | `10 + 2` → `12` | `10 + 2` → `12` | Both add numbers. |\
\| ☐ | String concatenation | `"Hi" + "!"` → `"Hi!"` | `"Hi" + "!"` → `"Hi!"` | `+` joins strings. |\
\| ☐ | Division | `10 / 2` → `5.0` | `10 / 2` → `5` | Python `/` always produces float; JS Number has no separate integer type. |\
\| ☐ | Floor division | `10 // 3` → `3` | `10 // 3` → SyntaxError | Python `//` gives floor division. |\
\| ☐ | Negative floor division | `-7 // 2` → `-4` | `Math.floor(-7 / 2)` → `-4` | Python rounds down toward negative infinity. |\
\| ☐ | Modulus | `10 % 3` → `1` | `10 % 3` → `1` | Remainder; negative values behave differently. |\
\| ☐ | Exponent | `2 ** 3` → `8` | `2 ** 3` → `8` | Both use `**` for power. |\
\| ☐ | Increment | `a += 1` | `a++` or `a += 1` | Python doesn't support `++`. |\
\| ☐ | Comparison equal | `10 == 10` → `True` | `10 == 10` → `true` | Checks value equality. |\
\| ☐ | Strict equality | `10 == "10"` → `False` | `10 === "10"` → `false` | Python `==` checks types as part of equality; JS `===` avoids coercion. |\
\| ☐ | Loose equality | No equivalent | `10 == "10"` → `true` | JS `==` performs type coercion. |\
\| ☐ | Not equal | `10 != 5` → `True` | `10 != 5` → `true` | Both check inequality. |\
\| ☐ | Chained comparison | `1 < a < 10` | `1 < a && a < 10` | Python supports chained comparisons directly. |\
\| ☐ | Logical AND | `True and False` → `False` | `true && false` → `false` | Both short-circuit. |\
\| ☐ | Logical OR | `0 or 5` → `5` | `0 || 5` → `5` | Both return an operand, not necessarily Boolean. |\
\| ☐ | Falsy zero | `bool(0)` → `False` | `Boolean(0)` → `false` | Zero is falsy in both. |\
\| ☐ | Empty list | `bool([])` → `False` | `Boolean([])` → `true` | Major difference: JS arrays are truthy, even empty. |\
\| ☐ | Empty object | `bool({})` → `False` | `Boolean({})` → `true` | Empty Python dict is falsy; JS object is truthy. |\
\| ☐ | Nullish default | `a if a is not None else 5` | `a ?? 5` | JS `??` uses fallback only for null or undefined. |\
\| ☐ | OR fallback | `a or 5` | `a || 5` | Both use fallback for falsy values; JS also treats `""`, `0`, `false` as falsy. |\
\| ☐ | Bitwise AND | `5 & 3` → `1` | `5 & 3` → `1` | Operates on binary bits. |\
\| ☐ | Bitwise OR | `5 \| 3` → `7` | `5 \| 3` → `7` | Sets a bit if either operand has it. |\
\| ☐ | Bitwise XOR | `5 ^ 3` → `6` | `5 ^ 3` → `6` | Sets a bit if bits differ. |\
\| ☐ | Left shift | `5 << 1` → `10` | `5 << 1` → `10` | Shifts bits left. |\
\| ☐ | Membership | `2 in [1,2,3]` → `True` | `[1,2,3].includes(2)` → `true` | Python uses `in`; JS commonly uses `includes()`. |\
\| ☐ | Membership in dict | `"a" in {"a": 1}` → `True` | `"a" in {a: 1}` → `true` | Checks keys in both. |\
\| ☐ | Identity | `a is b` | `a === b` (not always equivalent) | Python `is` checks object identity; JS `===` compares values/references. |\
\| ☐ | Object equality | `[1,2] == [1,2]` → `True` | `[1,2] === [1,2]` → `false` | Python lists compare contents; JS arrays compare references. |\
\| ☐ | `NaN` equality | `float("nan") == float("nan")` → `False` | `NaN === NaN` → `false` | NaN is unequal to itself. |\
\| ☐ | Check NaN | `math.isnan(a)` | `Number.isNaN(a)` | Explicitly checks NaN. |\
\| ☐ | Operator precedence | `2 + 3 * 4` → `14` | `2 + 3 * 4` → `14` | Multiplication occurs before addition. |\
\| ☐ | Assignment with operation | `a += 2` | `a += 2` | Both update the variable. |\
\| ☐ | Ternary expression | `"Yes" if a > 0 else "No"` | `a > 0 ? "Yes" : "No"` | Conditional expression syntax differs. |\
\| ☐ | Type coercion | `"5" + 2` → `"52"` | `"5" + 2` → `"52"` | Both concatenate; JS has additional implicit conversions for other operators. |

## Quick memory rules

\| Python                                                     | JavaScript |\
\|---|---|\
\| `print()`                                                   | `console.log()` |\
\| `input()`                                                   | `prompt()` (browser) |\
\| `None`                                                      | `null` |\
\| `True` / `False`                                            | `true` / `false` |\
\| `and` / `or` / `not` | `&&` / `||` / `!` |\
\| `int()` / `float()` / `str()` | `Number()` / `String()` |\
\| `type()` | `typeof` |\
\| `//` floor division | `Math.floor(a / b)` |\
\| `**` power | `**` power |\
\| `in` membership | `includes()` for arrays |\
\| `is` identity | `===` value/reference comparison |\
\| `list` | `Array` |\
\| `dict` | `Object` |\
\| `tuple` | No built-in tuple |\
\| `None` check: `is None` | Nullish check: `== null` or `??` |\
\| Indentation | `{ }` blocks |\
\| `elif` | `else if` |\
\| `f"{name}"` | `` `${name}` `` |\
\| `range(5)` | `for (let i=0; i<5; i++)` |
