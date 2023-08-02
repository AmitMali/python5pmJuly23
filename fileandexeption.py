# try:
#     print(f'hello {name}')
# except:
#     print('variable not declare')
# print(f'hello {name}')
#
# num=10
# try:
#     print(num/0)
# except:
#     print("divident is zero, operation not allowed")

# with open('sample.txt') as myfile:
#     print(myfile.read())

# myfile=open('sample.txt')
# print(myfile.read())
# myfile.close()
students=['komal', 'ankita', 'mrudugandha', 'sakshi', 'shruti', 'mamta', 'naima', 'sakshi', 'mansi']
# course='Python'
# batchTime='5 PM'

# student=input("Enter Student Name")
# course=input("Enter Course")
# batchTime=input("Enter Batch Time hh:hh AM/PM format")

# try:
#     with open('students.csv','a') as studFile:
#         # studFile.write("Name,Course,Batch Time")
#         # studFile.write('\n')
#         # for stud in students:
#         #     studFile.write(f'{stud},{course},{batchTime}\n')
#         studFile.write(f'{student},{course},{batchTime}\n')
# except:
#     print('unable to write file')

# with open('students.txt','a') as studFile:
#     print(studFile.writelines(students))