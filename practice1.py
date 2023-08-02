'''
no1=int(input("Enter start number"))
no2=int(input("Enter end number"))

if no1>no2:
    temp = no1
    no1 = no2
    no2 = temp

for x in range(no1,no2):
    if x%2==0:
        print(x)
'''
'''
take letter from user and print following pattern
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaaaaaa
'''

for x in range (1,11):print('a'*x)
