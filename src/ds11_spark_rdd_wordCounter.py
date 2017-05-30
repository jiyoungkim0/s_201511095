
# coding: utf-8

# In[1]:

import os 
import sys

os.environ["SPARK_HOME"]="C:\\Users\\ramy\\Downloads\\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))


# In[3]:

import pyspark
myConf = pyspark.SparkConf() 
spark = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:\\Users\\ramy\\SMU\\BigData\\Code\\s-201511095\\data').getOrCreate() 
filepath = os.path.join("data","ds_spark_wiki.txt")
myRdd = spark.sparkContext.textFile(filepath)
myRdd2=spark.sparkContext    .textFile(os.path.join(filepath))


# In[4]:

wc2=myRdd2    .flatMap(lambda x:x.split())    .map(lambda x:(x,1))    .reduceByKey(lambda x,y:x+y)    .map(lambda x:(x[1],x[0]))    .sortByKey(False)    .take(10)


# In[7]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt

count = map(lambda x: x[0], wc2)
word = map(lambda x: x[1], wc2)
plt.barh(range(len(count)), count, color = 'pink')
plt.yticks(range(len(count)), word)
plt.show()

