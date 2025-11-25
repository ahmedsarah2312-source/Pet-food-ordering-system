import numpy as np
import mysql.connector as m
import matplotlib.pyplot as plt

#Fetching data from mysql. 
Mydb=m.connect(host='localhost',user='root',password='sa123',database='ofos')

mycursor=Mydb.cursor()

mycursor.execute('select payment_method ,amount FROM payment')

result=mycursor.fetchall

payment_method=[]
amount=[]

for i in mycursor:
    payment_method.append(i[0])
    amount.append(i[1])
print("Method",payment_method)
print("Amount",amount)

plt.xlabel('Method')
plt.ylabel('Amount')
plt.title('Online order')
plt.scatter (payment_method,amount)
plt.show()
