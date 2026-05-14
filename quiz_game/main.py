from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    question_answer = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question_answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_quesitons():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")