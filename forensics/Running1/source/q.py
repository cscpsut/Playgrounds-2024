import os

def ask_questions():
    questions = [
        {"Task": "Task 1: Find the routing protocol being used across the network.\nanswer: ", "answer": "eigrp"},
        {"Task": "Task 2: Find the common important number used between the routers.\nanswer: ", "answer": "122"},
        {"Task": "Task 3: Find the command that prevents the advertisement of routes to the LAN.\nAnswer Example format: password-encryption\nanswer: ", "answer": "passive-interface"},
        {"Task": "Task 4: Find the departments in the network.\nAnswer example format: Engineering, Sales and Business\nanswer: ", "answer": "IT, Finance and Accounting"},
        {"Task": "Task 5: Find the most sensitive information in the topology.\nanswer: ", "answer": "N3tW0rK_3NG1N33R_T7_CR4CK"}
    ]
    
    # flag = os.environ.get("FLAG", "PlaygroundsCTF{y0u_4r3_4_6r347_n37w0rk_d373c71v3}")
    with open("/chal/flag.txt", "r") as f:
        flag = f.read()
        
    correct = True
    i = 0
    for q in questions:
        i += 1
        try:
            user_answer = input(q["Task"] + " ")
            if user_answer.lower().strip() != q["answer"].lower():
                correct = False
                break
        except Exception as e:
            print(f"Error: {e}")        

    if correct:
        print(f"Congratulations! You've answered all questions correctly. Here is your flag: {flag}")
    else:
        print("You've answered some questions incorrectly. Please try again.")
    
if __name__ == "__main__":
    ask_questions()
