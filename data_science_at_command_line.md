# [What I learnt from] Data Science at the command line
- github repo https://github.com/jeroenjanssens/data-science-at-the-command-line
- We will use only the important/public tools, not the ones specfic only to this book

## Chapter 2- Getting Started
### some useful commands:
- #### head
get top three lines
```sh
$ head -n 3 data/movies.txt or 
$ head -3 data/movies.txt
```
- #### seq
```sh
$ seq 3
1
2
3
```
- #### word count?
number of lines in the file
```sh
$wc -l
```
number of bytes(can be used for number of characters as well) in the file
```sh
$wc -c
```

### Passing files as input to commands
There are two ways to do this:
1. passing the file to the standard input of command
    ```sh
    $ myfile.txt wc -l
    ```
2. passing file as parameter of the command 
    ```sh
    $ wc -l myfile.txt
    ```


### Splitting command on multiple lines
Sometimes we use commands and pipelines that are too long to fit on the page.
In that case, we can split a long command with either a backslash ( \ ) or a pipe symbol ( | )

```sh
$ echo 'Hello'\
> ' world' |
> wc
```

### Redirecting Input and Output
>$ seq 10 > ten-numbers.txt

will save the output to ten-numbers.txt(if file doesn't exist, it will be created first, if exist, its content is replaced by the command output)

If you want to append the output to file, instead of replacing, use >> isntead of >.
>$ echo "line 1" > file.txt
>$ echo "line 2" >> file.txt

it will write first output to the file on first line and append the second command's output to the same file but below exsting content.
