
import sys
import json
from flask import request

class Contato:

	nome = ""
	email = ""
	telefone = ""

	def __init__(self, request):
		self.r = None
		self.__load(request.form['nome'], request.form['email'], request.form['telefone'])

	def __load(self, nome, email, telefone):
		self.r = None
		self.nome, self.email, self.telefone = nome, email, telefone

	def save_json(self):
		data = {'nome' : self.nome, 'email': self.email, 'telefone': self.telefone }
		with open('data.txt', 'w') as f:
			json.dump(data, f, ensure_ascii=False)		
