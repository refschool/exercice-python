from lex import *
#https://austinhenley.com/blog/teenytinycompiler1.html
def main():
	source = "LET foobar = 123"
	lexer = Lexer(source)

	while lexer.peek() != '\0':
		print(lexer.curChar)
		lexer.nextChar()

main()