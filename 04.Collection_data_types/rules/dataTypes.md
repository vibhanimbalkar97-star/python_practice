## Important interview rules to remember

| Concept               |JavaScript                                             Python                                                  |
| --------------------- | -------------------------------------------------------- | ----------------------------------------------------
| Check type            | `typeof x` (with exceptions)                             | `type(x)`                                               |
| Check an array/list   | `Array.isArray(x)`                                       | `isinstance(x, list)`                                   |
| Equality              | `===` checks value and type; objects compare by identity | `==` checks equality; `is` checks       
                                                                                    identity              |
| Mutable example       | Array, object                                            | List, dict,  
                                                                                     set                                         |
| Immutable example     | String, number, boolean, `null`, `undefined`             | String, int, float, bool, `None`, tuple (with a  
                                                                                      caveat) |
| Convert to boolean    | `Boolean(x)`                                             | `bool(x)`                                               |
| Special numeric value | `NaN` has type `number`                                  | `float('nan')` has type 
                                                                                        `float`                         |

Interview tip: For every output question, follow these four steps:

1. Identify the data type of each value.
2. Check whether conversion happens.
3. Check whether the operation mutates an object or creates a new one.
4. Trace the expression from left to right, paying attention to operator precedence.