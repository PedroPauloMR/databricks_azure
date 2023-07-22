# Databricks notebook source
dbutils.fs.mkdirs('/mnt/dados')

# COMMAND ----------

dbutils.fs.ls('/mnt/dados/')

# COMMAND ----------

CLIENT_ID_STORAGE = '7f850b1e-8984-49cf-86bf-b42992ad6343'
TENANT_ID_STORAGE = '01d328a3-c1b5-4599-954c-0be1292fe001'
SECRET_VALUE = '1Zy8Q~6Pb2NLR2i6a9ka9K2afNZ93~oAp4Rx4cjH'

# COMMAND ----------


configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": CLIENT_ID_STORAGE,
          "fs.azure.account.oauth2.client.secret": SECRET_VALUE,
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/"+ TENANT_ID_STORAGE + "/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://imoveis@datalakealurapedro.dfs.core.windows.net/",
  mount_point = "/mnt/dados",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/dados/inbound')

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


