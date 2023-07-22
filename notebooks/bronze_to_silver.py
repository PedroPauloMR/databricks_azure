# Databricks notebook source
dbutils.fs.ls('dbfs:/mnt/dados/bronze/dataset_imoveis/')

# COMMAND ----------

path = 'dbfs:/mnt/dados/bronze/dataset_imoveis/'

# COMMAND ----------

dados = spark.read.format('delta').load(path)
display(dados)

# COMMAND ----------

display(dados.select('anuncio.*'))

# COMMAND ----------

display(dados.select('anuncio.*','anuncio.endereco.*'))

# COMMAND ----------

dados_detail = dados.select('anuncio.*','anuncio.endereco.*')
display(dados_detail)

# COMMAND ----------

dados_detail = dados_detail.drop('caracteristicas','endereco')
display(dados_detail)

# COMMAND ----------

path_destiny = 'dbfs:/mnt/dados/silver/dataset_imoveis/'

dados_detail.write.mode('overwrite').format('delta').save(path_destiny)

# COMMAND ----------

display(dbutils.fs.ls(path_destiny))

# COMMAND ----------


