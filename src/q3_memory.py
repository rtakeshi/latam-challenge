from typing import List, Tuple
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType
from pyspark.sql.functions import regexp_extract, collect_list, explode, count

STAGING_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("content", StringType(), True),
    StructField("date", DateType(), True) 
])


def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    spark = SparkSession.builder.appName("FarmersProtestTweets").getOrCreate()

    df = spark.read.option('delimiter', '~').option('header', True).option('multiline', True).schema(STAGING_SCHEMA).csv(file_path)


    # Tweet mention regex pattern
    mention_pattern = r"(@\w+)"

    # Extracting all strings with mention pattern
    mentions_df = df.select("content", regexp_extract(df["content"], mention_pattern, 1).alias("mention"))

    # Removing all empty mentions
    mentions_df = mentions_df.filter(mentions_df["mention"] != "")

    # Collecting all mentions as an array
    mentions_df = mentions_df.groupBy("content").agg(collect_list("mention").alias("mentions"))

    # DataFrame containing all user mentions
    user_mentions = mentions_df.select("content", explode(mentions_df["mentions"]).alias("mention"))

    # Count and group by user mentions
    mention_counts = user_mentions.groupBy("mention").agg(count("mention").alias("count"))

    # Ordering by mentions count and mention username for tie edge case
    sorted_mentions = mention_counts.orderBy(mention_counts["count"].desc(), mention_counts["mention"]).limit(10)

    result_collection = sorted_mentions.collect()

    #Creating result list of tupples
    result = []
    for row in result_collection:
        result.append((row['mention'], row['count']))


    return result