
# A simple Python 3 program 
# to find three elements whose 
# sum is equal to zero 

# Prints all triplets in 
# arr[] with 0 sum 
def findTriplets(arr, m): 

	found = True
	for i in range(0, m-2): 
	
		for j in range(i+1, m-1): 
		
			for k in range(j+1, m): 
			
				if (arr[i] + arr[j] + arr[k] == 0): 
					print(arr[i], arr[j], arr[k]) 
					found = True
	
			
	# If no triplet with 0 sum 
	# found in array 
	if (found == False): 
		print(" not exist ") 

# Driver code 
arr = [0, -1, 2, -3, 1] 
m= len(arr) 
findTriplets(arr, m) 
	 
