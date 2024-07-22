import logging
import os
import sys

from common import data_transformations, get_spark_session, write_mariadb
from delta.tables import DeltaTable

# spark session
spark = get_spark_session(
    "ETL", "thrift://hive:9083", "http://minio:9000", "spark", "spark12345"
)
# Set log4j
spark.sparkContext.setLogLevel("ERROR")
log4jLogger = spark._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger("LOGGER")
logger.setLevel(log4jLogger.Level.INFO)


def insert_data(
    input_path="s3a://datalake/bitcoin_newdata.csv",
    output_path="s3a://datalake/deltatables/bitcoin/",
    **kwargs
):

    sdf = (
        spark.read.format("com.databricks.spark.csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ",")
        .option("mode", "DROPMALFORMED")
        .load(input_path)
    )

    sdf = data_transformations(sdf)
    sdf.printSchema()
    sdf.show()

    delta_table = DeltaTable.forPath(spark, output_path)

    # (delta_table.alias("t1").merge(
    #     sdf.alias("t2"),
    #     "t1.timestamp = t2.timestamp")
    #     .whenMatched().updateAll()
    #     .whenNotMatched().insertAll()
    #     .execute())

    (
        delta_table.alias("t1")
        .merge(sdf.alias("t2"), "t1.timestamp = t2.timestamp")
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )

    # write_mariadb(sdf, "mariadb", "root", "root", "dwh", "main_events")

    spark.stop()

    return "Done"


if __name__ == "__main__":

    input_path = str(sys.argv[1])
    output_path = str(sys.argv[2])

    insert_data(input_path, output_path)
