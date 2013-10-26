from flask import Flask, render_template, request
from models.contact import Contato
from models.contact_repository import ContactRepository
import sqlite3

app = Flask(__name__)
app.debug = True

@app.route('/avalicacao')
def avaliacao():
		return render_template('avaliacao.html')


@app.route('/success', methods=['POST'])
def success():
	contato = Contato(request)
	contato.save_json()

	repository = ContactRepository()
	repository.create(contato)

	#save_db(contato)

	return render_template('success.html', contact=contato) 



if __name__ == '__main__':
    app.run()