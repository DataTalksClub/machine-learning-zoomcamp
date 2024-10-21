# 4.3 Confusion table

[![ML Zoomcamp 4.3 - Confusion Table](./images/thumbnail-4-03.jpg)](https://www.youtube.com/watch?v=Jt2dDLSlBng&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR "Link to YouTube: ML Zoomcamp 4.3 - Confusion Table")

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-4-evaluation-metrics-for-classification) empty?

## Notes

Confusion table is a way of measuring different types of errors and correct decisions that binary classifiers can make. Considering this information, it is possible to evaluate the quality of the model by different strategies.

When comes to a prediction of an LR model, each falls into one of four different categories:

* Prediction is that the customer WILL churn. This is known as the **Positive class**
  * And Customer actually churned - Known as a **True Positive (TP)**
  * But Customer actually did not churn - Known as a **False Positive (FP)**
* Prediction is that the customer WILL NOT churn' - This is known as the **Negative class**
  * Customer did not churn - **True Negative (TN)**
  * Customer churned - **False Negative (FN)**

`Confusion Table` is a way to summarize the above results in a tabular format, as shown below:

<table>
  <tr>
    <th></th>
    <th></th>
    <th colspan="2" style="text-align: center;">Predictions</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Negative</td>
    <td>Positive</td>
  </tr>
  <tr>
    <td rowspan="2">Actual</td>
    <td>Negative</td>
    <td style="text-align: center;">TN</td>
    <td style="text-align: center;">FP</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td style="text-align: center;">FN</td>
    <td style="text-align: center;">TP</td>
  </tr>
</table>

![confusion_matrix.png](./images/confusion_matrix.png)

The **accuracy** corresponds to the sum of TN and TP divided by the total of observations.

The code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/04-evaluation/notebook.ipynb).

Add notes from the video (PRs are welcome)

|⚠️|The notes are written by the community.<br>If you see an error here, please create a PR with a fix.|
|---|:-:|

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/04/ml-zoomcamp-2023-evaluation-metrics-for-classification-part-3/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 4: Evaluation Metrics for Classification](./)
* Previous: [Accuracy and dummy model](02-accuracy.md)
* Next: [Precision and Recall](04-precision-recall.md)
