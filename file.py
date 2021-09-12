
from algorithms import *

arr = list(map(int,input("Enter list as space seperated elements : ").split()))

key = int(input("Enter search key : "))

ans = binarySearch(arr, key)

print("Found at : ", ans) if ans!=-1 else print("Not found")