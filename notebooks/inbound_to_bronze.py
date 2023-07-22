# Databricks notebook source
dbutils.fs.ls('/mnt/dados/inbound')

# COMMAND ----------

# https://docs.databricks.com/dbfs/mounts.html#mount-adls-gen2-or-blob-storage-with-absf

# COMMAND ----------

path = 'dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json'

# COMMAND ----------

dados = spark.read.json(path)

display(dados)

# COMMAND ----------

dados_ads = dados.drop('imagens','usuario')
display(dados_ads)

# COMMAND ----------

dados_ads = dados_ads.withColumn('id', dados_ads['anuncio']['id'])
display(dados_ads)

# COMMAND ----------

path_destiny = 'dbfs:/mnt/dados/bronze/dataset_imoveis'
dados_ads.write.mode('overwrite').format('delta').save(path_destiny)

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/mnt/dados/bronze/dataset_imoveis/'))

# COMMAND ----------


