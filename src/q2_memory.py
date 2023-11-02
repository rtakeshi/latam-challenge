from typing import List, Tuple
from datetime import datetime
from memory_profiler import profile
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, explode, split, count
from pyspark.sql.types import ArrayType


STAGING_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("content", StringType(), True),
    StructField("date", DateType(), True) 
])

def extract_emojis(text):
    return emoji.get_emoji_regexp().findall(text)

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    spark = SparkSession.builder.appName("FarmersProtestTweets").getOrCreate()
    df = spark.read.option('delimiter', '~').option('header', True).option('multiline', True).schema(STAGING_SCHEMA).csv(file_path)
    
    #Create a new DF with exploded Array of content using UDF to find Emojis
    emoji_df = df.withColumn('emoji', explode(extract_emojis_udf(df['content'])))

    #Count and ordering by usage and emoji alphabetical order for tie edge case
    emoji_counts = emoji_df.groupBy('emoji').agg(count('emoji').alias('count')).orderBy(col("count").desc(), col('emoji')).limit(10)

    result_collection = emoji_counts.collect()

    #Creating result list of tupples
    result = []
    for row in result_collection:
        result.append((row['emoji'], row['count']))


    return result