from networksecurity.components.data_ingestion import DataIngestion,DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation,DataValidationArtifact
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.enitity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig
# from networksecurity.constant.training_pipeline import 
try:
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    data_validation_config = DataValidationConfig(training_pipeline_config)
    data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
    data_validation_artifact = data_validation.initiate_data_validation()
    data_transformation_config = DataTransformationConfig(training_pipeline_config=training_pipeline_config)
    data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
    data_transformation_artifact  = data_transformation.initiate_data_transformation()
    print("artifact",data_transformation_config)
except Exception as e:
    print(e)
# a.initiate_data_ingestion(c)