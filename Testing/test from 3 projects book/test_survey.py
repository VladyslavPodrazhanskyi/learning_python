import unittest
from survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    """Test for class AnonymousSurvey"""

    def test_add_single_response(self):
        question = "What language did you learn to speak first?"
        language_survey = AnonymousSurvey(question)
        single_response = "English"
        language_survey.add_response(single_response)
        self.assertIn(single_response, language_survey.responses)
    def test_add_three_responses(self):
        question = "What language did you learn to speak first?"
        language_survey = AnonymousSurvey(question)
        three_responses = ["English", "Spanish", "German"]
        for response in three_responses:
            language_survey.add_response(response)
        for response in three_responses:
            self.assertIn(response, language_survey.responses)


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