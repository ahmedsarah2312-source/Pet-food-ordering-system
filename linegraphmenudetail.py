import numpy as np
import mysql.connector as m
import matplotlib.pyplot as plt

#Fetching data from mysql. 
Mydb=m.connect(host='localhost',user='root',password='sa123',database='ofos')

mycursor=Mydb.cursor()

mycursor.execute('select item_name , price FROM menu')

result=mycursor.fetchall

item_name=[]
price=[]

for i in mycursor:
    item_name.append(i[0])
    price.append(i[1])
print("item",item_name)
print("price",price)

plt.xlabel('Item')
plt.ylabel('cost')
plt.title('Menu detail')
plt.plot (item_name,price)
plt.show()
