R Functions
==============
(from **R in a Nutshell**)

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
> 1.000000 1.414214 1.732051 2.000000 2.236068 2.449490 2.645751 2.828427 3.000000 3.162278
apply(airquality,2,function(x){return(sum(is.na(x)))})
> Ozone Solar.R   Wind    Temp    Month     Day 
> 37    7         0       0       0         0 
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

### Properties of Functions
R includes a set of functions for getting more information about function objects.
**args:** returns set of arguments accepted by a function
**formals:** extract information about the arguments to a function(only available for functions written in R and not for built-in functions)
**body:** return the body of a function
```sh
f <- function(x,y=1,z=2) {x+y+z}
f(3)
>6
formals(f)
$x
$y
[1] 1
$z
[1] 2

body(f)
{
    x + y + z
}
```

### Argument Order and Named Arguments
When you specify a function in R, you assign a name to each argument in the function.   
Inside the body of the function, you can access the arguments by name.  
eg. `addTheLog <- function(first, second) {first + log(second)}`   
When we call a function in R, we can specify the arguments in three different ways
(in order of priority):   
1.Exact names: `addTheLog(second=exp(4),first=1)` return 5
2.Partially matching names: `addTheLog(s=exp(4),f=1)` again returns 5 as s matches with second, f with first and no confusion occur.
3.Argument order: `addTheLog(1,exp(4))` Here we have to pass the argument in specified order, otherwise output will be wrong. 






[sapply]:http://www.pmc.ucsc.edu/~mclapham/Rtips/apply_sapply.htm
