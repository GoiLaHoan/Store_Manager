
f = open('./../../Data/Data_Sales.txt')
list1 = []
for line in f:
    text=line.replace('\n','').strip()
    line1=text.split()
    for i in line1:
        list1.append(i)
print(list1)

