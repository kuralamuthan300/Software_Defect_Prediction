from software_defect_prediction import logger
from software_defect_prediction.components.data_transformation import Data_Transformation
from software_defect_prediction.pipeline.stage_01_dataingestion_pipeline import DataIngestionPipeline
from software_defect_prediction.pipeline.stage_02_datavalidation_pipeline import DataValidationPipeline
from software_defect_prediction.pipeline.stage_03_datatransformation_pipeline import DataTransformationPipeline


dataingestion_pipeline = DataIngestionPipeline()
dataingestion_pipeline.main()

datavalidation_pipeline = DataValidationPipeline()
datavalidation_pipeline.main()

datatransformation_pipeline = DataTransformationPipeline()
datatransformation_pipeline.main()
