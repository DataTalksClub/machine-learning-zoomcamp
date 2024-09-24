
## 2.2 Data preparation

<a href="https://www.youtube.com/watch?v=Kd74oR4QWGM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=13"><img src="images/thumbnail-2-02.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-2-slides)


## Notes

**Pandas attributes and methods:** 

* `pd.read_csv(<file_path_string>)` -> read csv files 
* `df.head()` -> take a look of the dataframe 
* `df.columns` -> retrieve colum names of a dataframe 
* `df.columns.str.lower()` -> lowercase all the letters 
* `df.columns.str.replace(' ', '_')` -> replace the space separator 
* `df.dtypes` -> retrieve data types of all features 
* `df.index` -> retrieve indices of a dataframe

The entire code of this project is available in [this jupyter notebook](notebook.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/18/ml-zoomcamp-2023-machine-learning-for-regression-part-1/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 2: Machine Learning for Regression](./)
* Previous: [Car price prediction project](01-car-price-intro.md)
* Next: [Exploratory data analysis](03-eda.md)
