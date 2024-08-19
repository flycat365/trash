# -*- coding: utf-8 -*-

import mariadb

conn = mariadb.connect(user="root", password="zh13079058260", host="192.168.100.129", port=3306, database="company")

cur = conn.cursor()
sql = "select * from emp where ename=%s"
cur.execute(sql, ('SCOTT',))
result = cur.fetchall()
print(result)

cur.close()
conn.close()