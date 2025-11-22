from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.enitity.config_entity import DataIngestionConfig,TrainingPipelineConfig
# from networksecurity.constant.training_pipeline import 
try:
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    artifact = data_ingestion.initiate_data_ingestion()
    print("artifact",artifact)
except Exception as e:
    print(e)
# a.initiate_data_ingestion(c)