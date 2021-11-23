Run mlflow ui in the directory where you have mlruns folder.

Many machine learning teams use [MLflow](https://www.mlflow.org) for experiment management, deployment, and as a model registry.  If you are already familiar with MLflow, you can integrate it with Evidently to **track the performance of production models**. 

In this case, you use **Evidently to calculate the metrics** and **MLflow to log the results**. You can then access the metrics in the MLflow interface. 



Refer the notebook.

MLFlow is for creating ML Pipelines, you can create experiments and do model registry too.

If we don’t want to use cloud services and want to utilize cost, MLFlow can be used.

Lets say,

we can use Jenkins instead of GCP Cloud Build for CI/CD.

we can also GitHub Actions for CI/CD, also for testing use cases on push.

Like locally, we can schedule the job and it triggers our MLFlow pipeline, or like on every git push, our Jenkins trigger our MLFlow, something like that.

we can use local repo instead GCP Cloud source Repo.

we can use local scheduler instead GCP Cloud Scheduler.



