__author__ = 'pivo'
import pymongo

conn = pymongo.Connection(safe=True)
db = conn.school
students = db.students

homeworks = students.find()
id = -1
for doc in homeworks:
	score_min = 0
	for score in doc['scores']:
		if score['type'] == 'homework':
			if score_min == 0 or score['score'] < score_min:
				score_min = score['score']

	students.update({'_id':doc['_id']}, {'$pull':{'scores': {'type':'homework', 'score':score_min}}})
	print(doc['scores'])
