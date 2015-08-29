# usr/bin/env/python!

import web
import api
from util import Config, Logger, RequestState



urls = (
  '/', 'Index',
  '/expenses/', 'Expenses'
)



class Index:

	def GET(self):
		raise web.notfound()

	def POST(self, resource_id=None):
		raise web.notfound()

class Expenses:
	def __init__(self):
		self.logger = Logger("WEB")

	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		return 'Listing expenses not yet implemented'

	def POST(self, resource_id=None):
		web.header('Access-Control-Allow-Origin', '*')
		jsondata = web.data()
		self.logger.write(jsondata)
		resp = api.API().add_expense(jsondata)
		return resp


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
