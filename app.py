from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random, string

#------------------------------------------------------------------

app = Flask(__name__) # Instance of the whole app.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Database url (database.db is the file where we store the OTP)

db = SQLAlchemy(app) # Database instance

class storeFOUR(db.Model): # This is the table (store_four)
# if you wanna change table name then lol i forgot
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<{self.id} This is the id lol>' # this is what you get when you use storeFOUR.query.first()


@app.route('/api/get4digit', methods=['POST','GET']) # this be the url for postman
def get4digit():
    # data=request.get_json()
    # data['whatever the thing is named as']
    if request == 'POST':
        code = ''.join(random.choices(string.digits, k=4))# Generate OTP lol
        try: 
            storecode = storeFOUR(code=code) # Create an SQLALC object
            db.session.add(storecode) # Add this object to db
            db.commit() # hmm
        except Exception as err:
            return jsonify({'status':'Failure', 'error':repr(err)}) # LOL 
        return jsonify({'status':'success','code':code}) # send otp 
    else:
        return jsonify({"message":"LOL LOSER","status":"failure(used GET)"}) # if its get method (you can just remove the 'GET' to restrict the page to only POST reqs)


if __name__ == '__main__':
    app.run(port=69, debug=True) # THIS STARTS THE APP