"""
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Mysparkapp").getOrCreate()
"""
"""Pandas"""
"""import pandas as pd

# Reading a CSV file from your local Windows directory
file_path = "C:/Users/selvi/Downloads/practice_retail_data.csv"
df = pd.read_csv(file_path)

# Preview the data
#print(df.head())
print(df.tail(10))
print(df.info())"""

"""Pyspark"""
from pyspark.sql import SparkSession

# Initialize the Spark Session
spark = SparkSession.builder \
    .appName("FileReadingTest") \
    .getOrCreate()

# Reading a CSV file into a PySpark DataFrame
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("C:/Users/selvi/Downloads/practice_retail_data.csv")

# Show the first 5 rows



df.show(5)


#df.filter(col("region").isNull()).show()

