import random
import string

a=int(input("enter length of password: "))
alphabet=string.ascii_letters
numbers=string.digits
special="!#$&"
#print(special)
#print(alphabet)
#print(numbers)
passw= alphabet+str(numbers)+special

print(passw)
ans=''
for i in range(a):
    ans+=random.choice(passw)
print(ans)