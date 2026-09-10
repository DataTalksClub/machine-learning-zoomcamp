---
video_url: "https://www.youtube.com/watch?v=BNF1wjBwTQA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
code:
  - label: Notebook
    path: notebook.ipynb
---
# EDA

Now we explore the training data: we check for missing values, look at
the distribution of the target variable, and go through the numerical
and categorical columns. For EDA we use the full train set - train and
validation together - because we will also use it to compute feature
importance later.

First we reset its index, as we did for the other parts:

```python
df_full_train = df_full_train.reset_index(drop=True)
```

## Missing values

The check is simple - for every column we count the NaN values:

```python
df_full_train.isnull().sum()
```

```text
customerid          0
gender              0
seniorcitizen       0
partner             0
dependents          0
tenure              0
phoneservice        0
multiplelines       0
internetservice     0
onlinesecurity      0
onlinebackup        0
deviceprotection    0
techsupport         0
streamingtv         0
streamingmovies     0
contract            0
paperlessbilling    0
paymentmethod       0
monthlycharges      0
totalcharges        0
churn               0
dtype: int64
```

Everything is 0 - there are no missing values anywhere. We already took
care of the only column that had them, `totalcharges`, during data
preparation.

## Looking at the target: the churn rate

Next we look at the target variable - how many customers churned and
how many stayed:

```python
df_full_train.churn.value_counts(normalize=True)
```

```text
0    0.730032
1    0.269968
Name: churn, dtype: float64
```

About 73% of the customers stayed and 27% churned. The percentage of
ones - 0.269968, roughly 27% - is called the churn rate.

Because churn is now a column of ones and zeros, there is a shortcut
for computing it: the mean. The mean of a binary column is the number
of ones divided by the total number of rows, which is exactly the
churn rate:

```python
df_full_train.churn.mean()
```

```text
0.26996805111821087
```

Same number. This works for any binary variable: its mean is always the
fraction of ones.

## Numerical and categorical variables

Next we decide which columns are numerical and which are categorical.
Most columns in this dataset contain strings, so they are categorical.
Among the numeric ones, `seniorcitizen` is really a categorical
variable - it is just encoded as 0/1 - and `churn` is the target. That
leaves three numerical variables:

```python
numerical = ['tenure', 'monthlycharges', 'totalcharges']
```

And 16 categorical ones - everything except `customerid` (an
identifier, useless as a feature), the three numerical variables and
the target:

```python
categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]
```

It is a good idea to check how many unique values each categorical
variable has:

```python
df_full_train[categorical].nunique()
```

```text
gender              2
seniorcitizen       2
partner             2
dependents          2
phoneservice        2
multiplelines       3
internetservice     3
onlinesecurity      3
onlinebackup        3
deviceprotection    3
techsupport         3
streamingtv         3
streamingmovies     3
contract            3
paperlessbilling    2
paymentmethod       4
dtype: int64
```

Most variables have two or three values; `paymentmethod` has four - it
is the most diverse one. The number of categories matters later: it
determines how many columns we get after one-hot encoding.

## Materials

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification)

## Notes

The EDA for this project consisted of: 
* Checking missing values 
* Looking at the distribution of the target variable (churn)
* Looking at numerical and categorical variables 

**Functions and methods:** 

* `df.isnull().sum()` - returns the number of null values in the dataframe.  
* `df.x.value_counts()` returns the number of values for each category in x series. The `normalize=True` argument retrieves the percentage of each category. In this project, the mean of churn is equal to the churn rate obtained with the value_counts method. 
* `round(x, y)` - round an x number with y decimal places
* `df[x].nunique()` - returns the number of unique values in x series 

The entire code of this project is available in [this jupyter notebook](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/03-classification/notebook.ipynb). 

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/27/ml-zoomcamp-2023-machine-learning-for-classification-part-4/)
