
import pymysql
import json

db = pymysql.connect(host='116.62.212.225',user='root',password='One@2019',db='onedb_sit2',port=3306,charset='utf8mb4')

cursor = db.cursor()

sql = """
SELECT
	cp.code,
	cf.form_json 
FROM
	contract_form cf
	LEFT JOIN contract_process cp ON cf.process_code = cp.code 
WHERE
	cp.process_type = 1 
	AND cp.process_state >= 1030 
	AND cp.stop_state = 0;
	-- AND cp.code = 'eb3af1c162c1437599f35b77cec110ed';
"""
# print (sql)
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results)

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	# print(results)
	for row in results:
		contract_process = row[0]
		form_json = row[1]
		
		# print("contract_process=%s,form_json=%s" % (contract_process,form_json))
		# print (contract_process)
		# print (type(form_json))
		# aaa=json.dumps(form_json)
		# print(aaa)
		# for dicts in aaa:
		# 	print(dicts)
		s = json.loads(form_json)
		# print(s)
		# print(type(s))
		if 'ownerList' in s.keys():
			ownerList = s['ownerList']
			# print(ownerList)
			# print(type(ownerList))
			for r in ownerList:
				print(r['ownerCode'])
		else:
			r = s['ownerCode']
			print(r)
			# print(type(r))
			# print(type(r['ownerCode']))
		# # for s in s:
		# 	print(['remark'])

		# print(type(s))
		# print(s['remark'][0])
		# print(s)
		# remark = json.loads(s['remark'])
		# print(ownerList)
                                                                                                                       
			# ownerList = json.loads(i)['ownerList']
	# print(result)
	# print(type(result))
except:
	print("Error:unable to fecth data")

db.close()
