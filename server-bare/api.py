# usr/bin/env/python!

# A very simple implementation of the Macchiato prototype API

# Import json and utility libraries
import json
from util import Logger, RequestState, Config
import database


class API():
	def __init__(self):
		self.logger = Logger('API')
		self.db = database.Database()

	def add_expense(self, json_expense):
		state = RequestState('POST')										# create a request state object
		processed_json = json.loads(json_expense)							# interpret the JSON

		if (state.is_valid()) :
			report = ExpenseReport.create(processed_json, state) 				# create a new expense report
			response = report.store(self.db,state)										# persist the report

		json_return = json.dumps(state.export())							# encode JSON response

		return (json_return)


	#private API
	def _convert_json(self, json):
		return json.loads(json)

class ExpenseReport(object):

	MANDATORY_FIELDS = ['amount','user','date','category','reimburseable']

	def __init__(self):
		self.logger = Logger('REPORT')

	@staticmethod
	def create(inputmsg, state):
		# create an expense
		report = ExpenseReport()
		report.log('Creating report')

		# check if all fields are present
		if (not ExpenseReport._is_valid_input(inputmsg)):
			state.error('Illegal input')
			return None

		for key in inputmsg.keys():
			report.__setattr__(key, inputmsg[key])

		return report

	@staticmethod
	def _is_valid_input(msg):
		l = map(lambda x: x in msg.keys(), ExpenseReport.MANDATORY_FIELDS)
		x = reduce(lambda x,y: x&y, l)
		return x


	################################
	####     INSTANCE METHODS   ####
	################################
	def store(self, db,state):
		if (state.is_valid()):
			self.log('Persisting report')
			db.write_record(self)

	def log(self, msg):
		self.logger.write(msg)


	################################
	####     INSTANCE METHODS   ####
	################################
	def __str__(self):
		msg = 'Expense Report printer:\n'
		for key in self.__dict__.keys():
			msg += '  %s: %s\n' % (key, self.__dict__[key])
		msg += '-------------------------'
		return msg



if __name__ == "__main__":
	Config.instance().DEBUG = True

	api = API()

	msg1 = {'user':'philip', 'date':'2015-05-14', 'amount': 0.55, 'category':'food & beverage', 'reimburseable': False}
	msg = json.dumps(msg1)
	print msg

	resp = api.add_expense(msg)

	print resp


