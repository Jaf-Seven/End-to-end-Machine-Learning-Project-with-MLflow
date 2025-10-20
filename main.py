from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline    
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline   
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

# 🧩 New Imports for MLflow + DagsHub
import dagshub
import mlflow

# 🧠 Initialize MLflow tracking (DagsHub integration)
dagshub.init(
    repo_owner='mohamedjaafar2297',
    repo_name='End-to-end-Machine-Learning-Project-with-MLflow',
    mlflow=True
)
mlflow.set_tracking_uri("https://dagshub.com/mohamedjaafar2297/End-to-end-Machine-Learning-Project-with-MLflow.mlflow")

# Start MLflow experiment tracking
with mlflow.start_run( nested = True):

    ## ============ STAGE 1: DATA INGESTION ============ ##
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        mlflow.log_param("stage_1", "Data Ingestion completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        mlflow.log_param("stage_1_failed", str(e))
        raise e


    ## ============ STAGE 2: DATA VALIDATION ============ ##
    STAGE_NAME = "Data Validation Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        mlflow.log_param("stage_2", "Data Validation completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        mlflow.log_param("stage_2_failed", str(e))
        raise e


    ## ============ STAGE 3: DATA TRANSFORMATION ============ ##
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.main()
        mlflow.log_param("stage_3", "Data Transformation completed")
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        mlflow.log_param("stage_3_failed", str(e))
        raise e


    ## ============ STAGE 4: MODEL TRAINING ============ ##
    STAGE_NAME = "Model training stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        mlflow.log_param("stage_4", "Model Training completed")
        mlflow.log_metric("training_status", 1)
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        mlflow.log_param("stage_4_failed", str(e))
        mlflow.log_metric("training_status", 0)
        raise e


    STAGE_NAME = "Model evaluation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = ModelEvaluationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e