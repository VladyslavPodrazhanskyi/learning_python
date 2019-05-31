class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def add_response(self, new_response):
        self.responses.append(new_response)

    def show_responses(self):
        print("Survey result:")
        for response in self.responses:
            print("\t"+response)