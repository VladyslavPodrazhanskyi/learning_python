from survey import AnonymousSurvey

question = "What language did you learn to speak first?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("\nEnter'q' at anytime to quit")

while True:
    new_response = input("Language: ")
    if new_response == "q":
        break
    else:
        language_survey.add_response(new_response)

print("Thank you to everyone who participate in this survey")
language_survey.show_responses()




