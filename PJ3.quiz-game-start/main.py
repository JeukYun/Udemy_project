from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    Q = question
    question_bank.append(Question(Q['text'], Q['answer']))

# print(question_bank[0].text)
# Question 객체로 이루어진 question_bank 리스트 생성 완료
# Question 객체에는 question_data의 dict(text, answer)값이 속성으로 입력.


quiz = QuizBrain(question_bank) # quiz 객체 생성

while quiz.still_has_question():
    quiz.next_question() # QuizBrain 메서드 next_question() 호출

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
