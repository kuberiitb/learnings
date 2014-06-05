R Functions
==============

From R in a Nutshell
-------------------

### The Function Keyword
Basic Syntax: 
functionName <- function(arguments){ body } 
eg: `f <- function(x,y) {x+y} `

### Return Values
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
### Functions As Arguments  
Many functions in R can take other functions as arguments. eg: sapply
```sh
a=1:10   
sapply(a,sqrt)
1.000000 1.414214 1.732051 2.000000 2.236068 2.449490 2.645751 2.828427 3.000000 3.162278
```

