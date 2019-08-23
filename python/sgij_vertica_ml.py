# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:23:18 2019

@description: Machine Learning using Vertica-ML
@author: Miguel Salinas Gancedo
@email: miguel@thingtrack.com
"""

import vertica_python
from vertica_ml_python import RVD

conn_info = {'host': '192.168.1.40',
             'port': 5433,
             'user': 'dbadmin',
             'password': 'password',
             'database': 'VMart',
             # default throw error on invalid UTF-8 results
             'unicode_error': 'strict',
             # SSL is disabled by default
             'ssl': False,
             # using server-side prepared statements is disabled by default
             'use_prepared_statements': False,
             # connection timeout is not enabled by default
             'connection_timeout': 5}

# simple connection, with manual close
connection = vertica_python.connect(**conn_info)

cur = connection.cursor()
cur.execute("SELECT age, pclass FROM training.titanic")

#for row in cur.iterate():
#    print(row)

titanic = RVD ('training.titanic', cur)

# We filter some values
titanic.filter ("pclass = 2")

#print(titanic.age)
print(titanic.columns)

titanic.bar(columns = ['age', 'pclass'])
   
# do things
connection.close()
