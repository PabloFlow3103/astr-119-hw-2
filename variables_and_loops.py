import numpy as np

def main():
	# defie your ints and floats
	a=0
	n=10
	x=119.0
	#declare 10 zeros for some reason
	y=np.zeros(n,dtype=float)
	#use loops to iterate
	for i in range(n):
		y[a] =2.0 * float(a) + 1.
	#sanother type of range based for loop just declaring we want to iterate through the variable
	for y_element in y:
		print(y_element)

if __name__ == "__main__":
	main()