# connect to the database

import sqlite3
import util

class Database:
	def __init__(self):
		self.db_location = util.Config.instance().DB_PATH
		self.cursor = self._open_connection()
		self.log = util.Logger('DATABASE')

	# connect to the database
	def _open_connection(self):
		self.conn = sqlite3.connect(self.db_location)
		cursor = self.conn.cursor()
		return cursor

	def write_record(self, record):
		category_id = self.get_category_id(record.category)[0][0]
		user_id = self.get_user_id(record.user)[0][0]
		sql = "INSERT INTO expense_reports ('user_id','category_id','amount','reimbursed','date') VALUES ('%s','%s','%s','%s','%s')" % (user_id, category_id, record.amount, record.reimburseable, record.date)
		self._execute(sql)

	def get_category_id(self, category):
		return self._get_id('category_id','categories','name',category)

	def get_user_id(self, user):
		return self._get_id('user_id','users','name',user)

	def _get_id(self, field, table, match_field, match_value):
		sql = "SELECT %s FROM %s WHERE %s LIKE '%%%s%%'" % (field, table, match_field, match_value)
		return self._execute_get(sql)


	def _execute_get(self, SQL):
		self._execute(SQL)
		return self.cursor.fetchall()

	def _execute(self, SQL):
		self.log.write(SQL)
		self.cursor.execute(SQL)
		self.conn.commit()

if __name__ == "__main__":
	db = Database()

	print db.get_category_id('Taxi')
	print db.get_user_id('philip')