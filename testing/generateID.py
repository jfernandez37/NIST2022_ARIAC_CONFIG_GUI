import string
import random
from time import sleep
usedId=[]
SIZE=8
def generateOrderId():
    newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=SIZE))
    if newId in usedId:
        while newId in usedId:
            newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=SIZE))
    usedId.append(newId)
    return newId

if __name__=="__main__":
    allIds=[]
    for i in range(1000):
        newId=generateOrderId()
        if newId in allIds:
            print("Error. Function failed")
            quit()
        else:
            print(newId)