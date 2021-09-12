def linearSearch(arr, key):
	for i, val in enumerate(arr):
		if val == key:
			return i
	return -1 

def binarySearch(arr, key):
	start = 0
	end = len(arr)-1
	comp = 0
	while start<=end:
		comp += 1
		mid = (start + end)//2
		if arr[mid] == key:
			print("No of Comparisions :",comp)
			return mid
		elif arr[mid]>key:
			end = mid-1
		else :
			start = mid+1
	print("No of Comparisions :",comp)
	return -1
