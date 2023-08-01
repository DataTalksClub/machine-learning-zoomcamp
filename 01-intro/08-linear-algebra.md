## 1.8 Linear Algebra Refresher

<a href="https://www.youtube.com/watch?v=zZyKUeOR4Gg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=8"><img src="images/thumbnail-1-08.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-18-linear-algebra-refresher)


## Notes

### Linear Algebra Refresher
* Vector operations
* Multiplication
  * Vector-vector multiplication
  * Matrix-vector multiplication
  * Matrix-matrix multiplication
* Identity matrix
* Inverse

### Vector operations
~~~~python
u = np.array([2, 7, 5, 6])
v = np.array([3, 4, 8, 6])

# addition 
u + v

# subtraction 
u - v

# scalar multiplication 
2 * v
~~~~
### Multiplication

#####  Vector-vector multiplication

~~~~python
def vector_vector_multiplication(u, v):
    assert u.shape[0] == v.shape[0]
    
    n = u.shape[0]
    
    result = 0.0

    for i in range(n):
        result = result + u[i] * v[i]
    
    return result
~~~~

#####  Matrix-vector multiplication

~~~~python
def matrix_vector_multiplication(U, v):
    assert U.shape[1] == v.shape[0]
    
    num_rows = U.shape[0]
    
    result = np.zeros(num_rows)
    
    for i in range(num_rows):
        result[i] = vector_vector_multiplication(U[i], v)
    
    return result
~~~~

#####  Matrix-matrix multiplication

~~~~python
def matrix_matrix_multiplication(U, V):
    assert U.shape[1] == V.shape[0]
    
    num_rows = U.shape[0]
    num_cols = V.shape[1]
    
    result = np.zeros((num_rows, num_cols))
    
    for i in range(num_cols):
        vi = V[:, i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:, i] = Uvi
    
    return result
~~~~
### Identity matrix

~~~~python
I = np.eye(3)
~~~~
### Inverse
~~~~python
V = np.array([
    [1, 1, 2],
    [0, 0.5, 1], 
    [0, 2, 1],
])
inv = np.linalg.inv(V)
~~~~


Add notes here (PRs are welcome).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

## Links

* [Notebook from the video](notebooks/08-linear-algebra.ipynb)
* [Get a visual understanding of matrix multiplication](http://matrixmultiplication.xyz/)
* [Overview of matrix multiplication functions in python/numpy](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_1-intro_to_ML_linear_algebra/Notes_for_Chapter_1-Linear_Algebra.ipynb) 


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Lesson 1: Introduction to Machine Learning](./)
* Previous: [Introduction to NumPy](07-numpy.md)
* Next: [Introduction to Pandas](09-pandas.md)
