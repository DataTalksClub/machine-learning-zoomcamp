
## 7.1 Intro/Session Overview

<a href="https://www.youtube.com/watch?v=2viqmJ_NpgE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-01.jpg"></a>
 
## Links
[Slides](https://www.slideshare.net/TimLiu72/71-ml-zoom-camp-intro-publicpptx)

## Notes

The goal of this session is to build and deploy an ML service, customize our service to fit our use case, and make our service production ready with the open-source library BentoML. For this, we'll be using the model we built in session 6.

What is production ready?

- `Scalability`: it is the ability to increase or decrease the resources of the application according to the user demands.
- `Operationally efficiency`: it is being able to maintain the service by reducing the time, efforts and resources as much as possible without compromising the high-quality.
- `Repeatability (CI/CD)`: to update or modify the service as we need without having to do everything again from the scratch.
- `Fexibility`: to make it easy to react and apply changes to the issues in the production.
- `Resiliency`: to ensure even if the service is completely broke we are still able to reverse to the previous stable version.
- `Easy to use`: all the required frameworks should be easy to use.

We first focus should always be on getting the service to the production and rest will come later.

What is a BentoML? A typical machine learning application has various components. For instance, code, model(s), data, dependencies, configuration, deployment logic, and many more. BentoML packages all these componments into one deployable unit with ease.

What we will be convering in session 7?

- Building a prediction service
- Deploying our prediction service
- Anatomy of a BentoML service
- Customizing Bentos
- BentoML Production Deployment
- High Perfromance serving
- Custom Runner / Framework

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
* Next: [Building Your Prediction Service with BentoML](02-build-bento-service.md)