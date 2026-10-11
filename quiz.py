print("***************")
print("Welcome to my Quiz Game!!!")

question_bank=[
    {"text":"The ability of one class to acquire methods and attributes of another class is called"
            "----.","answer":"A"},
    {"text": " Which of the following is a type of inheritance?","answer":"D"},
    {"text":"What type of inheritance  has multiple subclass to a single superclass?","answer":"C"},
    {"text":"What is depth of multilevel inheritance in python?","answer":"C"},
    {"text":"What does MRO stand for?","answer":"B"},
]
options=[ ["A. Inheritance "," B. Abstraction"," C.Polymorshism"," D. Objects"],
         ["A. Single"," B. Double", " C. Multiple"," D. both A and C"],
         ["A. Multiple Inheritance"," B.multiple levels"," C.Hiearchical Inheritance","D.None of these"],
         ["A. Two level", "B. Three level","C.Any level","D.None of these"],
         ["A.Method recursive object"," B. Method Resolution order"," C.Main Resolution"," D.Method Resolution order"],
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("******************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is{question_bank[question_num]["answer"]}")
        print(f"Your current score is{score}/{question_num+1}")
        print(f" You have given {score} correct answers")
        print(f" Your score is {score/len(question_bank)*100}%")




