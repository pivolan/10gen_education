__author__ = 'pivo'
import pymongo

conn = pymongo.Connection(safe=True)
db = conn.students
grades = db.grades

homeworks = grades.find({'type': 'homework'}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
id = -1
for doc in homeworks:
	if id != doc['student_id']:
		grades.remove({'_id':doc['_id']})
	id = doc['student_id']
	print(doc)