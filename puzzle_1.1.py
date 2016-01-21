def if_unique_chars_one(s):
	"""Determine if a string has all chars uniques"""
	if s:
		next_char = s[1]
		count = 1
		for a in s:
			if a != next_char:
				return False
			else:
				if count < len(s) - 1:
					count += 1
					next_char = s[count]
				else:
					return True
	else:
		return False

#TODO
def if_unique_chars_two(s):
	"""Determine if a string has all chars uniques"""
	pass

def main():
	"""Shell string and main"""
	print 'Introduce string: '
	s = raw_input()
	return if_unique_chars_one(s)

if __name__ == '__main__':
	print main()