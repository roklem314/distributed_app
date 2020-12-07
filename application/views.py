from application import app, db 
from flask import render_template, request
from application.encrypter.models import Ciphertext
from twofish import Twofish
import binascii
import random
import string


@app.route("/", methods=['GET', 'POST'])
 #def info(uid: int):
def index():
    if request.method == 'POST':
        key = binascii.unhexlify('8CACBE276491F6FF4B1EC0E9CFD52E76')
        T = Twofish(key)
        plaintext = request.form['plaintext']
        plaintext_original = request.form['plaintext']
        if (len(plaintext) < 16 ):
            while (len(plaintext) < 16):
                plaintext = plaintext + random.choice(string.ascii_letters)
        if (len(plaintext) == 16 ):
            chipertext = T.encrypt(bytes(plaintext, 'utf-8'))
            new_chipertext= Ciphertext(chipertext)
            db.session().add(new_chipertext)
            db.session().commit()
            result = chipertext.decode('utf-8','ignore')
            #chipertext_to_plaintext = T.decrypt(chipertext)
            return render_template("index.html", result_c=result, result_p=  plaintext_original)
    

    return render_template("index.html")

