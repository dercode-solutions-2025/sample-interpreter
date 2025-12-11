def tokenize(code):
	code = code.strip()
	tokens = []
	if ',' in code:
		# expect a one liner: no blocks
		code = code.strip().split(',')
		tokens.append(code)
		if func == "print":
			# I don't really care if there are quotes or not: it doesn't stop the execution so...
			# I should handle printing and input - basic functions - right here because it's easier
			print(arg)
		if func == "input":
			input(arg)
	if '=' in code:
		code = code.split('=')
		tokens.append(code)
		# x = 10 would return ['x', '10'']
	if 'func' in code:
		# expects a function, such as: func myfunc arg1 arg2 | print arg1 + arg2
		code = code.split('|')
		definition = code[0]
		definition.split()
		vals = code[1]
		vals.split()
		tokens.append(definition)
		tokens.append(vals)
	return tokensdef
