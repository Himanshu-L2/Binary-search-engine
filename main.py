num_list = int(input('Please enter the numbers of items to be in the list : '))
l1=[]

for i in range (0,num_list):
    li = int(input('Please enter the liest item number ' + str(i+1) +' :'))
    l1.append(li)

src = int(input('Please emter the number to be searched.'))
flag = 0
desk = 0
while (flag != 1) or (desk != 1):
    l1.sort()
    print(l1)
    for i in range (2,num_list,2):
        if (num_list%i==0):
            flag = 1
            break
    if(flag==1):
        print('Even')
        break
    if(flag!=1):
        desk = 1
        print('Odd')
        break
    while():
