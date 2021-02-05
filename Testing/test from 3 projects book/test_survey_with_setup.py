# При тестировании классов, написанных вами, метод setUp() упрощает написание
# тестовых методов. Вы создаете один набор экземпляров и атрибутов в setUp() ,
# а затем используете эти экземпляры во всех тестовых методах. Это намного проще
# и удобнее, чем создавать новый набор экземпляров и атрибутов в каждом тестовом
# методе.


import unittest
from survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    """Test for class AnonymousSurvey"""
    def setUp(self):
        question = "What language did you learn to speak first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "German"]

    def test_add_single_response(self):
        single_response = self.responses[0]
        self.my_survey.add_response(single_response)
        self.assertIn(single_response, self.my_survey.responses)

    def test_add_three_responses(self):
        for response in self.three_responses:
            self.language_survey.add_response(response)
        for response in self.three_responses:
            self.assertIn(response, self.language_survey.responses)

   # def tearDown(self):



unittest.main()


# class AnonymousSurvey:
#     def __init__(self, question):
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         print(self.question)
#
#     def add_response(self, new_response):
#         self.responses.append(new_response)
#
#     def show_responses(self):
#         print("Survey result:")
#         for response in self.responses:
#             print("\t"+response)