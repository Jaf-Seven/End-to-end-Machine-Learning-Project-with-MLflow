import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path
import dagshub
from mlProject import logger


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        # Step 1: Initialize MLflow with same experiment as main.py
        dagshub.init(
            repo_owner='mohamedjaafar2297',
            repo_name='End-to-end-Machine-Learning-Project-with-MLflow',
            mlflow=True
        )
        mlflow.set_tracking_uri(
            "https://dagshub.com/mohamedjaafar2297/End-to-end-Machine-Learning-Project-with-MLflow.mlflow"
        )
        mlflow.set_experiment("ML_Pipeline_Experiment_V2")

        logger.info("DagsHub tracking initialized successfully.")

        # Step 2: Load model and test data
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Step 3: Start nested MLflow run (under main.py run)
        with mlflow.start_run(run_name="Model_Evaluation", nested=True):
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Step 4: Log params + metrics
            if hasattr(self.config, "all_params"):
                mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            logger.info(f"✅ Metrics logged to MLflow: RMSE={rmse}, MAE={mae}, R2={r2}")

            # Step 5: Log model artifact
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")

        logger.info("✅ Model Evaluation logged successfully to MLflow.")
