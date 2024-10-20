# 3.1 Churn prediction project

<a href="https://www.youtube.com/watch?v=0Zw04wdeTQo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-3-01.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-3-machine-learning-for-classification) empty?

## Notes

The project aims to identify customers that are likely to churn or stop to using a service. Each customer has a score associated with the probability of churning. Considering this data, the company would send an email with discounts or other promotions to avoid churning.

The ML strategy applied to approach this problem is binary classification, which for one instance ($i^{th}$ customer), can be expressed as:

$$\large g\left(x_{i}\right) = y_{i}$$

In the formula, $y_i$ is the model's prediction and belongs to {0,1}, with 0 being the negative value or no churning, and 1 the positive value or churning. The output corresponds to the likelihood of churning.

In brief, the main idea behind this project is to build a model with historical data from customers and assign a score of the likelihood of churning.

For this project, we used a [Kaggle dataset](https://www.kaggle.com/blastchar/telco-customer-churn).

|⚠️|The notes are written by the community.<br>If you see an error here, please create a PR with a fix.|
|---|:-:|

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/25/ml-zoomcamp-2023-machine-learning-for-classification-part-1/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 3: Machine Learning for Classification](./)
* Next: [Data preparation](02-data-preparation.md)
