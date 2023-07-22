# Databricks notebook source
dbutils.fs.mkdirs('/mnt/dados')

# COMMAND ----------

dbutils.fs.ls('/mnt/dados/')

# COMMAND ----------

CLIENT_ID_STORAGE = ''
TENANT_ID_STORAGE = ''
SECRET_VALUE = ''

# COMMAND ----------


configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": CLIENT_ID_STORAGE,
          "fs.azure.account.oauth2.client.secret": SECRET_VALUE,
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/"+ TENANT_ID_STORAGE + "/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://<name_container>@<application-registration>.dfs.core.windows.net/",
  mount_point = "<mount_created>",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/dados/inbound')

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


