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


quiz = QuizBrain(question_bank)
quiz.next_question()