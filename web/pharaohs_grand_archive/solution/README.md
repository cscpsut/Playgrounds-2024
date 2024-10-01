# Write-Up

## TL;DR
Basic LFI vulnerability

### Solution
1. By intercepting requests using Burp Suite, we notice the requests responsible for retrieving the scrolls.
   ![alt text](image.png)
2. We notice that there is a parameter in the URL called `file`, which indicates that the scrolls are probably saved in text files on the server, and they are being retrieved using the name of the file. The content is returned in Base64 format.
3. Check if there is an LFI vulnerability by trying to read `/etc/passwd`:
    1. Send one of the requests to Repeater using `CTRL+R`.
    2. Modify the `file` parameter to `../../../etc/passwd`.
       ![alt text](image-1.png)
    3. Decode it using CyberChef.
       ![alt text](3.png)
4. Now to read the flag, you need to read the environment variables in `/proc/self/environ`.
    ![alt text](image-2.png)
    ![alt text](image-3.png)
