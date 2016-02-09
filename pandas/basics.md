###Summary of [pandas cookbook](http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/tree/v0.1/cookbook/)

importing the library

```python
import pandas as pd
```

read the data

```python
train = pd.read_csv('titanic_train.csv')
```
####ways to print samples of data
```python
#head
train.head()
#top N(say 5) rows
train[:5]
#selected column(one)
train['Name']
#selected column(one) N{top) rows
train['Name'][:5] #:5 implies start from start index and upto 5-1 i.e. 4 elements
#or
train[:5]['Name']
#selected columns(multiple)
train[['Survived','Name']]
#selected columns(multiple) N rows
train[['Survived','Name']][:5]
```
One way Frequency count of a column:
```python
train[['Survived']].value_counts() #by deafault sorted by descending frequency
train[['Survived']].value_counts()[:10] #for top 10 values
```


