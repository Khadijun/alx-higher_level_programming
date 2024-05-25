#!/usr/bin/env/python3
import cmd
'''
this module handles comand line arguments, i.e command line interpreter
'''
class  khaddy(cmd.Cmd):
	'''
	subclass Khady inheritss the characters of class cmd.Cmd
	'''
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = 'Khaddy$'
	def do_quit(self):
		return exit

cli = khaddy()
cli.cmdloop()
