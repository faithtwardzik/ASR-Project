# Program creates a 'Performance Tracker' GUI app which takes in user's speech responses
# and responds with "Correct" or "Incorrect. Try again" (until correct response given)
# Displays performance summary after each slide and at end of exercise
import threading
import tkinter
import speech_recognition as sr
import pyttsx3 as tts
import time
import sys
import tkvideo
from PIL import ImageTk, Image
from multiprocessing import Process

root = tkinter.Tk()
engine = tts.init()


# exits program upon user command
def exit_program(text):
    if text == "exit program":
        sys.exit()


# converts user audio to text string
def speech_to_text():
    r = sr.Recognizer()
    text = ""

    # loops until user gives valid input
    while text == "":  # sr.Microphone(), r.listen
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=30)
            try:
                text = r.recognize_google(audio)
            except Exception as e:
                engine.say("Could not detect input. Please try again.")
                engine.runAndWait()
    return text


# checks user input against correct inputs, if incorrect, loops until receiving correct input,
# if correct, says "Correct" and continues to next slide
def slide1_run():
    slide1 = speech_to_text()
    slide1_inc_tries = 0

    exit_program(slide1)
    while slide1 != "brushing teeth" and slide1 != "washing hands" and slide1 != "combing hair":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide1_inc_tries += 1
        slide1 = speech_to_text()
        exit_program(slide1)
    engine.say("Correct")
    engine.runAndWait()
    # incorrect_tries["slide1"].append(slide1_inc_tries)
    #  gen_performance_summary(slide1_inc_tries, "Slide 1")
    engine.say("Continue")
    engine.runAndWait()
    #  canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    root.update()

    # used to get rid of the video (my_label) and the rest of the objects on the screen. However,
    # I don't think it destroys the video, just hides it. So it might be playing in the background,
    # holding up thread2
    my_label.pack_forget()
    my_label.grid_forget()
    my_label.place_forget()
    my_label.forget()
    canvas.delete('all')
    return slide1_inc_tries


# checks user input against correct inputs, if incorrect, loops until receiving correct input,
# if correct, says "Correct" and continues to next slide (for slide2)
def slide2_run():
    slide2 = speech_to_text()
    slide2_inc_tries = 0
    exit_program(slide2)
    while slide2 != "packing bag" and slide2 != "choosing shirt" and slide2 != "eating breakfast":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide2_inc_tries += 1
        slide2 = speech_to_text()
        exit_program(slide2)
    engine.say("Correct")
    engine.runAndWait()
    #  incorrect_tries["slide2"].append(slide2_inc_tries)
    # gen_performance_summary(slide2_inc_tries, "Slide 2")
    engine.say("Continue")
    engine.runAndWait()
    # canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    canvas.delete('all')
    root.update()


# displays the text and shows the video on the screen for slide1
def show_vid1():
    #  my_label = tkinter.Label(root)
    #  my_label.pack()
    player = tkvideo.tkvideo("Media1.mov", my_label, loop=1, size=(600, 325))
    my_label.place(relx=0.5, rely=0, anchor='n')
    player.play()
    logo_resize = Image.open("Apex_logo_actual.png")
    logo = ImageTk.PhotoImage(logo_resize)
    describe_resized = Image.open("Describe.png")
    describe_resized = describe_resized.resize((600, 200), Image.ANTIALIAS)
    describe = ImageTk.PhotoImage(describe_resized)
    canvas.create_image(0, 0, anchor='center', image=logo)
    canvas.create_image(500, 400, anchor='center', image=describe)
    root.update()


# displays the text and shows the video on the screen for slide2
def show_vid2():
    #  my_label = tkinter.Label(root)
    #  my_label.pack()
    player = tkvideo.tkvideo("Media2.mov", vid_slide2, loop=1, size=(600, 325))
    vid_slide2.place(relx=0.5, rely=0, anchor='n')
    player.play()
    logo_resize = Image.open("Apex_logo_actual.png")
    logo = ImageTk.PhotoImage(logo_resize)
    describe_resized = Image.open("Describe.png")
    describe_resized = describe_resized.resize((600, 200), Image.ANTIALIAS)
    describe = ImageTk.PhotoImage(describe_resized)
    canvas.create_image(0, 0, anchor='center', image=logo)
    canvas.create_image(500, 400, anchor='center', image=describe)
    root.update()


