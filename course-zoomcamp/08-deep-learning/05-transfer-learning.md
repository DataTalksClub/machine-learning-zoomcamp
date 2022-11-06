## 8.5 Transfer learning

<a href="https://www.youtube.com/watch?v=WKHylqfNmq4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-05.jpg"></a>
 
[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-8-neural-networks-and-deep-learning-250592316)


## Notes

Add notes from the video (PRs are welcome)

* convolutional layers convert an image into a vector representation
* dense layers use vector representations to make predictions
* using a pretrained neural network
* imagenet has 1000 different classes
* a dense layer may be specific to a certain number of classes whereas the vector representation can be applied to another dataset
* reusing the vector representation from convolutional layers means transferring knowledge and the idea behind transfer learning
* train faster on smaller size images
* the batch size
* base model vs custom model
* bottom layers vs top layers in keras
* keras optimizers
* using the adam optimizer
* weights, learning rates
* eta in xgboost
* model loss
* categorical cross entropy
* changing accuracy during several training epochs
* overfitting

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
* Previous: [Convolutional neural networks](04-conv-neural-nets.md)
* Next: [Adjusting the learning rate](06-learning-rate.md)
