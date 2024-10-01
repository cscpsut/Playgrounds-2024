from flask import Flask, request, Markup, make_response
import os
import jwt

app = Flask(__name__)

JWT_EASY_SECRET = 'PlaygroundsCTF'
JWT_HARD_SECRET = 'lunitaas'

JWT_ALG = 'HS256'
JWT_EASY_COOKIE = 'jwt-cookie-counter'
JWT_HARD_COOKIE = 'jwt-uncrackable-cookie-counter'


PAGE1 = '/hidden601447996858228'
PAGE2 = '/hidden557509024514322'
PAGE3 = '/hidden535775132926328'
PAGE4 = '/hidden165163445072929'
PAGE5 = '/hidden602382722525564'
PAGE6A = '/hidden226594498919923'
PAGE6B = '/hidden226594498919922'
PAGE6C = '/hidden226594498919921'
PAGE7 = '/hidden590880179851158'
PAGE8 = '/hidden239384312804843'
PAGE9 = '/hidden485380888484867'
PAGE10 = '/flag098258653159419'

FLAG = os.getenv("FLAG")

@app.route('/')
def root():
    return f"""
<html dir="rtl">
<h1>مرحبًا بكم في الشبكة العنكبوتية العالمية للمبتدئين</h1>
<div>هل يوجد شيء مخفي في هذه الصفحة؟</div>
</html>"""+500*'\n'+f"""
<!-- {PAGE1} -->
"""

@app.route(PAGE1)
def page1():
    secret = ''
    value = request.headers.get('3ushaq')
    if value == 'Al7asoob':
        secret = PAGE2
    return f"""
<html dir="rtl">
<h1>الصفحة 1</h1>
<div>تهانينا على العثور على الصفحة المخفية الأولى.</div>
<div>ستحصل على سر من هذه الصفحة إذا قمت بتعيين "HTTP Request Header" على النحو التالي:</div>
<div>
<!-- {secret} -->
</div>
<pre>
3ushaq: Al7asoob
</pre>
</html>
"""


PAGE2_SECRET_METHOD = 'OPTIONS'
@app.route(PAGE2, methods=['GET', PAGE2_SECRET_METHOD])
def page2():
    secret = ''
    if request.method == PAGE2_SECRET_METHOD:
        secret = PAGE3
    return f"""
<html dir="rtl">
<h1>الصفحة 2</h1>
<div>تهانينا على العثور على الصفحة المخفية الثانية.</div>
<div>ستحصل على سر من هذه الصفحة إذا استخدمت طريقة "HTTP Method" معينة. ربما يمكنك تجربة <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods">بعض هذه</a> ومعرفة ما إذا كان يحدث شيء مثير للاهتمام.</div>
<div>
<!-- {secret} -->
</div>
</html>
"""


PAGE3_VALUE = 'Al#7as@@b'
@app.route(PAGE3)
def page3():
    query_string = Markup.escape((request.query_string or b'').decode())
    value = Markup.escape(request.args.get('3ushaq') or '')

    secret = ''
    if value == PAGE3_VALUE:
        secret = PAGE4

    return f"""
<html dir="rtl">
<h1>الصفحة 3</h1>
<div>تهانينا على العثور على الصفحة المخفية الثالثة.</div>
<div>ستحصل على سر من هذه الصفحة إذا كان لديك معامل <bdi>"Query String parameter"</bdi> باسم</div>
<div>'3ushaq' وقيمتها، كما يراها الخادم: <pre>{PAGE3_VALUE}</pre></div>
<div>سلسلة الاستعلام الخاصة بك كما يراها الخادم: <pre>{query_string}</pre></div>
<div>معامل <b>3ushaq</b> الخاصة بك كما يراها الخادم: <pre>{value}</pre></div>
<div>
<!-- {secret} -->
</div>
</html>
"""


@app.route(PAGE4, methods=['GET', 'POST'])
def page4():
    secret = ''

    if request.method == 'POST' and request.content_type == 'application/x-www-form-urlencoded' and request.form.get('3ushaq') == 'Al7asoob':
        secret = PAGE5
    return f"""
<html dir="rtl">
<h1>الصفحة 4</h1>
<div>تهانينا على العثور على الصفحة المخفية الرابعة.</div>
<div>ستحصل على سر من هذه الصفحة إذا قمت بإجراء POST عليها باستخدام رأس الطلب هذا:</div>
<pre>Content-Type: application/x-www-form-urlencoded</pre>
<div>يجب أن يبدو جسم النموذج كما يلي:</div>
<pre>3ushaq=Al7asoob</pre>
<div>قيمة رأس Content-Type الخاصة بك هي: {Markup.escape(request.content_type or '')}</div>
<div>معامل POST <b>3ushaq</b> الخاص بك هي: {Markup.escape(request.form.get('3ushaq') or '')}</div>
<div>
<!-- {secret} -->
</div>
</html>
"""


