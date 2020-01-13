import dis

def greet(name):
	return "Hello, " + name + "!"

greet('Dan')

dis.dis(greet)
