from flask import Flask,  render_template, request, send_from_directory,jsonify, make_response
import os
import threading
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    content = request.args.get('content') or request.form['content']
    if content is None:
        return render_template('post.html', content='You must provide a content parameter!')

    return render_template('post.html', content=content)

@app.route('/report', methods=['GET'])
def report():
    report_url = request.args.get('url') 
    if report_url is None:
        return make_response(jsonify({"message": f"You must provide a URL"}), 400)

    post_url = f"http://localhost:1337/"
    def post_request(url, data):
        requests.post(url, data=data)
        
    thread = threading.Thread(target=post_request, args=(post_url, {"url": report_url}))
    thread.start()
    return make_response(jsonify({"message": f"The admin will check your url shortly"}), 200)


@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'assets', 'css'), filename)

@app.route('/fonts/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.root_path, 'assets', 'fonts'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'assets', 'images'), filename)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=False,port=80)
