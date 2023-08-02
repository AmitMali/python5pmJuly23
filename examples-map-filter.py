studetsMarks=[56,76,89,45,34,67,89,23,45,32,12,45,33,23]
def gracePass(mark):
    if mark >=32 and mark<35:
        return 35
    else:
        return mark

updatedStudetsMarks=list(map(gracePass,studetsMarks))

failedStudens= filter(lambda marks:marks<35,updatedStudetsMarks)
passedStudens= filter(lambda marks:marks>=35,updatedStudetsMarks)

print("Failed Students = ",list(failedStudens))
print("Passed Students = ",list(passedStudens))