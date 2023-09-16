# FINAL SCHEDULE MAKER WITH OPEN AI

import openai
import datetime

# First, let's set up the OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Let's create a function to generate a study schedule for the next seven days based on the subjects and exam dates
def generate_schedule(subjects):
    # Get the current date
    today = datetime.date.today()

    # Create a list to store the study schedule for each day
    schedule = [""] * 7

    # Loop through each subject and exam date and assign study time to the corresponding days
    for subject, exam_date in subjects.items():
        # Calculate the number of days between today and the exam date
        delta = exam_date - today
        days_until_exam = delta.days

        # If the exam is in the next seven days, assign study time to the corresponding days
        if days_until_exam <= 7 and days_until_exam >= 0:
            for i in range(days_until_exam, 7):
                schedule[i] += f"\n- {subject}: {days_until_exam-i} day(s) until the exam"
    
    # Set up the prompt for the API request
    prompt = (f"Create a detailed study schedule to help me prepare for my exams. The schedule should span the next seven days and include specific tasks to be completed each day." 
               "The exams will each cover one of the following subjects and will be held on their respective exam dates: {subjects}. {schedule}")

    # Call the API to generate the study schedule
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )

    # Extract the study schedule from the API response
    study_schedule = response.choices[0].text.strip()

    # Return the study schedule
    return study_schedule

# Now, let's create a basic application that takes in a list of subjects and their respective exam dates and generates a study schedule for the next seven days
subjects = {}

while True:
    print("Enter a subject or type 'done' to finish:")
    subject = input()
    if subject == "done":
        break
    print("Enter the exam date (YYYY-MM-DD):")
    exam_date = input()
    exam_date = datetime.datetime.strptime(exam_date, "%Y-%m-%d").date()
    subjects[subject] = exam_date

# Print the list of subjects and exam dates
print("Subjects and Exam Dates:")
for subject, exam_date in subjects.items():
    print(f"{subject}: {exam_date.strftime('%Y-%m-%d')}")

# Generate a study schedule based on the subjects and exam dates
study_schedule = generate_schedule(subjects)

# Print the study schedule
print("\nStudy Schedule for the Next Seven Days:")
print(study_schedule)







# # CHAT ASSISTANT WITH OPEN AI

# import openai
# import datetime

# # First, let's set up the OpenAI API key
# openai.api_key = "OPENAI_API_KEY"

# # Let's create a function to generate an exam schedule for the day based on the given subjects
# def generate_schedule(subjects):
#     # Set up the prompt for the API request
#     prompt = f"Using a table, create a detailed study schedule for a week to prepare for exams in the following subjects: {subjects}."
    
#     # Call the API to generate the schedule
#     response = openai.Completion.create(
#       engine="text-davinci-002",
#       prompt=prompt,
#       max_tokens=1024,
#       n=1,
#       stop=None,
#       temperature=0.5,
#     )
    
#     # Extract the schedule from the API response
#     schedule = response.choices[0].text.strip()
    
#     # Return the schedule
#     return schedule

# # Now, let's create a basic list of subjects
# subjects = []

# while True:
#     print("Enter a subject or type 'done' to finish:")
#     subject = input()
#     if subject == "done":
#         break
#     subjects.append(subject)

# # Print the list of subjects
# print("To-Do List:")
# for i, subject in enumerate(subjects):
#     print(f"{i+1}. {subject}")

# # Generate a schedule based on the subjects
# schedule = generate_schedule(subjects)

# # Print the schedule
# print("\nSchedule for the Week:")
# print(schedule)




# VOICE ASSISTANT WITH OPEN AI 

# import openai
# import speech_recognition as sr
# import pyttsx3
# import datetime
# import webbrowser
# import os
# import time

# # Set up OpenAI API credentials
# openai.api_key = "OPENAI_API_KEY"


# def get_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak now...")
#         audio = r.listen(source)
#         said = ""

#         try:
#             said = r.recognize_google(audio)
#             print(said)
#         except Exception as e:
#             print("Exception: " + str(e))

#     return said.lower()

# # def set_reminder():
# #     engine = pyttsx3.init()
# #     engine.say("What should I remind you about?")
# #     engine.runAndWait()

# #     text = get_audio()

# #     engine.say("When should I remind you?")
# #     engine.runAndWait()

# #     time_str = get_audio()

# #     try:
# #         time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
# #         now = datetime.datetime.now()

# #         delta = time_obj - now.time()

# #         reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=delta.seconds)

# #         engine.say(f"Reminder set for {time_str}")
# #         engine.runAndWait()

# #         time.sleep(delta.seconds)
# #         engine.say(f"Reminder: {text}")
# #         engine.runAndWait()

# #     except ValueError:
# #         engine.say("Sorry, I did not understand the time")
# #         engine.runAndWait()

# def create_to_do_list():
#     tasks = []

#     engine = pyttsx3.init()
#     engine.say("What tasks do you want to add to your to-do list? Say 'done' when you're finished.")
#     engine.runAndWait()

#     while True:
#         task = get_audio()

#         if "done" in task:
#             break

#         tasks.append(task)
#         engine.say(f"{task} added to to-do list")
#         engine.runAndWait()

#     engine.say("Creating schedule based on your to-do list...")
#     engine.runAndWait()

#     # Use OpenAI API to generate a schedule based on the to-do list
#     prompt = f"Create a schedule for a day based on the following to-do list: {', '.join(tasks)}"
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     schedule = response.choices[0].text.strip()

#     engine.say("Here's your schedule for the day:")
#     engine.say(schedule)
#     engine.runAndWait()

# # def search_web():
# #     engine = pyttsx3.init()
# #     engine.say("What do you want me to search for?")
# #     engine.runAndWait()

# #     search_query = get_audio()

# #     url = f"https://www.google.com/search?q={search_query}"
# #     webbrowser.get().open(url)

# #     engine.say(f"Here are the search results for {search_query}")
# #     engine.runAndWait()

# while True:
#     print("Listening...")
#     text = get_audio()

#     # if "set reminder" in text:
#     #     set_reminder()

#     if "create to-do list" in text:
#         create_to_do_list()

#     # if "search" in text:
#     #     search_web()

#     if "stop listening" in text or "exit" in text:
#         print("Exiting...")
#         break







# VOICE ASSISTANT WITHOUT OPEN AI

# import speech_recognition as sr
# import pyttsx3
# import datetime
# import webbrowser
# import os
# import time

# def get_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak now...")
#         audio = r.listen(source)
#         said = ""

#         try:
#             said = r.recognize_google(audio)
#             print(said)
#         except Exception as e:
#             print("Exception: " + str(e))

#     return said.lower()

# def set_reminder():
#     engine = pyttsx3.init()
#     engine.say("What should I remind you about?")
#     engine.runAndWait()

#     text = get_audio()

#     engine.say("When should I remind you?")
#     engine.runAndWait()

#     time_str = get_audio()

#     try:
#         time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
#         now = datetime.datetime.now()

#         delta = time_obj - now.time()

#         reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=delta.seconds)

#         engine.say(f"Reminder set for {time_str}")
#         engine.runAndWait()

#         time.sleep(delta.seconds)
#         engine.say(f"Reminder: {text}")
#         engine.runAndWait()

#     except ValueError:
#         engine.say("Sorry, I did not understand the time")
#         engine.runAndWait()

# while True:
#     print("Listening...")
#     text = get_audio()

#     if "set reminder" in text:
#         set_reminder()

#     if "create to-do list" in text:
#         create_to_do_list()

#     if "search" in text:
#         search_web()

#     if "stop listening" in text or "exit" in text:
#         print("Exiting...")
#         break

