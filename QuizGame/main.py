from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)


quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()