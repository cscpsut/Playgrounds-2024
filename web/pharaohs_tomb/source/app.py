from flask import *
import os,secrets

app = Flask(__name__)
app.secret_key=os.urandom(30)
FLAG=os.getenv('FLAG') or "PlaygroundsCTF{FAKE_FLAG_FOR_TESTING}"
users={"pharaoh":{"password":secrets.token_hex(),"role":'pharaoh'}}

def logged_in_check():
    if session and session.get('loggedin') == True:
        return redirect(url_for('gold'))
    return False

@app.route("/")
def index():
    return redirect(url_for('tomb_entrance'))

@app.route('/tomb_entrance',methods=['GET'])
def tomb_entrance():
    return render_template('tomb_entrance.html')

@app.route('/register',methods=['GET','POST'])   
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('confirm_password')
        if username in users:
            return render_template('register.html',error='Username already exist.')
        elif password != password2:
            return render_template('register.html',error='Password and password confirmation do not match.')
        else:
            users[username]={k:v for k,v in request.form.items()}
            return render_template('login.html',message='User registered successfully.')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username]['password'] == password:
            session['loggedin'] = True
            session['role'] = users[username].get('role')
            return redirect(url_for('guards'))
        return render_template('login.html',error="Invalid username or password.")
        
@app.route('/guards')
def guards():
    if logged_in_check():
        return render_template('guards.html',logged_in=True)
    return render_template('guards.html',logged_in=False)

@app.route('/gold')
def gold(): # Flag
    if logged_in_check() and session.get('role') == 'pharaoh' or session.get('role') == 'guard':
        return render_template('gold.html',flag=FLAG)
    else:
        return render_template('guards.html', error='You do not have permission to access the gold.')
    
@app.route('/logout',methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for('tomb_entrance'))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1337)

