from parser import vars
global tokens
global mode
def tokenize(code):
	code = code.strip()
	tokens = []
	if ',' in code:
		# expect a one liner: no blocks
		code = code.strip().split(',')
		tokens.append(code)
		if func == "print":
			if "$$" in code:
				code = code.replace("$$", "")
				print(vars.get(var))
			# I don't really care if there are quotes or not: it doesn't stop the execution so...
			# I should handle printing and input - basic functions - right here because it's easier
			print(arg)
		if func == "input":
			input(arg)
	if '=' in code:
		mode = "VAR"
		code = code.split('=')
		ast = (mode, code)
		tokens.append(ast)
		# x = 10 would return ['x', '10'']
		# since i made it a tuple, it returns: ("VAR", ['x', '10'])
	if 'func' in code:
		# expects a function, such as: func myfunc arg1 arg2 | print arg1 + arg2
		mode = "FUNC"
		code = code.split('|')
		sect1 = code[0]
		sect2 = code[1]
		funcname = sect1[1]
		if len(sect1) == 2:
			ast = (mode, funcname, sect2)
			tokens.append(ast)
		elif len(sect1) == 3:
			args = sect1[2:]
			ast = (mode, funcname, args, sect2)
			tokens.append(ast)
	return tokens
