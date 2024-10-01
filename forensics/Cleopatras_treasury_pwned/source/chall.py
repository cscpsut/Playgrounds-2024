import os
import sys

questions_and_answers = [
    {"question": "What is the first command the attacker ran on the machine?\n", "answer": ["whoami"]},
    {"question": "The attacker executed 4 commands for enumeration purposes including whoami. The last one displays files with a special permission bit, what is that bit called? Format: Name bit\n", "answer": ["SUID bit","SUID","suid","suid bit"]},
    {"question": "What is the name of the executable that was exploited?\n", "answer": ["treasury"]},
    {"question": "The exploit used Buffer Overflow vulnerability to enter a locked function in the treasury file, what was the size of the buffer?\n", "answer": ["56"]},
    {"question": "Provide the exact timestamp for when the attacker successfully opened a root shell by exploiting treasury executable. Format: YYYY-MM-DD HH:MM:SS-HH:00\n", "answer": ["2024-09-26 17:45:48-04:00"]},
    {"question": "To maintain persistence, the attacker created a new user with root privileges. What was the username?\n", "answer": ["yasta"]} 
]

def ask_question(question, correct_answers):
    while True:
        user_answer = input(question + " ")
        if user_answer in correct_answers:
            break
        print("Incorrect answer, please try again.")

def main():
    for qa in questions_and_answers:
        ask_question(qa["question"], qa["answer"])

    flag = os.getenv("FLAG", "FLAG not set")
    print("Yayy! Here's your flag:", flag)

main()
