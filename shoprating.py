import numpy as np
import mysql.connector as m
import matplotlib.pyplot as plt

#Fetching data from mysql. 
Mydb=m.connect(host='localhost',user='root',password='sa123',database='ofos')

mycursor=Mydb.cursor()

mycursor.execute('select petshop.name as name,rating.rating as rating from petshop inner join rating on petshop.petshop_id=rating.petshop_id')

result=mycursor.fetchall

name=[]
rating=[]

for i in mycursor:
 name.append(i[0])
 rating.append(i[1])
print("Name of the Shop",name)
print("Shop Rating",rating)

plt.xlabel('name')
plt.ylabel('Rating')
plt.title('Shop Rating')
plt.bar (name,rating)
plt.show()
