import os
FLAG = os.environ.get('FLAG')
if isinstance(FLAG, str):
    FLAG = FLAG.encode()
# Best infra team <3