
## 7.2 Building Your Prediction Service with BentoML

<a href="https://www.youtube.com/watch?v=bWdEVlUw1CA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-02.jpg"></a>
 
## Links
* [Saving Models Documentation](https://docs.bentoml.org/en/latest/concepts/model.html)

## Notes

We need BentoML model store to save an XGBoost model instance in the following way:

```python
# Save xgboost model
bentoml.xgboost.save_model('credit_risk_model',
                            model,
                            custom_objects={'DictVectorizer': dv})
```

BentoML will generator a directory in the home directory where the model will be kept.

Once the model is saved, we can create a `service.py` file that will be used to define the BentoML service:

```python
import bentoml
from bentoml.io import JSON


# Pull the model as model reference (it pulls all the associate metadata of the model)
model_ref = bentoml.xgboost.get('credit_risk_model:latest')
# Call DictVectorizer object using model reference
dv = model_ref.custom_objects['DictVectorizer']
# Create the model runner (it can also scale the model separately)
model_runner = model_ref.to_runner()

# Create the service 'credit_risk_classifier' and pass the model
svc = bentoml.Service('credit_risk_classifier', runners=[model_runner])


# Define an endpoint on the BentoML service
@svc.api(input=JSON(), output=JSON()) # decorate endpoint as in json format for input and output
def classify(application_data):
    # transform data from client using dictvectorizer
    vector = dv.transform(application_data)
    # make predictions using 'runner.predict.run(input)' instead of 'model.predict'
    prediction = model_runner.predict.run(vector)
    
    result = prediction[0] # extract prediction from 1D array
    print('Prediction:', result)

    if result > 0.5:
        return {'Status': 'DECLINED'}
    elif result > 0.3:
        return {'Status': 'MAYBE'}
    else:
        return {'Status': 'APPROVED'}
```

Once the service and the endpoint is created we can run the app using the command: `bentoml serve service:svc`, where ***service*** is the script and ***svc*** is the service name.

*There are some key things to consider at the time of bentoml version 1.0.7*:

- The final model has to be trained without providing feature names in the `DMatrix` constructor to prevent "ValueError" while building the BentoML application.
- When running bento service instead of using `http://0.0.0.0:3000/`, use `http://localhost:3000/`.
- On Windows systems `bentoml serve service:svc --reload` is not working. The issue has been added [here](https://github.com/bentoml/BentoML/issues/3111).

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

## Additional Issue Support
* Thanks for watching! Depending on your local setup, we do find issues from time to time. If you run into anything strange
we have a big community of BentoML users who would be happy to receive issue feedback: 
[BentoML slack community](https://l.bentoml.com/join-slack-mlzoomcamp). And if you're around shoot me a direct
message and say hi! 😃 

~Tim

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 7: Production-Ready Machine Learning (Bento ML)](./)
* Previous: [Intro/Session Overview](01-intro.md)
* Next: [Deploying Your Prediction Service](03-deploy-bento-service.md)