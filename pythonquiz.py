class QuizBot:
    def __init__(self):
        self.questions = [
            "What is the capital of INDIA?",
            "Which planet is known as the Red Planet?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the chemical symbol for water?",
            "What year did the Titanic sink?"
        ]
        self.answers = ["Delhi", "Mars", "William Shakespeare", "H2O", "1912"]
        self.user_responses = []
        self.current_question_index = 0

    def record_current_answer(self, answer):
        self.user_responses.append(answer)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        else:
            return None

    def generate_final_response(self):
        score = 0
        total_questions = len(self.questions)
        for i in range(total_questions):
            if self.user_responses[i] == self.answers[i]:
                score += 1
        return f"You scored {score} out of {total_questions}."

def main():
    quiz_bot = QuizBot()
    while True:
        question = quiz_bot.get_next_question()
        if question:
            print(question)
            answer = input("Your answer: ")
            quiz_bot.record_current_answer(answer)
        else:
            print(quiz_bot.generate_final_response())
            break

if __name__ == "__main__":
    main()
