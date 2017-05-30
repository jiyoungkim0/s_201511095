
# coding: utf-8

# In[3]:

import os 
import sys

os.environ["SPARK_HOME"]="C:\\Users\\ramy\\Downloads\\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))


# In[4]:

import pyspark
myConf = pyspark.SparkConf() 
spark = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:\\Users\\ramy\\SMU\\BigData\\Code\\s-201511095\\data').getOrCreate() 
filepath = os.path.join('data','overview.txt')
myRdd = spark.sparkContext.textFile(filepath)


# In[12]:

import os
lines=spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt"))
wc=lines.flatMap(lambda x: x.split(' '))


# In[13]:

from operator import add
wc = spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt"))    .flatMap(lambda x: x.split(' '))    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))    .reduceByKey(add)


# In[14]:

from operator import add
wc = spark.sparkContext.textFile("data/ds_spark_wiki.txt")    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())    .map(lambda x:x.split())    .map(lambda x:[(i,1) for i in x])


# In[15]:

documents = spark.sparkContext.textFile("data/ds_spark_wiki.txt")    .map(lambda line: line.split(" "))


# In[16]:

from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
tf = hashingTF.transform(documents)
tf.collect()

