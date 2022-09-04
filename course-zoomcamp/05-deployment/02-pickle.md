
## 5.2 Saving and loading the model

<a href="https://www.youtube.com/watch?v=EJpqZ7OlwFU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-02.jpg"></a>
 

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Notes
**In this session we'll cover the idea "How to use the model in future without training and evaluating the code"**
- To save the model we made before there is an option using the pickle library:
  - First install the library with the command ```pip install pickle-mixin``` if you don't have it.
  - After training the model and being the model ready for prediction process use this code to save the model for later.
  - ```
    import pickle
    with open('model.bin', 'wb') as f_out:
       pickle.dump((dcit_vectorizer, model), f_out)
    f_out.close() ## After opening any file it's nessecery to close it
      ```
  - In the code above we'll making a binary file named model.bin and writing the dict_vectorizer for one hot encoding and model as array in it. (We will save it as binary in case it wouldn't be readable by humans)
  - To be able to use the model in future without running the code, We need to open the binary file we saved before.
  - ```
    with open('mode.bin', 'rb') as f_in:  ## Note that never open a binary file you do not trust!
        dict_vectorizer, model = pickle.load(f_in)
    f_in.close()
     ```
   - With unpacking the model and the dict_vectorizer, We're able to again predict for new input values without training a new model by re-running the code.
  


Add notes from the video (PRs are welcome)


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
* [Session 5: Deploying Machine Learning Models](./)
* Previous: [Intro / Session overview](01-intro.md)
* Next: [Web services: introduction to Flask](03-flask-intro.md)
