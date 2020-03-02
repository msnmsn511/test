import pymysql
import textwrap

class MysqlHandler(object):

	def __init__(self,config_file,key):
		self.config = ConfigparserHandler(config_file)
		self.host = self.config.get_data(key,'47.97.218.120')
		self.user = self.config.get_data(key,'root')
		self.psd = self.config.get_data(key,'dev@vanje')
		self.db = self.cofig.get_data(key,'sit1')
		self.port = self.config.get_data(key, '3306')
		self.conn = None
		self.cur = None
		self.logging = LogHandler().log()
		self.connect_mysql()

	def connect_mysql(self):
		try:
			self.conn = pymysql.connect(self.host,self.user,self.psd,self.db,int(self.port),cursorclass = pymysql.cursors.DictCursor,charset = 'utf8')
		except Exception as e:
			self.logging.exception(e)
		else:
			self.cur = self.conn.cursor()
			self.logging.info('{}数据库连接成功'.format(self.host))

	def close_mysql(self):
		if self.conn and self.cur:
			self.conn.close()
			self.logging.info('{}数据库关闭成功'.format(self.host))

	def select_db(self,sql):	
		try:
			self.cur.execute(sql)
			data = self.cur.fetchall()
		except Exception as e:
			self.logging.exception(e)
			return ''
		else:
			sql = textwrap.dedent(sql)
			self.logging.info(f'{sql}数据库查询成功')
			return data