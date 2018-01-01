from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True      

@app.route("/", methods=['POST','GET'])
def index():
    if request.method=='POST':
        error_name=''
        error_password=''
        error_email=''
        username = request.form['username']
        password_top = request.form['password_top']
        password_bot = request.form['password_bot']
        email=request.form['email']
        
        uname=re.compile('\S{3,20}$')
        unamecheck=uname.match(username)
        if not unamecheck:
            error_name='Please enter an username between 3 and 20 characters and no spaces.'

        if password_bot!=password_top:
            error_password='Passwords do not match'
        else:
            password=re.compile('\S{3,20}$')
            password_check=password.match(password_top)
            if not password_check:
                error_password='Please enter a password between 3 and 20 characteres and no spaces.'
        
        if email:
            email_re=re.compile('\S+@\S+\.\S+')
            email_check=email_re.match(email)
            if not email_check:
                error_email="""Please enter an email containing a single @,
                              a single ., contains no spaces, and is between 3 and 20 characters long."""               
        
        if error_email or error_password or error_name:
            return render_template('index.html',error_name=error_name,
                                   error_password=error_password,
                                   error_email=error_email,
                                   email=email,
                                   username=username)
        else:
            return render_template('welcome.html',
                                    username=username)

        

    else:    
        return render_template('index.html')

app.run()