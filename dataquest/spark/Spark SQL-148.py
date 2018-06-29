## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

query = "select age from census2010"
sqlCtx.sql(query).show()

## 4. Filtering ##

query = 'select males, females from census2010 where age > 5 and age <15'
sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query = 'select males, females from census2010'
sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

census1980 =sqlCtx.read.json("census_1980.json")
df.registerTempTable('census1980')

census1990 =sqlCtx.read.json("census_1990.json")
df.registerTempTable('census1990')

census2000 =sqlCtx.read.json("census_2000.json")
df.registerTempTable('census2000')

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = 'select c.total,i.total from census2010 c  inner join  census2000 i on i.age=c.age'
sqlCtx.sql(query).show()

## 8. SQL Functions ##

query = """
        select SUM(census2010.total),SUM(census2000.total),SUM(census1990.total) 
        from census2010 
        inner join  census2000 on
        census2010.age = census2000.age
        inner join  census1990 on
        census2010.age = census1990.age

"""
sqlCtx.sql(query).show()