"""
2023 11/29 and 12/10
1445 جُمَادَىٰ ٱلْأُولَىٰ 15

Before Starting:
I am taking ACT, and I was like "I gotta train my mind to Automatically phase the test
by practicing with timer with given interval per question and passage".
So ,yes that is the program I will be building this time, ACT PHASER to train mind's time clock.

PROJECT: ACT PHASER

Plan:
1. Make basic timer on run window - # for testing
2. Make a tkinter option for each subject on main panel
3. Make each subject with its own page with adjustable phaser
4. Make functions for each ACT test timer, or maybe only one function
5. Assign and connect the code with tkinter interface
6. Clean Code
7. (optional) - Make exe file and Play Store runnable app, - apple is too expensive to upload for fun
"""

import customtkinter
import time
import pygame

pygame.mixer.init()

# tkinter basic frame
app = customtkinter.CTk()
app.geometry("600x800")
app.title("ACT Phaser")
app.resizable(False, False)


# functions
def short_timer():
    pygame.mixer.music.load('mixkit-flute-alert-2307.wav')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)


def session_end():
    pygame.mixer.music.load('mixkit-bell-tick-tock-timer-1046-[AudioTrimmer.com].wav')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)


def English():
    English_Testing = customtkinter.CTkToplevel()
    English_Testing.title('English_Testing')
    English_Testing.geometry('400x200')
    English_Testing.resizable(False, False)

    Time_Lapse = customtkinter.StringVar()
    Time_Lapse.set("0")

    def English_Timer():
        Questions = 0
        while Questions <= 75:
            Questions += 1
            seconds = 36
            short_timer()
            while seconds != 0:
                Time_Lapse.set(str(f'{Questions} - {seconds}'))
                English_Testing.update()
                time.sleep(1)
                seconds -= 1
        session_end()

    Background_timer = customtkinter.CTkLabel(master=English_Testing, text="", bg_color='#0D1117', width=400,
                                              height=400)
    Background_timer.place(x=0, y=0)

    Time_Label = customtkinter.CTkLabel(master=English_Testing, textvariable=Time_Lapse, fg_color='#0D1117',
                                        font=customtkinter.CTkFont(family='Consolas', size=50))
    Time_Label.place(x=125, y=65)

    English_Timer()


def Math():
    Math_Testing = customtkinter.CTkToplevel()
    Math_Testing.title('Math_Testing')
    Math_Testing.geometry('400x200')
    Math_Testing.resizable(False, False)

    Time_Lapse = customtkinter.StringVar()
    Time_Lapse.set("0")

    def Math_Timer():
        Questions = 0
        while Questions <= 60:
            Questions += 1
            seconds = 60
            short_timer()
            while seconds != 0:
                Time_Lapse.set(str(f'{Questions} - {seconds}'))
                Math_Testing.update()
                time.sleep(1)
                seconds -= 1
        session_end()

    Background_timer = customtkinter.CTkLabel(master=Math_Testing, text="", bg_color='#0D1117', width=400,
                                              height=400)
    Background_timer.place(x=0, y=0)

    Time_Label = customtkinter.CTkLabel(master=Math_Testing, textvariable=Time_Lapse, fg_color='#0D1117',
                                        font=customtkinter.CTkFont(family='Consolas', size=50))
    Time_Label.place(x=125, y=65)

    Math_Timer()


def Reading_1():
    Read_1_Testing = customtkinter.CTkToplevel()
    Read_1_Testing.title('Math_Testing')
    Read_1_Testing.geometry('400x200')
    Read_1_Testing.resizable(False, False)

    Time_Lapse = customtkinter.StringVar()
    Time_Lapse.set("0")

    def Read_1_Timer():
        x = 0
        while x < 3:
            x += 1
            passage = 0
            while passage < 1:
                passage += 1
                seconds = 300
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{x} - {seconds}'))
                    Read_1_Testing.update()
                    time.sleep(1)
                    seconds -= 1
            Questions = 0
            while Questions <= 9:
                Questions += 1
                seconds = 22
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{Questions} - {seconds}'))
                    Read_1_Testing.update()
                    time.sleep(1)
                    seconds -= 1
        session_end()

    Background_timer = customtkinter.CTkLabel(master=Read_1_Testing, text="", bg_color='#0D1117', width=400,
                                              height=400)
    Background_timer.place(x=0, y=0)

    Time_Label = customtkinter.CTkLabel(master=Read_1_Testing, textvariable=Time_Lapse, fg_color='#0D1117',
                                        font=customtkinter.CTkFont(family='Consolas', size=50))
    Time_Label.place(x=125, y=65)

    Read_1_Timer()


