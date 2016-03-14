###Summary of [pandas cookbook](http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/tree/v0.1/cookbook/)

importing the library

```python
import pandas as pd
import numpy as np
```

read the data

```python
train = pd.read_csv('data.csv')
```
####Ways to print samples of data
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
####Filter data based on value(s) of column(s)
```python
#subset data where Sex is male
train[train['Sex']=='male'][:10]
#subset data where Sex is male and print Age only
train[train['Sex']=='male']['Age']

#subset data where Sex is male and Age is not null
train[train['Sex']=='male']['Age'].notnull()
#subset data where Sex is male and print if Age is greater than 10(boolean) 
train[train['Sex']=='male']['Age'] > 10

#subset data on multiple columns 
train[(train['Sex']=='male') & (train['Age']>20)]
```

#### Groupby
```python
data.groupby('status').sum()
data.groupby('status').count()
data.groupby('status').agg({'content_id':'count', 'impressions': 'sum', 'clicks': 'sum', 'conversions':'sum', 'total_cost': 'sum'})
```

