import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from flask import *
import os
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyBYHpRerd0Dit9PnuF8e4JcxSj34fZqPbw",
    "authDomain": "renty-vue.firebaseapp.com",
    "databaseURL": "https://renty-vue.firebaseio.com",
    "projectId": "renty-vue",
    "storageBucket": "renty-vue.appspot.com",
    "messagingSenderId": "28025495187"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


# my_path = os.path.abspath(os.path.dirname(__file__))
# cred = credentials.Certificate(os.path.join(
#     my_path, "../renty-python-firebase-adminsdk.json"))

# options = {
#     'serviceAccountId': 'firebase-adminsdk-rma72@renty-vue.iam.gserviceaccount.com'
# }
# default_app = firebase_admin.initialize_app(cred, options=options)
# # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/julio/dev/FirebasePython/renty-python-firebase-adminsdk.json"
# # firebase_admin.initialize_app(options=options)
# # firebase = pyrebase.initialize_app(config)

# # auth = firebase.auth()
# uid = 'LDFi5ZgeRagBTa3AiGMfJlIxZgd2'
# custom_token = auth.create_custom_token(uid)
# print(custom_token)


@app.route('/', methods=['GET', 'POST'])
def basic():
    unsuccessful = 'Login unsuccessful'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            # id_token = auth.get_account_info(user['idToken'])
            print(user["idToken"])
            return render_template('new.html', s=successful)
        except:
            return render_template('new.html', us=unsuccessful)

    return render_template('new.html')


if __name__ == '__main__':
    app.run()
