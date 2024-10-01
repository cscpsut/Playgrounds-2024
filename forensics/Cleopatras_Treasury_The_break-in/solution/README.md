# Writeup
Once you've opened the provided PCAP file in Wireshark or NetworkMiner, you can analyze the network traffic and begin answering the following questions:

Q: What is the victim IP?
The victim IP corresponds to the machine hosting the web server.
A: 192.168.232.128

Q: What is the attacker IP?
The attacker IP is the one attempting to exploit a vulnerability in the server.
A: 192.168.232.129

Q: What port was the server hosted on?
To find the server’s port, look for traffic directed at the victim IP.
A: 45631

Q: Provide the User-Agent used to connect to the server.
You can extract the User-Agent by following the HTTP stream and reviewing the HTTP headers.
A: curl/8.5.0

Q: What specific vulnerability was the attacker exploiting? Please provide your answer in the format: VUL (e.g., SSRF).
The attacker was using directory traversal techniques, which is a sign of a Local File Inclusion (LFI) vulnerability.
A: LFI

Q: What file did the attacker extract using the LFI vulnerability?
The attacker extracted a sensitive file that allowed further access to the victim machine.
A: id_rsa

Q: What service did the attacker use to connect after obtaining the file?
After obtaining the RSA private key, the attacker used this service to establish a connection.
A: SSH
