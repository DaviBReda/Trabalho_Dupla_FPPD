from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower

spark = SparkSession.builder.appName("SimpleWordCount").getOrCreate()

data = [("Hello World",), ("Hello FPPD",), ("TRABALHO TESTE FPPD",)]
df = spark.createDataFrame(data, ["text"])

words = df.select(explode(split(col("text"), " ")).alias("word"))

words_lower = words.select(lower(col("word")).alias("word_lower"))

word_counts = words_lower.groupBy("word_lower").count()

word_counts.show()

spark.stop()
