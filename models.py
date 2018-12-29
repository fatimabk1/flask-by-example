# import our database connection created in app.py
from app import db
# import json from sqlalchemy dialects
from sqlalchemy.dialects.postgresql import json

# Result models a table in the db
class Result(db.Model):
	__tablename__ = 'results'

	# sqlalchemy used to define attribuate name + type + restrictions
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String())
	result_all = db.Column(JSON)
	result_no_stop_words = db.Column(JSON)

	# runs the first time we create a new result
	def __init__(self, url, result_all, result_no_stop_words):
		self.url = url
		self.result_all result_all
		self.result_no_stop_words = result_no_stop_words

	# represent the object when we query for it
	def __repr__(self):
		return '<id {}>'.format(self.id)

