# ans=lambda x,y:x*y
#
# print(ans(10,2))

data=[5, 12, 17, 18, 24, 32]

def evenOdd(x):
    return True if x%2==0 else False

result=filter(evenOdd,data)

# print(list(result))

# print(list(filter(lambda x:x>14,data)))

# def sqrof(x):
#     return x*x
# sqrlist=map(sqrof,data)

# for no in map(lambda x:x*x,data):print(no)

