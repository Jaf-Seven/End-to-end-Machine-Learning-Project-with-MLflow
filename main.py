from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline    
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline   
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import sys

sys.stdout.reconfigure(encoding='utf-8')

import dagshub
import mlflow

# ==================== MLflow + DagsHub Setup ====================
dagshub.init(
    repo_owner='mohamedjaafar2297',
    repo_name='End-to-end-Machine-Learning-Project-with-MLflow',
    mlflow=True
)
mlflow.set_tracking_uri("https://dagshub.com/mohamedjaafar2297/End-to-end-Machine-Learning-Project-with-MLflow.mlflow")

# ✅ Use ONE consistent experiment for all runs
mlflow.set_experiment("ML_Pipeline_Experiment_v2")

# ================================================================

with mlflow.start_run(run_name="Main_Pipeline_Run"):
    try:
        ## ============ STAGE 1: DATA INGESTION ============ ##
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        DataIngestionTrainingPipeline().main()
        mlflow.log_param("stage_1", "Data Ingestion completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")

        ## ============ STAGE 2: DATA VALIDATION ============ ##
        STAGE_NAME = "Data Validation Stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        DataValidationTrainingPipeline().main()
        mlflow.log_param("stage_2", "Data Validation completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")

        ## ============ STAGE 3: DATA TRANSFORMATION ============ ##
        STAGE_NAME = "Data Transformation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        DataTransformationTrainingPipeline().main()
        mlflow.log_param("stage_3", "Data Transformation completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        ## ============ STAGE 4: MODEL TRAINING ============ ##
        STAGE_NAME = "Model training stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        ModelTrainerTrainingPipeline().main()
        mlflow.log_param("stage_4", "Model Training completed")
        mlflow.log_metric("training_status", 1)
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        ## ============ STAGE 5: MODEL EVALUATION ============ ##
        STAGE_NAME = "Model evaluation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        ModelEvaluationTrainingPipeline().main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
