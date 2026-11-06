---
video_url: https://www.youtube.com/watch?v=Qa0-jYtRdbY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=7
code:
  - label: Notebook
    path: notebooks/07-numpy.ipynb
prev_url: 06-environment.md
next_url: 08-linear-algebra.md
---
# Introduction to NumPy

In this lesson we do a quick introduction to NumPy: the functions for creating arrays, multi-dimensional arrays, randomly generated arrays, element-wise operations, comparison operations and summarizing operations. These are the things we will use constantly throughout the course.

## Importing NumPy

You have already configured the environment and installed the libraries. Now we need to import NumPy:

```python
import numpy as np
```

We don't just import NumPy - we use an alias, `np`, so it's shorter to write. Instead of `numpy` we can now type `np`. This is a convention: in Python data science, this is how it's usually done.

## Creating arrays

The simplest function for creating arrays is `zeros`. It takes one argument - the size of the array - and creates an array of that size filled with zeros:

```python
>>> np.zeros(10)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

There is a similar function, `ones`, which fills the array with ones instead:

```python
>>> np.ones(10)
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```

And if you want to fill an array with some arbitrary number, use `full`: first you specify the size of the array, then the element to fill it with:

```python
>>> np.full(10, 2.5)
array([2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5])
```


If you have a Python list and want to create an array from it, use the `array` function and pass the list as the argument:

```python
>>> a = np.array([1, 2, 3, 5, 7, 12])
>>> a
array([ 1,  2,  3,  5,  7, 12])
```

To access an element of the array, use its index. Remember that indexing in Python starts with zero, so to access the element `3` we use index 2:

```python
>>> a[2]
3
```

And we can use the assignment operator to change it - say, replace 3 with 10:

```python
>>> a[2] = 10
>>> a
array([ 1,  2, 10,  5,  7, 12])
```


Two more useful functions for creating arrays. `arange` creates a range of numbers - it works like the Python function `range`, except instead of an iterator it gives us a NumPy array. The last element is exclusive:

```python
>>> np.arange(3, 10)
array([3, 4, 5, 6, 7, 8, 9])
```

`linspace` creates an array of a given size filled with numbers evenly spaced between the first and the second parameter:

```python
>>> np.linspace(0, 100, 11)
array([  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.])
```

The first element is 0, the last is 100, and everything in between is filled in. With 11 elements the steps are nice round numbers - 0, 10, 20, and so on.

## Multi-dimensional arrays

So far we created one-dimensional arrays. NumPy can also create two-dimensional and multi-dimensional arrays.

We use the same `zeros` function, but now we specify the dimensions of the array: the first number is the number of rows, the second is the number of columns:

```python
>>> np.zeros((5, 2))
array([[0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.]])
```

We can also create a two-dimensional array from a list of lists:

```python
>>> n = np.array([
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ])
```

Accessing elements works the same as with one-dimensional arrays, except we now have two indices - rows and columns are both indexed from zero. To access the element in row 0, column 1:

```python
>>> n[0, 1]
2
```

And again we can use the assignment operator - replace that 2 with 20:

```python
>>> n[0, 1] = 20
>>> n
array([[ 1, 20,  3],
       [ 4,  5,  6],
       [ 7,  8,  9]])
```


If we pass only one index, we get an entire row:

```python
>>> n[2]
array([7, 8, 9])
```

We can rewrite the entire row too - the only condition is that the dimensions match. Let's make the last row all ones:

```python
>>> n[2] = [1, 1, 1]
>>> n
array([[ 1, 20,  3],
       [ 4,  5,  6],
       [ 1,  1,  1]])
```

The same works for columns. To get a column we need to specify only the second index, but we cannot leave the first one empty - we put the colon operator there, meaning "all the rows":

```python
>>> n[:, 1]
array([20,  5,  1])
```

And we can assign to the column as well:

```python
>>> n[:, 2] = [0, 1, 2]
>>> n
array([[ 1, 20,  0],
       [ 4,  5,  1],
       [ 1,  1,  2]])
```


## Randomly generated arrays

NumPy can also generate arrays with random numbers. Let's generate a two-dimensional array with 5 rows and 2 columns:

```python
>>> np.random.rand(5, 2)
```

This gives us an array with random numbers between 0 and 1, sampled from the standard uniform distribution. Every time we execute this cell, we get different numbers.

If we want to make the results reproducible - so that when you run this code you get the same numbers as I do - we can fix the random seed. These numbers are not really random, they are pseudorandom: they are generated by an algorithm, and we can set the seed of this generator. Then the sequence of numbers produced on my computer and on your computer will be the same:

```python
>>> np.random.seed(2)
>>> 100 * np.random.rand(5, 2)
array([[43.59949021,  2.59262318],
       [54.96624779, 43.53223926],
       [42.03678021, 33.0334821 ],
       [20.4648634 , 61.92709664],
       [29.96546737, 26.68272751]])
