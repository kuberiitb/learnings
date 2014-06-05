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
Many functions in R can take other functions as arguments. eg: [sapply]
```sh
a=1:10   
sapply(a,sqrt)
1.000000 1.414214 1.732051 2.000000 2.236068 2.449490 2.645751 2.828427 3.000000 3.162278
apply(airquality,2,function(x){return(sum(is.na(x)))})
Ozone Solar.R   Wind    Temp    Month     Day 
37    7         0       0       0         0 
```

### Anonymous Functions
Because functions are just objects in R, it is possible to create functions that do not have names. 
These are called anonymous functions. Anonymous functions are usually passed as arguments to other functions.

We will define a function *apply.to.three* that takes another function as its argument and then applies that function to the number 3.
```sh
apply.to.three <- function(f) {f(3)}
apply.to.three(function(x) {x * 7})
21
```
#### How it works?
When the R interpreter evaluates the expression `apply.to.three(function(x) {x * 7})` ,it assigns the argument f to the anonymous function function(x) {x * 7}. 
The interpreter then begins evaluating the expression f(3). 
The interpreter assigns 3 to the argument x for the anonymous function. 
Finally, the interpreter evaluates the expression 3 * 7 and returns the result.


[sapply]:http://www.pmc.ucsc.edu/~mclapham/Rtips/apply_sapply.htm
