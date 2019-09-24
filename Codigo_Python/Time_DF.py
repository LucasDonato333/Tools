import time
import datetime
from pyspark.sql.functions import lit,unix_timestamp
timestamp = (datetime.datetime.fromtimestamp(time.time()) - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
timestamp
new_df = df.withColumn('time',unix_timestamp(lit(timestamp),'yyyy-MM-dd HH:mm:ss').cast("timestamp"))
new_df.show(truncate = False)