```

Now every time we execute the cell, the results are the same, because we fixed the seed. (The exact numbers can vary a bit depending on the version of NumPy or the operating system, but in general the sequence should be the same.)


Here we multiplied everything by 100: instead of numbers between 0 and 1 we get numbers between 0 and 100. Why we can multiply an array by a number like this is explained below - it's an element-wise operation.

There are many different distributions we can sample from. To draw numbers from the standard normal distribution, we add an `n` to the name - `randn` stands for "random normal":

```python
>>> np.random.seed(2)
>>> np.random.randn(5, 2)
array([[-0.41675785, -0.05626683],
       [-2.1361961 ,  1.64027081],
       [-1.79343559, -0.84174737],
       [ 0.50288142, -1.24528809],
       [-1.05795222, -0.90900761]])
```

And for random integers there is `randint`, where we specify the lowest number, the highest number (exclusive - so this gives values between 0 and 99) and the size:

```python
>>> np.random.seed(2)
>>> np.random.randint(low=0, high=100, size=(5, 2))
array([[40, 15],
       [72, 22],
       [43, 82],
       [75,  7],
       [34, 49]])
```

## Element-wise operations

Now let's explain the multiplication we just did. Create an array first - `np.arange(5)` gives us numbers from 0 to 4:

```python
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
```

What if we want to add a number to all elements of this array? With NumPy we can just write:

```python
>>> a + 1
array([1, 2, 3, 4, 5])
```

If it was a usual Python list, we wouldn't be able to do this - we would need to write a loop and add the number to each element. NumPy makes it easier: `+ 1` adds one to each element. The same works for multiplication - every element gets multiplied by 2:

```python
>>> a * 2
array([0, 2, 4, 6, 8])
```


This is exactly what we did when we multiplied the random array by 100. And of course we can also divide, subtract, and do everything else we want. We can even chain operations:

```python
>>> b = (10 + (a * 2)) ** 2 / 100
>>> b
array([1.  , 1.44, 1.96, 2.56, 3.24])
```

First `a` is multiplied by 2, then 10 is added, then everything is squared and divided by 100. Every operation is applied element by element.

We can also combine two arrays. For `a` and the `b` we just created, we can compute the element-wise sum - for the first elements we compute the sum, for the second elements we compute the sum, and so on:

```python
>>> a + b
array([1.  , 2.44, 3.96, 5.56, 7.24])
```

Again we can multiply, divide, and chain these operations with anything we want.

## Comparison operations

Comparison operations are also element-wise. Let's check which elements of `a` are greater than or equal to 2:

```python
>>> a >= 2
array([False, False,  True,  True,  True])
```


The first element is less than 2, the second is less than 2, but 2 is greater than or equal to 2 - and the same is true for the rest.

We can also compare two arrays element by element - which elements of `a` are greater than the corresponding elements of `b`:

```python
>>> a > b
array([False, False,  True,  True,  True])
```

And we can use the boolean result to select the elements of `a` for which the condition is true:

```python
>>> a[a > b]
array([2, 3, 4])
```

The comparison returns a boolean array, and `a[a > b]` returns all the elements of `a` for which this condition is true. This way we can look at all the elements that satisfy a condition.

## Summarizing operations

Element-wise operations return another array. There is a different kind of operation that instead returns a single number - I call them summarizing operations.

For example, `min` returns the smallest number:

```python
>>> a.min()
0
```

`max` returns the maximal number, `sum` computes the sum of all elements (0 + 1 + 2 + 3 + 4 = 10), and `mean` computes the average:

```python
>>> a.sum()
10
>>> a.mean()
2.0
```


There is also the standard deviation, if you are interested:

```python
>>> a.std()
1.4142135623730951
```

All of this works for two-dimensional arrays too. For our matrix `n`, we can compute the sum of all its elements or find the minimal number:

```python
>>> n.min()
0
```

This was a quick introduction - there are a lot more useful functions in NumPy. Check the links below to read more: for example, how to find the minimal number in each row of a two-dimensional array, or how to sort.

In the next lesson we quickly go through the basics of linear algebra, where we will talk about multiplication operations.

## Materials

- [Notebook](notebooks/07-numpy.ipynb)
- [Introduction to NumPy](https://mlbookcamp.com/article/numpy)
- [NumPy Cheat sheet](https://www.datacamp.com/community/blog/python-numpy-cheat-sheet)
