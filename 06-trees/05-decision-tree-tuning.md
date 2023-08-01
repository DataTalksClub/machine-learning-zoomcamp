## 6.5 Decision trees parameter tuning

<a href="https://www.youtube.com/watch?v=XJaxwH50Qok&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-6-05.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-6-decision-trees-and-ensemble-learning)


## Notes

In this lesson, we will discuss about different parameters present to control a Decision Tree (DT). Two features, `max_depth` and `min_samples_leaf` have a greater importance than other parameters. We will further see how we first tune `max_depth` parameter and then move to tuning other parameters will help. Finally, a dataframe is created with all possible combinations of `max_depth`, `min_sample_leaf` and the auc score corresponding to them. These results are visualized using a heatmap by pivoting the dataframe to easily determine the best possible `max_depth` and `min_samples_leaf` combination. Finally, the DT is retrained using the identified parameter combination. DT so trained is viewed as a tree diagram.     

Add notes from the video (PRs are welcome)

* iterating to find optimal parameter settings
* creating the heatmap with seaborn

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 6: Decision Trees and Ensemble Learning](./)
* Previous: [Decision tree learning algorithm](04-decision-tree-learning.md)
* Next: [Ensemble learning and random forest](06-random-forest.md)
