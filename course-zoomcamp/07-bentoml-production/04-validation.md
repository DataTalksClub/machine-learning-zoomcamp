
## 7.4 Sending, Receiving and Validating Data

<a href="https://www.youtube.com/watch?v=zNYtXde0BCA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-04.jpg"></a>
 
## Links
* [Pydantic Documentation](https://pydantic-docs.helpmanual.io/usage/models/)
* [BentoML Data Types Documentation](https://docs.bentoml.org/en/latest/reference/api_io_descriptors.html)

## Instructor Clarifications
**Please remember pydantic is not included by BentoML**
It must be installed using ```pip install pydantic```

Also remember to include it in your bentofile.yaml as a dependency when building your bento

## Notes

Data validation is another great feature on BentoML that ensures the data transferation is valid and reliable. We can integrate Python library Pydatic with BentoML for this purpose.

Pydantic can be installed with `pip install pydantic`, after that we need to import the `BaseModel` class from the library and create our custom class for data validation:

```python
# Create pydantic base class to create data schema for validation
class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int
```

Our model is trained on 13 features of different data types and the BaseModel will ensure that we are always recieving them for the model prediction.

Next we need to implement pass the class in our bentoml service:

```python
# Pass pydantic class in the application
@svc.api(input=JSON(pydantic_model=CreditApplication), output=JSON()) # decorate endpoint as in json format for input and output
def classify(credit_application):
    # transform pydantic class to dict to extract key-value pairs 
    application = credit_application.dict()
    # transform data from client using dictvectorizer
    vector = dv.transform(application)
    # make predictions using 'runner.predict.run(input)' instead of 'model.predict'
    prediction = model_runner.predict.run(vector) 
```

Along the `JSON()`, BentoML uses various other descriptors in the input and output specification of the service api, for example, NumpyNdarray(), PandasDataFrame(), Text(), and many more.

**Reference**:

- [Pydantic Manual](https://pydantic-docs.helpmanual.io/)
- [BentoML API IO Descriptors](https://docs.bentoml.org/en/latest/reference/api_io_descriptors.html)

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
* Previous: [Deploying Your Prediction Service](03-deploy-bento-service.md)
* Next: [High-Performance Serving](05-high-performance.md)