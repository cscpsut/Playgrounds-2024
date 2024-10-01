import os
import sys

questions_and_answers = [
    {"question": "What is the victim IP?\n", "answer": "192.168.232.128"},
    {"question": "What is the attacker IP?\n", "answer": "192.168.232.129"},
    {"question": "What port was the server hosted on?\n", "answer": "45631"},
    {"question": "Provide the User-Agent used to connect to the server.\n", "answer": "curl/8.5.0"},
    {"question": "What specific vulnerability was the attacker exploiting? Please provide the answer in the format: VUL. For example, if the vulnerability is Server-Side Request Forgery, please write: SSRF\n", "answer": "LFI"},
    {"question": "What file was the attacker looking for?\n", "answer": "id_rsa"},
    {"question": "Through which protocol did the attacker connect to the victim machine?\n", "answer": "SSH"},
    {"question": "What option did the attacker use in the SSH command to specify the identity for authentication when connecting to the victim machine?(e.g., -b, -p, etc.). Hint: This is an OSINT question\n", "answer": "-i"}
]

def ask_question(question, correct_answer):
    while True:
        user_answer = input(question + " ")
        if user_answer == correct_answer:
            break
        print("Incorrect answer, please try again.")

def main():
    for qa in questions_and_answers:
        ask_question(qa["question"], qa["answer"])

    flag = os.getenv("FLAG", "FLAG not set")
    print("Yayy! Here's your flag:", flag)

main()
