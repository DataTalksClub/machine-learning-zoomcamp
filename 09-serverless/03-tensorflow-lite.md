
## 9.3 TensorFlow Lite

> Note: the materials in this unit are outdated.
> 
> Refer to the [ONNX Workshop](workshop/) for the up-to-date materials.

<a href="https://www.youtube.com/watch?v=OzZA4mSBE0Q&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-9-03.jpg"></a>
 
TensorFlow is a relatively large framework, with an unpacked size of approximately 1.7 GB. The size of such frameworks is an important consideration for several reasons:  

- **📜 Historical Constraints:** Previously, AWS Lambda imposed a limit of `50 MB` for package sizes. While Docker has since increased these limits to 10 GB, the size of the framework still plays a crucial role in certain scenarios.
- **⚡ Performance Issues with Large Images:** Large frameworks like TensorFlow result in increased storage costs, longer initialization times (e.g., for invoking a Lambda function), slower loading times, and a significantly larger RAM footprint.  

### Optimizing with TensorFlow Lite 🚀  
To address these challenges, TensorFlow Lite (TF-Lite) provides a lightweight alternative designed specifically for inference tasks (i.e., making predictions with `model.predict(X)`), excluding any other functionality such as training. To use TensorFlow Lite, the original TensorFlow model needs to be converted into the TF-Lite format. This process can significantly reduce model size and improve performance.  


## Notes

New URL for downloading the model:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5
```

Add notes from the video (PRs are welcome)

* tensorflow has a size of approximately 1.7 GB
* there are size limits of cloud services and docker container
* tensorflow lite is small in size and limited to using a model to make predictions (inference)
* convert tensorflow keras model to a tensorflow lite model

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/01/ml-zoomcamp-2023-serverless-part-2/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/02/ml-zoomcamp-2023-serverless-part-3/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 9: Serverless Deep Learning](./)
* Previous: [AWS Lambda](02-aws-lambda.md)
* Next: [Preparing the code for Lambda](04-preparing-code.md)