def Reading_2():
    Read_2_Testing = customtkinter.CTkToplevel()
    Read_2_Testing.title('Math_Testing')
    Read_2_Testing.geometry('400x200')
    Read_2_Testing.resizable(False, False)

    Time_Lapse = customtkinter.StringVar()
    Time_Lapse.set("0")

    def Read_2_Timer():
        x = 0
        while x < 3:
            x += 1
            passage = 0
            while passage < 1:
                passage += 1
                seconds = 180
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{x} - {seconds}'))
                    Read_2_Testing.update()
                    time.sleep(1)
                    seconds -= 1
            Questions = 0
            while Questions <= 9:
                Questions += 1
                seconds = 34
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{Questions} - {seconds}'))
                    Read_2_Testing.update()
                    time.sleep(1)
                    seconds -= 1
        session_end()

    Background_timer = customtkinter.CTkLabel(master=Read_2_Testing, text="", bg_color='#0D1117', width=400,
                                              height=400)
    Background_timer.place(x=0, y=0)

    Time_Label = customtkinter.CTkLabel(master=Read_2_Testing, textvariable=Time_Lapse, fg_color='#0D1117',
                                        font=customtkinter.CTkFont(family='Consolas', size=50))
    Time_Label.place(x=125, y=65)

    Read_2_Timer()


def Science():
    Science_Testing = customtkinter.CTkToplevel()
    Science_Testing.title('Math_Testing')
    Science_Testing.geometry('400x200')
    Science_Testing.resizable(False, False)

    Time_Lapse = customtkinter.StringVar()
    Time_Lapse.set("0")

    def Science_Timer():
        x = 0
        while x < 5:
            x += 1
            passage = 0
            while passage < 1:
                passage += 1
                seconds = 90
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{x} - {seconds}'))
                    Science_Testing.update()
                    time.sleep(1)
                    seconds -= 1
            Questions = 0
            while Questions <= 9:
                Questions += 1
                seconds = 38.67
                short_timer()
                while seconds != 0:
                    Time_Lapse.set(str(f'{Questions} - {seconds}'))
                    Science_Testing.update()
                    time.sleep(1)
                    seconds -= 1
        session_end()

    Background_timer = customtkinter.CTkLabel(master=Science_Testing, text="", bg_color='#0D1117', width=400,
                                              height=400)
    Background_timer.place(x=0, y=0)

    Time_Label = customtkinter.CTkLabel(master=Science_Testing, textvariable=Time_Lapse, fg_color='#0D1117',
                                        font=customtkinter.CTkFont(family='Consolas', size=50))
    Time_Label.place(x=125, y=65)

    Science_Timer()


# main menu
Background = customtkinter.CTkLabel(master=app, text="", bg_color='#0D1117', width=600, height=800)
Title = customtkinter.CTkLabel(master=app, text="ACT-PHASER", bg_color="#0D1117", width=10, height=10,
                               font=customtkinter.CTkFont(family="Segoe UI", size=50))
sub_Title = customtkinter.CTkLabel(master=app, text="Built by moy2004",
                                   bg_color="#0D1117", width=10, height=10,
                                   font=customtkinter.CTkFont(family="Segoe UI", size=13))
line = customtkinter.CTkFrame(master=app, bg_color='#30363D', width=500, height=1)

Background_Eng = customtkinter.CTkLabel(master=app, text="", bg_color="#161B22", width=500, height=120)
Button_1_Eng = customtkinter.CTkButton(master=app, text="start", width=100, height=25, corner_radius=0,
                                       text_color="#79C0FF", fg_color='#161B22', hover_color='#79C0FF',
                                       font=customtkinter.CTkFont(family='Consolas'), command=English)
Eng_Title = customtkinter.CTkLabel(master=app, text="English", text_color="#D2A8FF", fg_color='#161B22',
                                   font=customtkinter.CTkFont(family='Consolas', size=15))
Eng_Timing = customtkinter.CTkLabel(master=app, text="[75Q / 45M] ", fg_color='#161B22', text_color="#D2A8FF",
                                    font=customtkinter.CTkFont(family='Consolas', size=15))
Eng_1_Dec = customtkinter.CTkLabel(master=app, justify='left',
                                   text="Solve and Reading: 36 seconds per question\n\n"
                                        "Tip: even if you are sure the answer is correct\n"
                                        "use given time to rethink mutiple time then move",
                                   fg_color='#161B22', font=customtkinter.CTkFont(family='Consolas', size=15))

Background_Math = customtkinter.CTkLabel(master=app, text="", bg_color="#161B22", width=500, height=120)
Button_1_Math = customtkinter.CTkButton(master=app, text="start", width=100, height=25, corner_radius=0,
                                        text_color="#79C0FF", fg_color='#161B22', hover_color='#79C0FF',
                                        font=customtkinter.CTkFont(family='Consolas'), command=Math)
Math_Title = customtkinter.CTkLabel(master=app, text="Math", text_color="#FFA64D", fg_color='#161B22',
                                    font=customtkinter.CTkFont(family='Consolas', size=15))
