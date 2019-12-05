def split(word): 
    return [char for char in word]  


num = 124075
myStr = str(num)
myList = split(myStr)  
passCodes = []


for i in range(124075, 580769):
    myStr = str(i)
    myList = split(myStr)
    result = "Pass"
    equalFound = False
    firstFound = False
    myEquals=[]
    for j in range(1,6):
        x=int(myList.pop(0))
        y=int(myList.pop(0))
        if (y<x):
            result = "Fail"
        if (y==x):
            equalFound = True
            myEquals.append(y)
            if (myEquals.count(y) > 1):
                equalFound = False             
        myList.insert(0,y)

    if (result == 'Pass' and equalFound):
            passCodes.append(i)
print(passCodes)
print(len(passCodes))
 #   print(d6)

# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease

