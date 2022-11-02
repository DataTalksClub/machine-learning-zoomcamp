
## 7.3 Deploying Your Prediction Service

<a href="https://www.youtube.com/watch?v=qpjLm_Lm4FA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-03.jpg"></a>
 
## Links
* [Building Bentos Documentation](https://docs.bentoml.org/en/latest/concepts/bento.html)

## Notes

In this section we are going to look at BentoML cli and what operations BentoML is performing behind the scenes.

We can get a list of saved model in the terminal using the commmand `bentoml models list`. This command shows all the saved models and their tags, module, size, and the time they were created at. For instance:

```bash
 Tag                           Module           Size        Creation Time
 credit_risk_model:l652ugcqk…  bentoml.xgboost  197.77 KiB  2022-10-20 08:29:54
```

We can use `bentoml models list -o json|yaml|table` to display the output in one of the given format.

Running the command `bentoml models get credit_risk_model:l652ugcqkgefhd7k` displays the information about the model which looks like:

```yaml
name: credit_risk_model
version: l652ugcqkgefhd7k
module: bentoml.xgboost
labels: {}
options:
  model_class: Booster
metadata: {}
context:
  framework_name: xgboost
  framework_versions:
    xgboost: 1.6.2
  bentoml_version: 1.0.7
  python_version: 3.10.6
signatures:
  predict:
    batchable: false
api_version: v2
creation_time: '2022-10-20T08:29:54.706593+00:00'
```

Important thing to note here is that the version of the XGBoost in the `framework_versions` has to be same as the model was trained with otherwise we might get inconsistent results. The BentoML pulls these dependencies automatically and generates this file for convenience.

The next we want to do is, creating the file `bentofile.yaml`:

```yaml
service: "service.py:svc" # Specify entrypoint and service name
labels: # Labels related to the project for reminder (the provided labels are just for example)
  owner: bentoml-team
  project: gallery
include:
- "*.py" # A pattern for matching which files to include in the bento build
python:
  packages: # Additional pip packages required by the service
    - xgboost
    - sklearn
```

Once we have our `service.py` and `bentofile.yaml` files ready we can build the bento by running the command `bentoml build`. It will look in the service.py file to get all models being used and into bentofile.yaml file to get all the dependencies and creates one single deployable directory for us. The output will look something like this:

```bash
Successfully built Bento(tag="credit_risk_classifier:kdelkqsqms4i2b6d")
```

We can look into this directory by locating `cd ~/bentoml/bentos/credit_risk_classifier/kdelkqsqms4i2b6d/` and the file structure may look like this:

```bash
.
├── README.md # readme file
├── apis
│   └── openapi.yaml # openapi file to enable Swagger UI
├── bento.yaml # bento file to bind everything together
├── env # environment related directory
│   ├── docker # auto generate dockerfile (also can be customized)
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   └── python # requirments for installation
│       ├── install.sh
│       ├── requirements.txt
│       └── version.txt
├── models # trained model(s)
│   └── credit_risk_model
│       ├── l652ugcqkgefhd7k
│       │   ├── custom_objects.pkl # custom objects (in our case DictVectorizer)
│       │   ├── model.yaml # model metadate
│       │   └── saved_model.ubj # saved model
│       └── latest
└── src
    └── service.py # bentoml service file for endpoint
```

The idea behind the structure like this is to provide standardized way that a machine learning service might required.

Now the last thing we need to do is to build the docker image. This can be done with `bentoml containerize credit_risk_classifier:kdelkqsqms4i2b6d`.

> Note: We need to have Docker installed before running this command.

Once the docker image is built successfully, we can run `docker run -it --rm -p 3000:3000 containerize credit_risk_classifier:kdelkqsqms4i2b6d` to see if everything is working as expected. We are exposing 3000 port to map with the service port which is also 3000 and this should take us to Swagger UI page again.

**Reference**:

- [Tutorial: Intro to BentoML](https://docs.bentoml.org/en/latest/tutorial.html)

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
* Previous: [Building Your Prediction Service with BentoML](02-build-bento-service.md)
* Next: [Sending, Receiving and Validating Data](04-validation.md)