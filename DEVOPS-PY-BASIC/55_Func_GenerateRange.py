def generateRangeFromDefaultValues():
    a=list(range(10))
    print(a)

def generateRangeFromUserValue(a):
    for i in a:
        print(i,end="\t")

generateRangeFromDefaultValues()
generateRangeFromUserValue(range(10))
