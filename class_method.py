class MyClass:
	def method(self):
		"""
		Instance methods need a class instance and 
		can access the instance through `self`.
		"""
		return 'instance method called',self


	@classmethod
	def classmethod(cls):
		"""
		Class methods don't need a class instance
		They can't access the instance (self) but
		they have access to the class itself via 'cls'.
		"""
		return 'static method called'
	
	@staticmethod
	def staticmethod():
		"""
		Static methods don't have access to 'cls' or 'self'.
		They work like regular functions but belong to 
		the class's namespace.
		"""
		return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
