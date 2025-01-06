import pyttsx3 as pt

engine = pt.init()
engine.say("Hello World")
engine.runAndWait()

engine.stop()
engine.save_to_file("Hello World", "hello.mp3")
engine.runAndWait()

test1=pt.init()
test1.say("this is one project with pyttsx3") # this is the text that will be spoken
test1.runAndWait()