Math_Timing = customtkinter.CTkLabel(master=app, text="[60Q / 60M] ", fg_color='#161B22', text_color="#FFA64D",
                                     font=customtkinter.CTkFont(family='Consolas', size=15))
Math_1_Dec = customtkinter.CTkLabel(master=app, justify='left',
                                    text="Equal Focus: 60 seconds per question.\n\nTip: try to solve first 30Q in "
                                         "20m  \nthen spend minute per question",
                                    fg_color='#161B22', font=customtkinter.CTkFont(family='Consolas', size=15))

Background_Read = customtkinter.CTkLabel(master=app, text="", bg_color="#161B22", width=500, height=120)
Button_1_Read = customtkinter.CTkButton(master=app, text="start-1", width=100, height=25, corner_radius=0,
                                        text_color="#79C0FF", fg_color='#161B22', hover_color='#79C0FF',
                                        font=customtkinter.CTkFont(family='Consolas'), command=Reading_1)
Button_2_Read = customtkinter.CTkButton(master=app, text="start-2", width=100, height=25, corner_radius=0,
                                        text_color="#79C0FF", fg_color='#161B22', hover_color='#79C0FF',
                                        font=customtkinter.CTkFont(family='Consolas'), command=Reading_2)
Read_Title = customtkinter.CTkLabel(master=app, text="Reading", text_color="#39D353", fg_color='#161B22',
                                    font=customtkinter.CTkFont(family='Consolas', size=15))
Read_Timing = customtkinter.CTkLabel(master=app, text="[45Q / 35M] ", fg_color='#161B22', text_color="#39D353",
                                     font=customtkinter.CTkFont(family='Consolas', size=15))
Read_1_Dec = customtkinter.CTkLabel(master=app, justify='left',
                                    text="Passage Focus: 5 minutes passage,\n22 seconds per question",
                                    fg_color='#161B22', font=customtkinter.CTkFont(family='Consolas', size=15))
Read_2_Dec = customtkinter.CTkLabel(master=app, justify='left',
                                    text="Question Focus: 3 minutes passage,\n34 seconds per question",
                                    fg_color='#161B22', font=customtkinter.CTkFont(family='Consolas', size=15))

Background_Sci = customtkinter.CTkLabel(master=app, text="", bg_color="#161B22", width=500, height=120)
Button_1_Sci = customtkinter.CTkButton(master=app, text="start", width=100, height=25, corner_radius=0,
                                       text_color="#79C0FF", fg_color='#161B22', hover_color='#79C0FF',
                                       font=customtkinter.CTkFont(family='Consolas'), command=Science)
Sci_Title = customtkinter.CTkLabel(master=app, text="Science", text_color="#79C0FF", fg_color='#161B22',
                                   font=customtkinter.CTkFont(family='Consolas', size=15))
Sci_Timing = customtkinter.CTkLabel(master=app, text="[45Q / 35M] ", fg_color='#161B22', text_color="#79C0FF",
                                    font=customtkinter.CTkFont(family='Consolas', size=15))
Sci_1_Dec = customtkinter.CTkLabel(master=app, justify='left',
                                   text="Balanced phased: 1m 30sec passage\n"
                                        "38.67 seconds per questions\n"
                                        "Enter how many question are in each passage:",
                                   fg_color='#161B22', font=customtkinter.CTkFont(family='Consolas', size=15))

# main menu - placing
Background.place(x=0, y=0)
Title.place(x=52.5, y=65)
sub_Title.place(x=52.5, y=125)
line.place(x=50, y=150)

Background_Eng.place(x=50, y=160)
Button_1_Eng.place(x=440, y=180)
Eng_Title.place(x=60, y=160)
Eng_Timing.place(x=125, y=160)
Eng_1_Dec.place(x=60, y=190)

Background_Math.place(x=50, y=290)
Button_1_Math.place(x=440, y=310)
Math_Title.place(x=60, y=290)
Math_Timing.place(x=100, y=290)
Math_1_Dec.place(x=60, y=320)

Background_Read.place(x=50, y=420)
Button_1_Read.place(x=440, y=440)
Button_2_Read.place(x=440, y=480)
Read_Title.place(x=60, y=420)
Read_Timing.place(x=125, y=420)
Read_1_Dec.place(x=60, y=450)
Read_2_Dec.place(x=60, y=490)

Background_Sci.place(x=50, y=550)
Button_1_Sci.place(x=440, y=570)
Sci_Title.place(x=60, y=550)
Sci_Timing.place(x=125, y=550)
Sci_1_Dec.place(x=60, y=580)

# launching tkinter
app.mainloop()

"""
After Project Note:
⚠️⚠️⚠️ Writing a lot of UI code without classes and in single .py file with 
global variables like it's often done is a pain to read and very bad coding style!

Found this after I was done with UI coding, :/ Good lesson for next time -> explore library instruction first

After Project Review:
It was fun project XD

"""
