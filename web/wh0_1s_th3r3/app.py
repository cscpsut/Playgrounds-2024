from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    domain = request.form.get('domain')
    
    # Filter dangerous input
    blacklist = ['&', '|','`', '>', '<','ls','cat','less',]
    if any(char in domain for char in blacklist) or len(domain) > 50:
        return render_template('index.html', error="Injection Detected!!!")
    
    try:
        # Run the whois command and capture output
        result = subprocess.check_output(f"whois {domain}", shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
