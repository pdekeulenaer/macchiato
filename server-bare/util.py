# utilities
import sys

class Config():	
	def __init__(self):
		self.DEBUG = True
		self.DB_PATH = '/home/macchiato/database/macchiato_poc.db'
		pass

	_instance = None

	@staticmethod
	def instance():
		if (Config._instance is None):
			Config._instance = Config()
		return Config._instance

# A class to track the state
class RequestState():
	# default types is a POST
	def __init__(self, reqtype='GET'):
		self.HTTP_RESPONSE = 200
		self.HTTP_TYPE = reqtype
		self.content = None

	def error(self, msg='No error information'):
		self.HTTP_RESPONSE = 400
		self.content = msg

	def is_valid(self):
		return self.HTTP_RESPONSE == 200

	def export(self):
		return {'HTTP_RESPONSE':self.HTTP_RESPONSE,
				'HTTP_TYPE': self.HTTP_TYPE,
				'CONTENT': self.content}

class Logger():
	def __init__(self, prefix):
		self.prefix = prefix

	def write(self, msg):

		if (Config.instance().DEBUG):
			print "[%s] %s" % (self.prefix, msg)
			sys.stdout.flush()
		else:
			pass
