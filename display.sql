-- Databricks notebook source
-- MAGIC %sql
-- MAGIC select date, value, userType, kpiName
-- MAGIC from prod_ds.user_kpis_per_customer
-- MAGIC where customerName like 'H&M%'
-- MAGIC     and kpiName = "MAU"
-- MAGIC order by date, userType

-- COMMAND ----------


