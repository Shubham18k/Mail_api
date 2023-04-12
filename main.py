from flask import Flask,request,jsonify
import re
import os
import Email

app=Flask(__name__)

#mail validation
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return "Valid"
    else:
        return "Invalid"

@app.route('/mail',methods = ['POST'])
#mailing process
def mailer():
        try:
            dict_file = request.get_json()
            email = dict_file["Mail"]
            sub=dict_file['Subject']
            cont=dict_file['Content']
            val=check(email)
            if val=="Invalid" :
                 return jsonify({'message' : 'Invalid Email format'})
            else:
                Email.mail(email,sub,cont)
                return jsonify({'message' : f'Mail has been send to {email}'})
                 
        except Exception as e:
             return jsonify({'message' :'Error while sending mail'})

if __name__=='__main__':
    app.run(debug=True)