# main program, NOT CURRENTLY IN USE
def run():
    canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    root.update()
    incorrect_tries = {"slide1": [], "slide2": [], "slide3": [], "slide4": [], "slide5": []}

    engine.say("Please begin")
    engine.runAndWait()

    slide1_inc_tries = 0  # slide1_run()

    # same check of user input against correct inputs, for Slide 2
    slide2_inc_tries = 0

    slide2 = speech_to_text()
    slide2_inc_tries = 0
    exit_program(slide2)
    while slide2 != "packing bag" and slide2 != "choosing shirt" and slide2 != "eating breakfast":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide2_inc_tries += 1
        slide2 = speech_to_text()
        exit_program(slide2)
    engine.say("Correct")
    engine.runAndWait()
    incorrect_tries["slide2"].append(slide2_inc_tries)
    gen_performance_summary(slide2_inc_tries, "Slide 2")
    engine.say("Continue")
    engine.runAndWait()
    canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    root.update()

    # Slide 3 check
    slide3 = speech_to_text()
    slide3_inc_tries = 0
    exit_program(slide3)
    while slide3 != "boys playing soccer" and slide3 != "boys playing football" and \
            slide3 != "kicking ball" and slide3 != "soccer bag" and slide3 != "bag" and \
            slide3 != "football" and slide3 != "sneakers" and slide3 != "t-shirts":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide3_inc_tries += 1
        slide3 = speech_to_text()
        exit_program(slide3)
    engine.say("Correct")
    engine.runAndWait()
    incorrect_tries["slide3"].append(slide3_inc_tries)
    gen_performance_summary(slide3_inc_tries, "Slide 3")
    engine.say("Continue")
    engine.runAndWait()
    canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    root.update()

    # Slide 4 check
    slide4 = speech_to_text()
    slide4_inc_tries = 0
    exit_program(slide4)
    while slide4 != "family shopping" and slide4 != "family in the supermarket" and \
            slide4 != "family buying food" and slide4 != "avocado" and slide4 != "bananas" and \
            slide4 != "strawberries" and slide4 != "carrots":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide4_inc_tries += 1
        slide4 = speech_to_text()
        exit_program(slide4)
    engine.say("Correct")
    engine.runAndWait()
    incorrect_tries["slide4"].append(slide4_inc_tries)
    gen_performance_summary(slide4_inc_tries, "Slide 4")
    engine.say("Continue")
    engine.runAndWait()
    canvas.create_text(150, 10, text="To exit program at any time, please say 'Exit Program'")
    root.update()

    # Slide 5 check
    slide5 = speech_to_text()
    slide5_inc_tries = 0
    exit_program(slide5)
    print("5 " + slide5)
    while slide5 != "boys playing baseball" and slide5 != "baseball game" and \
            slide5 != "pitching" and slide5 != "hitting" and slide5 != "swinging" and \
            slide5 != "helmet" and slide5 != "bat" and slide5 != "glove" and slide5 != "ball":
        engine.say("Incorrect. Try again")
        engine.runAndWait()
        slide5_inc_tries += 1
        slide5 = speech_to_text()
    engine.say("Correct")
    engine.runAndWait()
    incorrect_tries["slide5"].append(slide5_inc_tries)
    gen_performance_summary(slide5_inc_tries, "Slide 5")

    # generates overall performance summary with # of incorrect tries for each slide
    canvas.create_text(300, 50, text="Performance Summary")
    canvas.create_text(25, 100, text="Slide")
    canvas.create_text(125, 100, text="Number of Incorrect Tries")
    canvas.create_text(25, 150, text="Slide 1")
    canvas.create_text(25, 200, text="Slide 2")
    canvas.create_text(25, 250, text="Slide 3")
    canvas.create_text(25, 300, text="Slide 4")
    canvas.create_text(25, 350, text="Slide 5")
    canvas.create_text(125, 150, text=incorrect_tries["slide1"])
    canvas.create_text(125, 200, text=incorrect_tries["slide2"])
    canvas.create_text(125, 250, text=incorrect_tries["slide3"])
    canvas.create_text(125, 300, text=incorrect_tries["slide4"])
    canvas.create_text(125, 350, text=incorrect_tries["slide5"])
    canvas.create_text(25, 400, text="Overall")
    all_incorrect_tries = slide1_inc_tries + slide2_inc_tries + slide3_inc_tries + \
                          slide4_inc_tries + slide5_inc_tries
    canvas.create_text(125, 400, text=all_incorrect_tries)
    root.update()
    time.sleep(5)
    canvas.delete('all')


# generates performance summary after each slide with # of incorrect tries
def gen_performance_summary(incorrect_tries, slide_num):
    canvas.create_text(300, 50, text="Performance Summary for " + slide_num)
    canvas.create_text(75, 100, text="Number of Incorrect Tries:")
    canvas.create_text(160, 100, text=incorrect_tries)
    root.update()
    time.sleep(1)
    # clears canvas for next performance summary
    canvas.delete('all')


# THE PROBLEM IS BELOW
thread1 = threading.Thread(target=show_vid1)
thread2 = threading.Thread(target=slide1_run)
thread3 = threading.Thread(target=show_vid2)
thread4 = threading.Thread(target=slide2_run)


def begin_all():
    thread1.start()
    thread2.start()
    # slide2_wrapper()


# I want to be able to start threads 3 and 4 when 1 and 2 end ... but I don't
# know how to do this, because I think thread1 never ends (keeps playing video).
# How do I manually kill thread 1 so that I can move on to these threads?
# And how do I know when thread 2 ends so that I can kill of thread 1 at that time?
def slide2_wrapper():
    thread3.start()
    thread4.start()


# create canvas, button, and title. Runs main loop.
canvas = tkinter.Canvas(root, height=450, width=1000)
canvas.pack()
run_prog = tkinter.Button(root, text="Run Program", padx=10, pady=10,
                          fg="white", bg="black", command=begin_all)
root.title("Performance Tracker")
run_prog.pack()
my_label = tkinter.Label(root)
my_label.pack()
vid_slide2 = tkinter.Label(root)
vid_slide2.pack()

root.mainloop()
