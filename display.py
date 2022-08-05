# Databricks notebook source
# MAGIC %sql
# MAGIC select date, value, userType, kpiName
# MAGIC from prod_ds.user_kpis_per_customer -- another comment
# MAGIC where customerName like 'H&M%'
# MAGIC     and kpiName = "MAU" -- comment
# MAGIC order by date, userType

# COMMAND ----------


