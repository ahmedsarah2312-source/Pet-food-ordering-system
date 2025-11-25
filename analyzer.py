import numpy as np
import mysql.connector as m
import matplotlib.pyplot as plt

#Fetching data from mysql. 
Mydb=m.connect(host='localhost',user='root',password='sa123',database='ofos')

mycursor=Mydb.cursor()

mycursor.execute('select petshop.name as name1,sum(orders.order_total) as total from  petshop inner join orders on petshop.petshop_id=orders.petshop_id group by petshop.name')

result=mycursor.fetchall

name1=[]
total=[]

for i in mycursor:
 name1.append(i[0])
 total .append(i[1])
print("Name of the Shop",name1)
print("Total Purchase ",total )

plt.xlabel('Shop Name')
plt.ylabel('Total Amount')
plt.title('Total Purchase')
plt.plot(name1,total,linestyle='dashed',)
plt.show()
