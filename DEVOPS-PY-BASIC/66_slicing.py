print("----------------------------------------------------------")
string="Learning Python is easy"
print(string)
for i in range(len(string)):
    print("Index value= [",i,"] -> ",string[i])
print("----------------------------------------------------------")
print("SLICING:")
print("---------")
# start index < stop index: step must be +ve
print("start index < stop index: step must be +ve.")
print("no step value, default value =1 ->","string[0:8] ->", string[0:8]) #no step value, default value =1
print("no start value and no stop, default start=0, default step =1 ->","string[:8] ->",string[:8])  #no start value and no stop, default start=0, default step =1
print("no stop, default value = last character ->","string[0:] ->",string[0:]) #no stop, default value = last character
print("no start and no stop, default o start=0 and stop=last ->","string[:] ->",string[:]) #no start and no stop, default o start=0 and stop=last
print("-----------------------------------------------------------------------------------------")
print("string[0:11:2] ->", string[0:11:2]) #lann y
print("string[10::3] ->", string[10::3]) # start index=10,stop index=, step=3
print("string[:16:5] ->", string[:16:5]) # start index=,stop index=16, step=5
print("-----------------------------------------------------------------------------------------")
# start index > stop index: step must be -ve
print(string[10:0:-1])
# string reverse
print(string[::-1])
print("-----------------------------------------------------------------------------------------")