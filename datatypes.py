#variables = values

"""
multiple
lines
commenting


data types
int
float
string
complex
bool


a=5
b=1.1
c="chargebee"
d=4+2j
e=True
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))


#colloction datatype
list
tuple
set
dict


#string operation

a="Geethaa"
print(a[0])
print(a[4])
print(a[-1])
print(a[-3])

#print (a[start index:stop index-1])

print(a[4:])
print(a[4:6])
print(a[:])

#print (a[start index:stop index-1:step])

print(a[::2])#alternate
print(a[::-1])#reverse


b="Bavani Kandhan"
print(b[9:6:-1]) #nak
print(b[-5:-8:-1])#nak
print(b[9:-8:-1])#nak
print(b[-5:6:-1])#nak


c="    Manideep Thalluru    "
print(c.strip())
print(c.lstrip())
print(c.rstrip())

a=["usha","manideep","abirami"]
print(a)
print(type(a))


b=("usha","manideep","abirami")
print(b)
print(type(b))

a[0]="Geethaa"
print(a)

c={1,1.1,"i"}
print(c)

d={1:"ravi",2:"raj"}
print(d)
print(d[1])


d={"veg":{"tomato":5,"brinjal":10},
   "fruits":{"apple":5,"banana":10}}
print(d)






password="admin@123"
limit=0
while(limit<3):
    entry=input("enter the password:")
    if (password==entry):
        print("password match")
    else:
        print("check your password")
        limit=limit+1
else:
    print("attempt limit reached ")





def abc():
    print("hello world")
    print("123")
abc()    
    

    
def add(a,b):
    print(a+b)
add (2,3)    


#object oriented progmming language

# classes,object

class first:
    a=78
    def method1(self):
        print("method1")
o1=first()
print(o1.a)
o1.a=80
print(o1.a)
o1.method1()


#inheritance concept


class second(first):
    b=45
    def method2(self):
        print("method2")
s1=second()
print(s1.b)
print(s1.a)

#print(o1.b) 'first' object has no attribute'b'
"""

#modules

#import cal

#cal.add(2,3)

#import cal as m
#m.sub(2,3)

#from cal import add
#add (4,5)

from cal import *
add(5,4)
sub(5,4)
mul(5,4)
div(5,4)























