from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import asc # asc para crescente e desc para decrescente.

sc = SparkContext('local')
spark = SparkSession(sc)

hostname='corretoradigital.chf01j8lttpe.us-east-2.rds.amazonaws.com'
jdbcPort="5432"
dbname='corretora_development'
username='admin_user'
password='Corretora2019'
jdbc_url = "jdbc:postgresql://{0}:{1}/{2}?user={3}&password={4}".format(hostname, jdbcPort, dbname,username,password)

connectionProperties = {
  "admin_user" : username,
  "Corretora2019" : password
}

'''
df = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "product") \
    .option("user", username) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .load()
'''

df = spark.read.format("jdbc").option("url", jdbc_url).option("dbtable", "product").option("user", username).option("password", password).option("driver", "org.postgresql.Driver").load()

df.filter(df['price'] < 500).sort(asc("price")).show()

### CONEXAO com JDBC ###
#spark-submit --jars /usr/share/java/postgresql-jdbc.jar job.py