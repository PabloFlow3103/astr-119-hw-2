try:
	print(a)
except:
	print("a is not defined!")


try:
	print(a)
except NameError:
	print("a is still not defined!")

except:
	print("Something else is wrong.")

#not sure if i still had to do this
print(a)