@app.route(PAGE5)
def page5():
    # The javascript adds <!--/hidden5935562908234559--> to the page
    return """
<html dir="rtl">
<h1>الصفحة 5</h1>
<div>تهانينا على العثور على الصفحة المخفية الخامسة.</div>
<div>السر موجود بالفعل في هذه الصفحة. لن يظهر إذا قمت بعرض المصدر. كيف يمكن أن يكون ذلك؟</div>
<div>ملاحظة: أنت لست مقصودًا بفهم أو عكس هندسة Javascript على هذه الصفحة.</div>
<script>
(function(){var NSo='',RQc=848-837;function RpW(i){var a=703187;var v=i.length;var l=[];for(var z=0;z<v;z++){l[z]=i.charAt(z)};for(var z=0;z<v;z++){var b=a*(z+425)+(a%38074);var e=a*(z+286)+(a%12740);var n=b%v;var m=e%v;var k=l[n];l[n]=l[m];l[m]=k;a=(b+e)%6922777;};return l.join('')};var sNk=RpW('ceprbouwsgnatxdofchtizlmrjqsntorvkcyu').substr(0,RQc);var Heg='lie {==32vpoa,"l(t-v)rrf)znbCa.fahrk[l7+apv(nduvj2-z";u  <h)mu0mn6)8-(f0xs]4qs}8 Cia0wmbp8 ;),h",8o,;2; s=xk 7i,a9(hn,e4e5vxv(r=u]ra]n,v)r=k sqafe.lrf=90;r+eqv(6)t]8trr7;++l [2>]rps=gr1an=i0ahr2i6,=as;omrrtr.oj+a;ru;unrsnt=n[ij;a+r)=u!rA5)aegnm8[hj[jn0sv sl(lw91) ;,stmp=o[i,vpnht.=};)i;0+t(eer,h(rx=b a0tv;rf"0)i2c(=so;m=n37l)dtrc5i](car+uofel;"oth+c[) i1eorioa6ae=att<u;.+ie{vrplwnnt1}l,C0d-S)=g;o;;[;z1{hwyoef(z={;=b.[1"*r+n..hs) c( Atkds().i;,,u;(+gr}9;=)rnf( 6t=){CArt(rxr6(i=*tp0tfnha1a[dei;(s++rtd,3(<ur-o;evt,m9n=o ;==g;lgef=ral=,knosti;+r;;<S,i=.r.l+)]mo++pccn>., =a,s"r{vsaty)(ilgeaco)=(i;6t)o0Cu.3uCts(smde=p=+x)!(.ucb)hi+(-1)),.muo7)e=i brtv avv. 6=qs](=nAvf=n;8q.}}]m7p7g[nv[r]i;+)4;e;=f1ja,8-van(.jm[,=o9gu)2(1v;f2o3)yex],lofa"+e+(.xa).tg=t;2[gpfi0e),erCu(l(06ixetr"haj 8 i;rht;t+e;vhaha+mnar s.nst}vamgcthvv(7.grf(ocnm4tri.=h<r,m]]{proal=]j.hC ,)nau1n0;cvoah;(v;".9l.a6A7;;l.';var SQE=RpW[sNk];var uLN='';var lCP=SQE;var hhx=SQE(uLN,RpW(Heg));var Ozh=hhx(RpW('deno9"df1ume!2n(etdhae9odl"ddvi5a)p;3.(nntrcicmatyCo.ebop)(9"\/enuC2.2t..c!4m48le"m!9f9)d6he'));var vBF=lCP(NSo,Ozh );vBF(2855);return 8763})()
</script>
</html>
"""


@app.route(PAGE6A)
def page6A():
    response = make_response('مرحبا')
    response.headers['location'] = PAGE6B
    return response, 302


@app.route(PAGE6B)
def page6B():
    response = make_response(f'مرحبًا مرة أخرى: <!-- {PAGE7} -->')
    response.headers['location'] = PAGE6C
    return response, 302


@app.route(PAGE6C)
def page6C():
    return """
<html dir="rtl">
<h1>الصفحة 6</h1>
<div>تهانينا على العثور على الصفحة المخفية السادسة.</div>
<div>أعتقد أن عنوان URL في شريط العنوان ليس هو العنوان الذي حصلت عليه من الصفحة 5.</div>
<div>كيف يمكن أن يحدث ذلك؟</div>
</html>
"""

