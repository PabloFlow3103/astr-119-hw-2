def main():
	#declare int & float
	i=0
	x=119.0

	#Range Based for loop
	for i in range(2):
		#simple consition
		if((i%2)==0):
			x += 3.
		else:
			x -= 5.
	#sturn x into a string
	s = "%3.2e" % x

	print(s)

if __name__ == "__main__":
	main()