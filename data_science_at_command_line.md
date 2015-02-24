# [What I learnt from] Data Science at the command line
- github repo https://github.com/jeroenjanssens/data-science-at-the-command-line
- We will use only the important/public tools, not the ones specfic only to this book

## Chpter 2- Getting Started
### head
get top three lines
```sh
head -n 3 data/movies.txt or 
head -3 data/movies.txt
```

### splitting command on multiple lines
Sometimes we use commands and pipelines that are too long to fit on the page.
In that case, we can split a long command with either a backslash ( \ ) or a pipe symbol ( | )

```sh
$ echo 'Hello'\
> ' world' |
> wc
```