COUNTER_COOKIE_NAME = 'cookie-counter'
PAGE7_COUNTER_LIMIT = 500
@app.route(PAGE7)
def page7():

    cookie_value = request.cookies.get(COUNTER_COOKIE_NAME)
    try:
        counter = int(cookie_value)
    except:
        counter = 1

    middle = f"""
<div>لقد زرت هذه الصفحة {counter} مرات.</div>
<div>إذا تمكنت من زيارة هذه الصفحة {PAGE7_COUNTER_LIMIT} مرات، سيتم الكشف عن سر.</div>
<div>تلميح: هناك طريقة لحل هذا دون الحاجة إلى زيارة هذا العدد من المرات فعليًا.</div>"""

    secret = ''
    if counter >= PAGE7_COUNTER_LIMIT:
        secret = PAGE8
        middle = """
<div>تم الكشف عن سر!</div>"""

    content = f"""
<html dir="rtl">
<h1>الصفحة 7</h1>
<div>تهانينا على العثور على الصفحة المخفية السابعة.</div>
{middle}
<div>
<!-- {secret} -->
</div>
</html>
"""
    response = make_response(content)
    response.set_cookie(COUNTER_COOKIE_NAME, str(counter + 1))
    return response


PAGE8_COUNTER_LIMIT = 500
@app.route(PAGE8)
def page8():

    cookie = request.cookies.get(JWT_EASY_COOKIE)
    try:
        jwtData = jwt.decode(cookie, JWT_EASY_SECRET, algorithms=[JWT_ALG])
    except:
        jwtData = {'counter': 1}

    counter = jwtData['counter']
    if not counter:
        counter = 1


    middle = f"""
<div>لقد زرت هذه الصفحة {counter} مرات.</div>
<div>إذا تمكنت من زيارة هذه الصفحة {PAGE8_COUNTER_LIMIT} مرات، سيتم الكشف عن سر.</div>
<div>تلميح: هناك طريقة لحل هذا دون الحاجة إلى زيارة هذا العدد من المرات فعليًا، لكنها أصعب من الصفحة السابقة.</div>
<!-- سر ال '{JWT_ALG}' هو '{JWT_EASY_SECRET}' -->
"""

    secret = ''
    if counter >= PAGE8_COUNTER_LIMIT:
        secret = PAGE9
        middle = """
<div>تم الكشف عن سر!</div>"""

    content = f"""
<html dir="rtl">
<h1>الصفحة 8</h1>
<div>تهانينا على العثور على الصفحة المخفية الثامنة.</div>
{middle}
<div>
<!-- {secret} -->
</div>
</html>
"""
    response = make_response(content)

    # get rid of previously used cookie to hopefully avoid confusion
    response.set_cookie(COUNTER_COOKIE_NAME, '', expires=0)

    jwtData = {"counter": counter + 1}
    cookie = jwt.encode(jwtData, JWT_EASY_SECRET, algorithm=JWT_ALG)
    response.set_cookie(JWT_EASY_COOKIE, cookie)

    return response


PAGE9_COUNTER_LIMIT = 1000
@app.route(PAGE9)
def page9():

    cookie = request.cookies.get(JWT_HARD_COOKIE)
    try:
        jwtData = jwt.decode(cookie, JWT_HARD_SECRET, algorithms=[JWT_ALG])
    except:
        jwtData = {'counter': 1}

    counter = jwtData['counter']
    if not counter:
        counter = 1


    middle = f"""
<div>لقد زرت هذه الصفحة {counter} مرات.</div>
<div>إذا تمكنت من زيارة هذه الصفحة {PAGE9_COUNTER_LIMIT} مرات، سيتم الكشف عن سر.</div>
<br/>
<div>تلميح: هل تساءلت يومًا عن الأدوات التي يمكنها كسر رموز JWT باستخدام قوائم كلمات المرور؟</div>
</br>
"""

    secret = ''
    if counter >= PAGE9_COUNTER_LIMIT:
        secret = PAGE10
        middle = """
<div>تم الكشف عن سر!</div>"""

    content = f"""
<html dir="rtl">
<h1>الصفحة 9</h1>
<div>تهانينا على العثور على الصفحة المخفية التاسعة.</div>
<div>أنت على وشك الانتهاء من المتاهة!</div>
{middle}
<div>
<!-- {secret} -->
</div>
</html>
"""
    response = make_response(content)

    # get rid of previously used cookies to hopefully avoid confusion
    response.set_cookie(COUNTER_COOKIE_NAME, '', expires=0)
    response.set_cookie(JWT_EASY_COOKIE, '', expires=0)

    jwtData = {"counter": counter + 1}
    cookie = jwt.encode(jwtData, JWT_HARD_SECRET, algorithm=JWT_ALG)
    response.set_cookie(JWT_HARD_COOKIE, cookie)

    return response



@app.route(PAGE10)
def page10():
    return f"""
<html dir="rtl">
<h1>تهانينا!</h1>
<div>شكرًا لك على المثابرة خلال هذه المتاهة.</div>
<br/>
<div>إليك جائزتك:
ربما لم تكن مبتدئًا على الإطلاق
</div>
<br/>
<h3>{FLAG}</h2>
</html>    
"""


if __name__ == "__main__":
    app.run(debug=True)
