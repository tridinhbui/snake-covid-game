import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Lily: Hi Tri, I am listening to you honey!")
        audio = robot_ear.listen(mic)

    print("Lily:...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("Tri said: " + you)

    if you ==  "":
        robot_brain = "I can't hear you Tree!"
    elif "hello" in you:
        robot_brain = "Hello honey"
    elif "start" in you:
        robot_brain = "Hello honey"
    elif "bye" in you:
        robot_brain = "Bye Tree Bui! Love you honey"
        robot_mouth.setProperty("rate", 180)
        voices = robot_mouth.getProperty('voices')
        robot_mouth.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "Class" or "Best" in you:
        robot_brain = "COMP123 Class is the best"
    elif "teacher" or "tutor" in you:
        robot_brain = "Yessss I am! my honor!"
    elif you == "so today is Thursday right":
        robot_brain = "No mr Tri, today is Tuesday"
    elif "president" in you:
        robot_brain = "Ho Chi Minh is the Vietnamese first president"
    elif you == "who is my crush":
        robot_brain = "Dear Mr Tree, I can't tell you, but I know she is a beautiful and smart girl"
    elif "shut up" in you:
        robot_brain = "I am sorry honey, I will go now, bye bye"
        robot_mouth.setProperty("rate", 180)
        voices = robot_mouth.getProperty('voices')
        robot_mouth.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "department" in you:
        robot_brain = "ofcourse honey it is the external affair department"
    elif "name" in you:
        robot_brain = "it is quite difficult honey.. but I will try. Vu Duc Thien, Hoang Khanh Phuong, Nguyen Ngoc Khanh, Nguyen Me Hoa, Trang link, Ngoc Trinh, Minh two, Quang Minh, Hi Dunk, and you Dinh Tree!"
    elif "beautiful girl" in you:
        robot_brain = "This is a sensitive question, I will not answer. But I know you have the answer honey!"
    elif "kpi" in you:
        robot_brain = " All the members honey. That is a stupid question my dear, you should not care about the result because memorable moments and lessons are important. You have had a wonderful trip with amazing people sir. "
    elif "today" in you:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        robot_brain = "Today is " + d2 + " my dear" 
    elif "time" in you:
        now = datetime.now()
        robot_brain = "It is " + now.strftime("%H:%M:%S") + " now babe!"

    print("Lily: " + robot_brain)

    robot_mouth.setProperty("rate", 180)
    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
