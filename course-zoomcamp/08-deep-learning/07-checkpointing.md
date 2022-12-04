## 8.7 Checkpointing

<a href="https://www.youtube.com/watch?v=NRpGUx0o3Ps&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-07.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-8-neural-networks-and-deep-learning-250592316)


`ModelCheckpoint` callback is used with training the model to save a model or weights in a checkpoint file at some interval, so the model or weights can be loaded later to continue the training from the state saved or to use for deployment.

**Classes, function, and attributes**:

- `keras.callbacks.ModelCheckpoint`: ModelCheckpoint class from keras callbacks api
- `filepath`: path to save the model file
- `monitor`: the metric name to monitor
- `save_best_only`: only save when the model is considered the best according to the metric provided in `monitor`
- `model`: overwrite the save file based on either maximum or the minimum scores according the metric provided in `monitor`

## Notes

Add notes from the video (PRs are welcome)

* checkpointing saves the model after each training iteration
* checkpoint conditions may include reaching the best performance
* keras callbacks

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
* [Session 8: Neural Networks and Deep Learning](./)
* Previous: [Adjusting the learning rate](06-learning-rate.md)
* Next: [Adding more layers](08-more-layers.md)
