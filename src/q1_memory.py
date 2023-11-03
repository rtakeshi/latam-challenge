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
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    spark = SparkSession.builder.appName("FarmersProtestTweets").getOrCreate()
    
    df = spark.read.option('delimiter', '~').option('header', True).option('multiline', True).schema(STAGING_SCHEMA).csv(file_path)
    
    #Top 10 dates with more content
    date_counts = df.groupBy('date').agg(count('content').alias('date_count'))
    date_counts = date_counts.orderBy(col('date_count').desc()).limit(10)

    #Joined DF filtering only top 10 dates by inner joining
    filtered_df = df.join(date_counts, 'date', 'inner')

    #Counting Users posts on top 10 dates
    user_counts_by_date = filtered_df.groupBy('date', 'date_count', 'username').agg(count('content').alias('user_count'))

    #Creating a window analytical function to filter top 1 username in each date
    #Edge case: if there is a tie, the username will follow alphabetical ordering
    window_spec = Window.partitionBy('date', 'date_count').orderBy(col('user_count').desc(), col('username'))

    #creating rank based in row_number ordering
    user_counts_by_date = user_counts_by_date.withColumn('rank', row_number().over(window_spec))

    #getting the Rank1 Username for each date
    top_users_by_date = user_counts_by_date.filter(user_counts_by_date['rank'] == 1)

    #ordering by content count by date
    top_users_by_date = top_users_by_date.select(['date', 'username']).orderBy(col('date_count').desc())

    # Collect dataframe results
    result_collection = top_users_by_date.collect()

    

    #Creating result list of tupples
    result = []
    for row in result_collection:
        result.append((row['date'], row['username']))


    return result