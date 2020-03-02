import pymysql
import textwrap
import json

db = pymysql.connect(host="116.62.212.225",user="root",password="One@2019",db="onedb_sit1",port=3306)
cursor = db.cursor()

# cursor.execute("select JSON_EXTRACT(form_json,'$**.ownerCode') from contract_form where  process_code = 'eb3af1c162c1437599f35b77cec110ed';")
# data = cursor.fetchone()
# print("Database version : %s" % data)

# sql = "select JSON_EXTRACT(form_json,'$**.ownerCode') from contract_form where  process_code = 'eb3af1c162c1437599f35b77cec110ed'"
sql = "select form_json from contract_form where  process_code = 'eb3af1c162c1437599f35b77cec110ed'"
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	# print (results)
	for row in results:
		value = row[0]
		# print (json.loads(value)['ownerList'])
		ownerList = json.loads(value)['ownerList']
		for i in ownerList:
			print(i['ownerCode'])

	# 	list(value)
	# 	print(list(value))
		# print(value.split(','))
		# print ("value=%s" % value)
		# print (type(value))

except:

	print ("Error:unable to fetch data")



db.close()
