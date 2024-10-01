import os
import jwt
import uuid
import json
import random
import secrets
from dotenv import load_dotenv
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)
load_dotenv()

X = 500
FLAG = os.getenv('FLAG')
SECRET_KEY = secrets.token_hex(32)
# print(SECRET_KEY)

with open([x for x in os.listdir() if x.endswith('.json')][0], 'r', encoding='utf-8') as file:
    all = json.load(file)

for q in all:
    q['المعرف'] = str(uuid.uuid4())

fail_responses = [
    'بدك واسطة ثقيلة على هيك امتحان',
    'لا بقربليش ابو مصعب',
    'موعدك الجاي كمان شهرين',
    'يلا ان شاء الله بتنجح بالمرة الجاي',
    'حدا برسب نظري يا رجل',
    'يلا يا شب قوم و قعد اللي وراك',
    'راسب'
]


@app.route('/robots.txt')
def noindex():
    response = make_response('User-agent: الشباب الطيبة\nAllow: *\n\nUser-agent: *\nDisallow: /\nDisallow: /فهرس')
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


@app.route('/فهرس')
def show_source_code():
    with open(os.path.abspath(__file__), 'r', encoding='utf-8') as file:
        source_code = file.read()
    response = make_response(source_code)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


# @app.route('/')
# def get_token():
#     initial_token = jwt.encode({'العداد': 0, 'المعرف': None}, SECRET_KEY, algorithm='HS256')
#     response = make_response(redirect(url_for('get_question')))
#     response.set_cookie('token', initial_token)
#     return response


@app.route('/سؤال')
def get_question():
    curr_q = random.choice(all)
    token = request.cookies.get('token')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        c = decoded.get('العداد', 0)
        new_token = jwt.encode({'العداد': c, 'المعرف': curr_q['المعرف']}, SECRET_KEY, algorithm='HS256')
        response = make_response(render_template('question.html', question=curr_q))
    except:
        new_token = jwt.encode({'العداد': 0, 'المعرف': None}, SECRET_KEY, algorithm='HS256')
        response = make_response(redirect(url_for('get_question')))
    finally:
        response.set_cookie('token', new_token)
        return response


@app.route('/تحقق', methods=['POST'])
def check_answer():
    data = request.form
    user_answer = data['الاجابة']

    token = request.cookies.get('token')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        c = decoded.get('العداد', 0)
        qid = decoded.get('المعرف', None)
    except:
        return random.choice(fail_responses)

    for q in all:
        if q['المعرف'] == qid:
            if user_answer == q['الخيارات'][q['مؤشر الاجابة الصحيحة']]:
                c += 1
                if c >= X:
                    return FLAG
                else:
                    new_token = jwt.encode({'العداد': c, 'المعرف': None}, SECRET_KEY, algorithm='HS256')
                    response = make_response(redirect(url_for('get_question')))
                    response.set_cookie('token', new_token)
                    return response

    return random.choice(fail_responses)


@app.route('/جواب')
def get_answer():
    qid = request.args.get('المعرف')
    for q in all:
        if q['المعرف'] == qid:
            return q['الخيارات'][q['مؤشر الاجابة الصحيحة']].encode('utf-8').decode('utf-8')

    return random.choice(fail_responses)


if __name__ == '__main__':
    app.run()