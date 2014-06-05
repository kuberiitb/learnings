R Functions
==============

From R in a Nutshell
-------------------

###The Function Keyword
Basic Syntax: 
functionName <- function(arguments){ body } 
eg: `f <- function(x,y) {x+y} `

###Return Values
In an R function, you may use the return function to specify the value returned by the function.
However, R will simply return the last evaluated expression as the result of a function.
So, it is common to omit the return statement
```sh
f <- function(x) {return(x^2 + 3)}
g <- function(x) {x^2 + 3}
f(3)
12
g(3)
12  #same values
```
