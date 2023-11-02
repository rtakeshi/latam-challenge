from typing import List, Tuple
from datetime import datetime
from pyspark.sql import SparkSession



def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    spark = SparkSession.builder.appName("FarmersProtestTweets").getOrCreate()
    df = spark.read.option('delimiter', '~').option('header', True).option('multiline', True).csv(file_path)
  
    return df.show(5)