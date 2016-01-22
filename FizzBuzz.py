def main():
	"""Print the numbers from 1 to 100. But if the number is multiple
	of 3 print Fizz instead of, and if it is multpiple of 5 print Buzz"""
	for x in range(1, 101):
		if x % 3 == 0:
			print 'Fizz'
		elif x % 5 == 0:
			print 'Buzz'
		else:
			print x

if __name__ == '__main__':
	main()