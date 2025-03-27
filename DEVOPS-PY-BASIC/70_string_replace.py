data="python is hard to understand"

print("Before replace() is used:")
print("-> ",data)
print("-> id value -> ",id(data))
print("After replace() is used:")
data=data.replace("hard","easy")
print("-> ",data)
print("-> id value -> ",id(data))