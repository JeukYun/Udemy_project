class QuizBrain:
    def __init__(self, q_list): # q_list 에는 Question 클래스의 객체들의 리스트가 있음
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number} : {current_question.text} (True/False) : ")