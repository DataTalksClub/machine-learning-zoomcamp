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

### 07 — identity matrix

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-07-identity-matrix.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x193+15+135`
- Invariants: heading `Identity matrix`; `I = np.eye(3)`; `V.dot(I)`; returned matrix values `[[1., 1., 2.], [0., 0.5, 1.], [0., 2., 1.], [2., 1., 0.]]`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-07-identity-matrix-cropped.png`
- Validation: accepted after visual inspection; command and numeric output are unchanged; face, camera tile, browser chrome, and controls are absent.

### 08 — inverse

- Source: `cohorts/2026/01-intro/images/08-linear-algebra-08-inverse.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x205+15+100`
- Invariants: heading `Inverse`; `Vs = V[[0, 1, 2]]`; `Vs_inv = np.linalg.inv(Vs)`; inverse matrix values including `-0.66666667`, `0.66666667`, `1.33333333`, and `-0.33333333`
- Output: `cohorts/2026/01-intro/images/08-linear-algebra-08-inverse-cropped.png`
- Validation: accepted after visual inspection; commands and numeric output are unchanged; face, camera tile, browser chrome, and recording controls are absent.

## 09-pandas

### 01 — create DataFrame

- Source: `cohorts/2026/01-intro/images/09-pandas-01-create-dataframe.jpg`
- Disposition: deterministic crop, camera mask, and 2x Lanczos raster conversion
- Crop: `560x285+15+20`; camera mask in resized crop: `980,0` to `1119,72`
- Invariants: exact `data` rows and values; exact `columns` list; `df = pd.DataFrame(data, columns=columns)`; five-row DataFrame output and all column names/values
- Output: `cohorts/2026/01-intro/images/09-pandas-01-create-dataframe-cropped.png`
- Validation: accepted after visual inspection; code, headers, table values, and `NaN` are unchanged; face, camera tile, browser chrome, and scrollbar are absent.

### 02 — Series and columns

- Source: `cohorts/2026/01-intro/images/09-pandas-02-series-and-columns.jpg`
- Disposition: deterministic crop, cursor mask, and 2x Lanczos raster conversion
- Crop: `560x230+15+95`; cursor mask in resized crop: `325,238` to `356,267`
- Invariants: `Engine HP` Series values `138.0`, `NaN`, `218.0`, `194.0`, `261.0`; `df[['Make', 'Model', 'MSRP']]`; all five rows and three selected columns
- Output: `cohorts/2026/01-intro/images/09-pandas-02-series-and-columns-cropped.png`
- Validation: accepted after visual inspection; exact Series values, command, headers, and table values are unchanged; face, camera tile, browser chrome, and cursor are absent.

### 03 — iloc

- Source: `cohorts/2026/01-intro/images/09-pandas-03-iloc.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x245+15+100`
- Invariants: source table row labels `a`–`e`; command `df.iloc[[1, 2, 4]]`; selected rows `b`, `c`, `e`; all visible columns and values including `NaN`, `AUTOMATIC`, and `54990`
- Output: `cohorts/2026/01-intro/images/09-pandas-03-iloc-cropped.png`
- Validation: accepted after visual inspection; command, row selection, headers, and values are unchanged; face, camera tile, browser chrome, and controls are absent.

### 04 — filtering

- Source: `cohorts/2026/01-intro/images/09-pandas-04-filtering.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x205+15+100`
- Invariants: `df['Make'] == 'Nissan'`; two Nissan rows; combined condition `(df['Make'] == 'Nissan') & (df['Year'] >= 2015)`; all visible headers and values
- Output: `cohorts/2026/01-intro/images/09-pandas-04-filtering-cropped.png`
- Validation: accepted after visual inspection; boolean conditions, selected rows, headers, and values are unchanged; face, camera tile, browser chrome, and recording controls are absent.

### 05 — string operations

- Source: `cohorts/2026/01-intro/images/09-pandas-05-string-operations.jpg`
- Disposition: deterministic crop, editor-caret mask, and 2x Lanczos raster conversion
- Crop: `560x225+15+105`; caret mask in resized crop: `296,142` to `318,181`
- Invariants: normalized `Vehicle_Style` values `sedan`, `sedan`, `convertible`, `4dr_suv`, `pickup`; all five rows and visible DataFrame columns
- Output: `cohorts/2026/01-intro/images/09-pandas-05-string-operations-cropped.png`
- Validation: accepted after visual inspection; exact normalized values and table content are unchanged; face, camera tile, browser chrome, and editor caret are absent.

### 06 — describe

- Source: `cohorts/2026/01-intro/images/09-pandas-06-describe.jpg`
- Disposition: deterministic crop, editor-caret mask, and 2x Lanczos raster conversion
- Crop: `560x240+15+95`; caret mask in resized crop: `590,55` to `620,105`
- Invariants: command `df.describe().round()`; columns `Year`, `Engine HP`, `Engine Cylinders`, `MSRP`; all rows from `count` through `max` and exact statistics
- Output: `cohorts/2026/01-intro/images/09-pandas-06-describe-cropped.png`
- Validation: accepted after visual inspection; command, headers, and all summary values are unchanged; face, camera tile, browser chrome, and editor caret are absent.

### 07 — missing values

- Source: `cohorts/2026/01-intro/images/09-pandas-07-missing-values.jpg`
- Disposition: deterministic crop, output-caret mask, and 2x Lanczos raster conversion
- Crop: `560x205+15+100`; caret mask in resized crop: `278,165` to `305,197`
- Invariants: command `df.isnull().sum()`; all eight column names; `Engine HP` has `1`; every other count is `0`; `dtype: int64`
- Output: `cohorts/2026/01-intro/images/09-pandas-07-missing-values-cropped.png`
- Validation: accepted after visual inspection; command, column names, counts, and dtype are unchanged; face, camera tile, browser chrome, and cursor are absent.

### 08 — groupby

- Source: `cohorts/2026/01-intro/images/09-pandas-08-groupby.jpg`
- Disposition: deterministic crop and 2x Lanczos raster conversion
- Crop: `560x105+15+150`
- Invariants: `df.groupby('Transmission Type').MSRP.max()`; `AUTOMATIC 34450`; `MANUAL 54990`; `Name: MSRP, dtype: int64`
- Output: `cohorts/2026/01-intro/images/09-pandas-08-groupby-cropped.png`
- Validation: accepted after visual inspection; command and all grouped values are unchanged; face, camera tile, browser chrome, and next-cell border are absent.

## 10-summary

### 01 — features, target, and model

- Source: `cohorts/2026/01-intro/images/10-summary-01-features-target-model.jpg`
- Disposition: deterministic crop followed by built-in imagegen redraw
- Crop: `560x300+15+30`; camera/cursor mask in crop: `490,0` to `559,30` and `495,270` to `559,299`
- Invariants: title `1.1 Introduction to ML`; feature table with `Year`, `Make`, `Mileage`, `...`; visible rows and values; target table `Price` with `$1.1k`, `$0.6k`, `$23k`, `...`; `ML` and `Model` boxes; feature/target-to-ML and ML-to-Model arrows
- Output: `cohorts/2026/01-intro/images/10-summary-01-features-target-model-imagegen-pilot.png`
- Validation: accepted after visual inspection; all instructional labels, values, table relationships, and arrow directions are preserved; face, camera tile, handwriting, browser/recording chrome, cursor, and watermark are absent.
