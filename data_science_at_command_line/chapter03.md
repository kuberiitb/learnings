## Chapter 3- Obtaining Data

#### NOTE: We need to install [csvkit](https://csvkit.readthedocs.org/en/0.9.0/) to use codes in this chapter.
```sh
$ pip install csvkit --upgrade
```
if python is not installed, first install it
```sh
$ sudo apt-get install python-dev python-pip python-setuptools build-essential
$ pip install csvkit --upgrade
```

Before starting the chapter, let's revise some useful commands:
- **csvcut** selects given columns using column names
-  **csvlook** formats the csv output and make it readable
- **jq** formats the .json output and make it readable
    
### Converting Microsoft Excel Spreadsheets
```sh
cd ~/book/ch03
$ in2csv data/imdb-250.xlsx > data/imdb-250.csv
Title,title trim,Year,Rank,Rank (desc),Rating,New in 2011 from 2010?,2010 rank,Rank Difference,
Sherlock Jr. (1924),SherlockJr.(1924),1924,221,30,8,y,n/a,n/a,
His Girl Friday (1940),HisGirlFriday(1940),1940,250,1,8,y,n/a,n/a,
```

As you can see, CSV by default is not too readable. You can pipe the data to a tool called csvlook, which will nicely format the data into a table.
Before showing the table, we would like to select few columns using command csvcut so that it gets fitted in the terminal view.
```sh
$ csvcut data/imdb-250.csv -c Title,"title trim",Year,Rating|csvlook
|-------------------------------------------+------+--------|
| Title                                     | Year | Rating |
|-------------------------------------------+------+--------|
| Sherlock Jr. (1924)                       | 1924 | 8      |
| His Girl Friday (1940)                    | 1940 | 8      |
|-------------------------------------------+------+--------|
``` 

#### [Next Chapter](https://github.com/kuberiitb/learnings/blob/master/data_science_at_command_line/chapter04.md)
