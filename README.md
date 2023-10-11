[![CI](https://github.com/BobZhang26/Bob_PythonTemplate1/actions/workflows/cicd.yml/badge.svg)](https://github.com/BobZhang26/Bob_PythonTemplate1/actions/workflows/cicd.yml)
## Miniproject 5: Python Script interacting with SQL Database

## Summary
In this project, we are building a work pipeline that connect external data source to SQLlite database and execute some SQL queries in Python script. The SQL queries will include four basic operations that you can perform on a database or data repository, namely Create, Read, Update, Delete (CRUD operations). 
<img width="977" alt="Screenshot 2023-10-02 at 11 25 47" src="https://github.com/nogibjj/mini_project_5/assets/141781876/94018e4a-0a3c-418a-8900-3bd898cff266">

## Structure

* in `mylib`directory, `extract.py` extract raw data from online url source. `transform_load.py` transform the original raw data format from `.csv` to `.db` SQLite database and builds connection.
* `query.py` contains CRUD queries to perform the basic SQL executions.

## Test
<img width="964" alt="Screenshot 2023-10-11 at 12 27 57" src="https://github.com/nogibjj/mini_project_5/assets/141781876/6f5214d9-9d37-44a1-9bc8-79f53a89da44">

