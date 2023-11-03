from typing import List, Tuple
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, explode, count, col
from pyspark.sql.types import StructType, StructField, ArrayType, StringType, DateType

from emoji_utils import extract_emojis


STAGING_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("content", StringType(), True),
    StructField("date", DateType(), True) 
])

def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    spark = SparkSession.builder.appName("FarmersProtestTweets").getOrCreate()

    df = spark.read.option('delimiter', '~').option('header', True).option('multiline', True).schema(STAGING_SCHEMA).csv(file_path)
    #Define UDF
    extract_emojis_udf = udf(extract_emojis, ArrayType(StringType()))

    
    #Create a new DF with exploded Array of content using UDF to find Emojis
    emoji_df = df.withColumn('emoji', explode(extract_emojis_udf(df['content'])))

    #Count and ordering by usage and emoji alphabetical order for tie edge case
    emoji_counts = emoji_df.groupBy('emoji').agg(count('emoji').alias('count')).orderBy(col("count").desc(), col('emoji')).limit(10)

    emoji_counts.show(5)

    result_collection = emoji_counts.collect()

    #Creating result list of tupples
    result = []
    for row in result_collection:
        result.append((row['emoji'], row['count']))


    return result