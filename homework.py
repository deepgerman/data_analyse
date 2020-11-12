f=open('salesdata.csv')
s=f.readlines()
'''print(len(s)-1)
data=s[0].split(',')
mean=[]
total_product_sale=[]
#for i in range()
total=0
median=[]
for i in range(1,len(s)):
    data=s[i].split(',')
    for j in range(1,53):
        total=total+int(data[j])
        if j==26:
           median.append(int(data[j])) #median           
    total_product_sale.append(total)
    total=0
for i in total_product_sale:
    mean.append(round(i/52,3))#mean
#highest average product
max(mean)#highest selling product
sale=0
'''
for i in range(1,52):
    i=i.split()
    




