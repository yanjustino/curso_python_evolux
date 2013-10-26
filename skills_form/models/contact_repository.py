from contact import Contato
import sqlite3

class ContactRepository:


	def __init__(self):
		self.r = None
		self.__create_database_if_not_exists()
	

	def __create_database_if_not_exists(self):
		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS skills
		             (name text, email text, skills text)''')

		conn.commit()
		conn.close()

	def create(self, contato):
		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		c.execute("INSERT INTO skills VALUES ('%s','%s','%s')" % (contato.nome, contato.email, contato.telefone))
		conn.commit()
		conn.close()