import mlflow
# - mlflow ui - do it in cmd to up mlflow ui
"""
if __name__ == "__main__":
    mlflow.set_experiment(experiment_name='exp_demo')    
    with mlflow.start_run(run_name='run_demo'):
        mlflow.log_param('b',2)
        for a in range(10):
            mlflow.log_metric('a',a)
"""            
mlflow.set_experiment(experiment_name='exp_demo1')
with mlflow.start_run(run_name='run_demo'):
    mlflow.log_param('b',2)
    for a in range(10):
        mlflow.log_metric('a',a)