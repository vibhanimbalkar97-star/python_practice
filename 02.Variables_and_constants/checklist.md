Final interview revision checklist
Concept	                              JavaScript	                     Python
Declare a variable	                 let x = 10	                          x = 10
Constant convention	                 const x = 10	                      X = 10 (naming convention only)
Uninitialized variable	             let x; gives undefined	              Reading an unassigned name raises NameError
Reassignment	                     Allowed with let	                  Allowed
Scope	                             let and const are block-scoped	      Functions create local scope; if blocks do not
Hoisting	                         var is initialized to undefined;    
                                     let/const have a temporal dead zone	No JavaScript-style variable hoisting
Mutable objects	                     const objects can be mutated	        Lists and dictionaries can be mutated
Modify global variable inside function	Depends on declaration/scope rules	Use global to reassign a module-level variable

Important: Python has no enforced constant keyword like JavaScript's const. Uppercase names such as MAX_SIZE = 100 are a convention that tells programmers not to change the value.