# ML Zoomcamp intro screenshot rollout: lessons 08–10

This report records every image reference in `08-linear-algebra.md`,
`09-pandas.md`, and `10-summary.md`. Exact code, formulas, commands, URLs,
axes, and numeric output use deterministic preparation. Bounded conceptual
diagrams in the summary use imagegen only after a deterministic crop.

## 08-linear-algebra

### 01 — vector operations

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-01-vector-operations.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x195+15+93`
- Invariants: `Vector operations`; `u = np.array([2, 4, 5, 6])`; `2 * u`; `array([ 4,  8, 10, 12])`; `v = np.array([1, 0, 0, 2])`; `u + v`; `array([3, 4, 5, 8])`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-01-vector-operations-cropped.png`
- Validation: accepted after visual inspection; code and values are unchanged; browser/recording chrome, face, and camera tile are absent.

### 02 — dot product

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-02-dot-product.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `470x267+15+32`
- Invariants: title `Vector-vector multiplication (dot product)`; vectors `u = [2, 4, 5, 6]` and `v = [1, 0, 0, 2]`; element-wise products `2·1`, `4·0`, `5·0`, `6·2`; sum relationship and arrows
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-02-dot-product-cropped.png`
- Validation: accepted after visual inspection; diagram labels and values are unchanged; face, camera tile, browser chrome, and cursor are absent.

### 03 — vector-vector implementation

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-03-vector-vector-implementation.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x213+15+100`
- Invariants: `def vector_vector_multiplication(u, v)`; shape assertion; loop `for i in range(n)`; accumulation `result = result + u[i] * v[i]`; return value; call and output `14.0`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-03-vector-vector-implementation-cropped.png`
- Validation: accepted after visual inspection; code and output remain exact; face, camera tile, browser chrome, and recording controls are absent.

### 04 — matrix-vector idea

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-04-matrix-vector-idea.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `490x285+0+32`
- Invariants: title `Matrix-vector multiplication`; matrix `U` with rows `[2, 4, 5, 6]`, `[1, 2, 1, 2]`, `[3, 1, 2, 1]`; vector `v = [1, 0.5, 2, 1]`; highlighted first row and arrow toward the vector
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-04-matrix-vector-idea-cropped.png`
- Validation: accepted after visual inspection; all matrix/vector values and relationship arrows are unchanged; face, camera tile, browser chrome, and controls are absent.

### 05 — matrix-vector implementation

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-05-matrix-vector-implementation.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x170+15+105`
- Invariants: visible implementation body with `num_rows`, `np.zeros(num_rows)`, row loop, `vector_vector_multiplication(U[i], v)`, return; test call `matrix_vector_multiplication(U, v)`; output `array([14.,  5.,  5.])`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-05-matrix-vector-implementation-cropped.png`
- Validation: accepted after visual inspection; visible code and numeric output are unchanged; browser/recording chrome, face, camera tile, next-cell pointer, and controls are absent.

### 06 — matrix-matrix implementation

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-06-matrix-matrix.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x205+15+95`
- Invariants: matrix-matrix result allocation; column loop; `vi = V[:, i]`; `matrix_vector_multiplication(U, vi)`; assignment to `result[:, i]`; test call and output matrix `[[14., 20., 13.], [5., 6., 5.], [5., 8.5, 9.]]`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-06-matrix-matrix-cropped.png`
- Validation: accepted after visual inspection; visible code and all numeric output are unchanged; browser/recording chrome, face, camera tile, and controls are absent.
