from typing import List, Tuple
from datetime import datetime
from pyspark.sql import SparkSession
from memory_profiler import profile

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    pass