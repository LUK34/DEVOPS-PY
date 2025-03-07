a=102
b=0b1101
c=0xaf12
d=1.23
e=1.23-2.34j
f=True

print(a)
print(bin(b))
print(hex(c))
print(d)
print(e)
print(f)
print("--------------------------------------------------------")
print(a," ",bin(b)," ",hex(c)," ",d," ",e," ",f)
print("--------------------------------------------------------")
print(a,"\n",bin(b),"\n",hex(c),"\n",d,"\n",e,"\n",f)
print("--------------------------------------------------------")
print(a,"\t",bin(b),"\t",hex(c),"\t",d,"\t",e,"\t",f)
print("--------------------------------------------------------")
Name="Sagar"
age=26
location='Vizag'
maritalStatus=True
print("Name of the candidate is ",Name," his age is ",age," from ",location," and the marital status is ",maritalStatus)
print("--------------------------------------------------------")
print("String Formatter:")
print("Name of the candidate is %s his age is %s from %s and the marital status is %s"%(Name,age,location,maritalStatus))
print("--------------------------------------------------------")
print("format()")
print("My name = {}".format(Name))
print("my age = {}".format(age))
print("My location = {}".format(location))
print("My marital status = {}".format(maritalStatus))
print("My name = {} my age ={} my location={} my marital status={} ".format(Name,age,location,maritalStatus))
print("--------------------------------------------------------")
