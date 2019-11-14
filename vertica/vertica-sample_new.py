#!/usr/bin/env python

# ------- file: myplot.py ------
import vertica_python
import logging

import matplotlib.pyplot as plt
import numpy as np

# ------- create vertica connection ------
conn_info = {'host': '192.168.1.125',
             'port': 5433,
             'user': 'dbadmin',
             'password': 'password',
             'database': 'VMart',
             'log_level': logging.INFO,
             'log_path': 'training-vertica-python.log'}

connection = vertica_python.connect(**conn_info)

cur = connection.cursor()

cur.execute("SELECT sa.Deptno, sa.Empno, sa.Sal, ROUND(AVG(sa.Sal) OVER(PARTITION BY sa.Deptno), 2) AS Avg FROM training.salary sa")

# convert source to matplotlib 
data = np.array(cur.fetchall())

# get plot columns
EmpNo = data[:,1]
Sal = data[:,2].astype(np.float)
AVGSal = data[:,3].astype(np.float)

# plot data
plt.plot(EmpNo, Sal, 'bo-', label="Salary")
plt.plot(EmpNo, AVGSal, 'go-', label="AVG Salary")

for i, j in zip(EmpNo, Sal):
	plt.text(i, j, str(j))

for i, j in zip(EmpNo, AVGSal):
	plt.text(i, j, str(j))

# Place a legend to the right of this smaller subplot.
plt.legend(loc='upper left')
plt.title('AVG Analytics')

plt.show()