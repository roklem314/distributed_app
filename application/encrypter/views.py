from application import app
from application import db 
from flask import render_template, request
from application.encrypter import models
from application.encrypter.models import Ciphertext
from twofish import Twofish
from application.encrypter.randomkey import generator2, hex_to_binary
import binascii
import random
import string


@app.route("/", methods=['GET', 'POST'])
 #def info(uid: int):
def index():
    if request.method == 'POST':
        gener_key = generator2()
        T = Twofish(gener_key)
        plaintext = request.form['plaintext']
        plaintext_original = request.form['plaintext']
        if (len(plaintext) < 16 ):
            while (len(plaintext) < 16):
                plaintext = plaintext + random.choice(string.ascii_letters)
        if (len(plaintext) == 16 ):
            chipertext = T.encrypt(bytes(plaintext, 'utf-8'))
            new_chipertext= Ciphertext(chipertext,gener_key)
            #new_key = Ciphertext(hex_to_binary(gener_key))
            #db.session().add(new_chipertext)
            db.session().add(new_chipertext)
            db.session().commit()
            result = chipertext.decode('utf-8','ignore')
            #chipertext_to_plaintext = T.decrypt(chipertext)
            return render_template("index.html", result_c=result, result_p=  plaintext_original)
    

    return render_template("index.html")

