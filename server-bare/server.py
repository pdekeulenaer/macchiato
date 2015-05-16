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
	def GET(self):
		return 'Listing expenses not yet implemented'

	def POST(self, resource_id=None):
		jsondata = web.data()
		resp = api.API().add_expense(jsondata)
		return resp


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()