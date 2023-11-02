from typing import List, Tuple
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType
from pyspark.sql.functions import col, count, row_number
from pyspark.sql.window import Window
from memory_profiler import profile


STAGING_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("content", StringType(), True),
    StructField("date", DateType(), True) 
])

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    pass