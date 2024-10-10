import tkinter as tk
from tkinter import messagebox
import pygame
import random
import words
def game():
    # Create the main window
    root = tk.Tk()
    root.state("zoomed")
    root.title("Wordle Game")
    #root.geometry("1300x700")
    root.configure(background="thistle")
    def wordlegame():
        global correct_guess
        global word_list
        global hint

        #words According to categorie wise
        words_hint={"ANIMAL":["bison","hyena","Lemur","Eagle","sheep","hippo","skunk","gecko"],
                    "MOVIE":["actor","scene","media","clips"],"BODY":["navel","scalp","veins","wrist","waist"],
                    "COUNTRY":["spain","libya","kenya","tongo","benin","eygpt","italy"],
                    "HARD MATERIALS":["Steel","Grind","Ferrs","Anvil","Slabs","Knurl","Grits"],
                    "NATURE":["Roots","Rocks","Petal","Strom","Horns","claws","Peaks","Tides","Water","Gases","Winds","Cloud"],
                    "SCIENCE":["Nerve","Genes","optic","force","Radio","Metal","Atoms","Catal","Bonds","Spore","Fluid","Oxide","React","Brain"],
                    "TECHNOLOGY":["Bytes","Codes","Graph","Debug","Datas","Virus","Robot","Model","Train"],
                    "SCHOOL":["Class","Study","Grade","Teach","Books","Learn","Chair"],
                    "FARMER":["Barns","Rural","Sowed","Flock","Hilly","Thresh","Grain"]}
        
        hint,item=random.choice(list(words_hint.items()))       #generates random words.

        word_list = words.WORDS   
        correct_guess = random.choice(item)
        correct_guess = correct_guess.upper()
        print(correct_guess)
        alpha = [" "]*30

        heading = tk.Label(root, width=40, bg="thistle", font=("arial", 20, "bold"), text="\tWORDLE\t",padx=12)
        heading.grid(row=0, column=0)

        frame = tk.Frame(root, bg="powder Blue", bd=5, width=1300, height=700, relief=tk.RAISED)
        frame.grid(row=7, column=0, padx=30)

        keys = [["A", "B", "C", "D", "HINT","E","F","G", "H", "I"], 
                ["J","K", "L", "M", "N", "O", "P", "Q", "R", "S"], 
                ["T", "Enter", "U", "V", "W", "X", "Y", "Z", "Back","Exit"]]   #keyboard

        input_guess = str()
        attempt = 1

        def input_button1(key):
            nonlocal input_guess
            pygame.mixer.init()
            pygame.mixer.music.load("buttonsound.mp3")
            pygame.mixer.music.play()
            if key == "Enter":
                if len(input_guess) == 5 :
                    if input_guess.lower() in word_list :
                        guess(input_guess)
                        input_guess = str()
                        display.delete(0, tk.END)
                        display.insert(0, input_guess)
                    else:
                        input_guess = str()
                        display.delete(0, tk.END)
                        display.insert(0, input_guess)
                        messagebox.showwarning("Warning", "Enter the Meaningful word")
                    
                else:
                    messagebox.showwarning("Warning", "ENTER THE 5 LETTER WORD")
            elif key == "HINT":
                messagebox.showinfo("HINT","The word is related to {}".format(hint))
            elif key =="Exit":
                root.destroy()
            elif key == "Back":
                input_guess = input_guess[:-1]
                display.delete(0, tk.END)
                display.insert(0, input_guess)
            else:
                current = display.get()
                display.delete(0, tk.END)
                display.insert(0, str(current) + str(key))
                input_guess += key

        for i, key_row in enumerate(keys):
            for j, key in enumerate(key_row):
                tk.Button(frame, bg="lavender", font=("arial", 14, "bold"), text=key, width=9, height=2, command=lambda key=key: input_button1(key)).grid(row=i, column=j)

        frames = tk.Frame(root, bg="light blue", bd=5, width=1300, height=700, relief=tk.RIDGE)
        frames.grid(row=1, column=0, padx=10)

        rowchange = 0
        change = 0
        while change < 30:
            for columnchange in range(5):
                tk.Button(frames, font=("arial", 14, "bold"), text=alpha[change], width=10, height=2).grid(row=1+rowchange, column=0+columnchange)
                change += 1
            rowchange += 1

        display = tk.Entry(frames, font=("arial", 20, "bold"), bd=5, width=8)
        display.grid(row=4+rowchange, column=0+columnchange, pady=10)

        def condition_check(user_guess):
            nonlocal attempt
            for i in range(len(user_guess)):
                if user_guess[i] in correct_guess:
                    if user_guess[i] == correct_guess[i]:
                        tk.Button(frames, bg="light green", font=("arial", 14, "bold"), text=user_guess[i], width=10, height=2).grid(row=attempt, column=i)
                        for k, key_row in enumerate(keys):
                            for j, key in enumerate(key_row):
                                if key == user_guess[i]:
                                    tk.Button(frame, bg="light green", font=("arial", 14, "bold"), text=key, width=9, height=2, command=lambda key=key: input_button1(key)).grid(row=k, column=j)
                    else:
                        tk.Button(frames, bg="yellow", font=("arial", 14, "bold"), text=user_guess[i], width=10, height=2).grid(row=attempt, column=i)
                        for k, key_row in enumerate(keys):
                            for j, key in enumerate(key_row):
                                if key == user_guess[i]:
                                    tk.Button(frame, bg="yellow", font=("arial", 14, "bold"), text=key, width=9, height=2, command=lambda key=key: input_button1(key)).grid(row=k, column=j)
                else:
                    tk.Button(frames, bg="red", font=("arial", 14, "bold"), text=user_guess[i], width=10, height=2).grid(row=attempt, column=i)
                    for k, key_row in enumerate(keys):
                        for j, key in enumerate(key_row):
                            if key == user_guess[i]:
                                tk.Button(frame, bg="red", font=("arial", 14, "bold"), text=key, width=9, height=2, command=lambda key=key: input_button1(key)).grid(row=k, column=j)

        def guess(user_guess):
            nonlocal attempt
            global but
            global label3
            global frame_win
            if user_guess == correct_guess:
                for i in range(len(user_guess)):
                    tk.Button(frames, bg="light green", font=("arial", 14, "bold"), text=user_guess[i], width=10, height=2).grid(row=attempt, column=i)
                    for k, key_row in enumerate(keys):
                        for j, key in enumerate(key_row):
                            if key == user_guess[i]:
                                tk.Button(frame, bg="light green", font=("arial", 14, "bold"), text=key, width=9, height=2, command=lambda key=key: input_button1(key)).grid(row=k, column=j)
                frames.destroy()
                frame.destroy()
                frame_win = tk.Frame(root,width=1400,height=800)
                frame_win.grid(row=0, column=0, padx=10)
                photos = tk.PhotoImage(file=r"congrats.png")
                label3 = tk.Label(frame_win,image=photos)
                label3.pack()
                but = tk.Frame(root,width=300,height=50,bg="blue").grid(row=2,column=0)
                exit_buttons = tk.Button(but, font=("arial", 40, "bold"), text="Exit", command=exit_game)
                exit_buttons.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
                play_congrtassound()
                root.mainloop()
            
            else:
                if attempt == 6:
                    condition_check(user_guess)
                    frames.destroy()
                    frame.destroy()
                    frame_loss = tk.Frame(root,width=1400,height=800)
                    frame_loss.grid(row=0, column=0, padx=10)
                    photos1 = tk.PhotoImage(file="sorry_ss3.png")
                    label4 = tk.Label(frame_loss,width=1300,height=700,image=photos1)
                    label4.pack()
                    but = tk.Frame(root,width=300,height=50,bg="blue").grid(row=2,column=0)
                    message= tk.Button(but,bg="light pink",font=("arial",30,"bold"),text="SORRY!!! Better luck next time\n the exact answer is {}".format(correct_guess))
                    exit_buttons = tk.Button(but, font=("arial", 40, "bold"), text="Exit", command=exit_game)
                    play_sorrysound()
                    message.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                    exit_buttons.place(relx=0.8, rely=0.8, anchor=tk.CENTER)
                    playagain_buttons = tk.Button(but,bg="LightSkyBlue1",font=("arial", 40, "bold"), text="playagain", command=setup_wordle_game)
                    playagain_buttons.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
                    root.mainloop()
                else:
                    condition_check(user_guess)
            attempt += 1
        root.mainloop()
    def hint_reveal():
        tk.Button(root,bg="brown",font=("arial", 14, "bold"), text="The word is related to {}".format(hint)).grid(row=0,column=0)
    def levels():
        global label7
        label.destroy()
        photo_path7 = "levels_ss1.png"
        try:
            photo7 = tk.PhotoImage(file=photo_path7)
            label7 = tk.Label(root,width=1300,height=700,image=photo7)
            label7.pack()
        except tk.TclError:
            messagebox.showerror("Error", f"Failed to load image from {photo_path7}")
        easy = tk.Button(root, bg="salmon",font=("arial", 40, "bold"), text="EASY", command=setup_wordle_game)
        medium = tk.Button(root,bg="salmon",font=("arial", 40, "bold"), text="MEDIUM", command=setup_wordle_game)
        hard = tk.Button(root,bg="salmon", font=("arial", 40, "bold"), text="HARD", command=setup_wordle_game)
        exitlevel =tk.Button(root,bg="MediumPurple1", font=("arial", 30, "bold"), text="EXIT", command=exit_game)
        easy.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        medium.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        hard.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        exitlevel.place(relx=0.8, rely=0.8, anchor=tk.CENTER)
        root.mainloop()
        
    def buttons():
        start_button = tk.Button(root, font=("arial", 20, "bold"), text="Start", command=start_game)
        instructions_button = tk.Button(root, font=("arial", 20, "bold"), text="Instructions", command=show_instructions)
        exit_button = tk.Button(root, font=("arial", 20, "bold"), text="Exit", command=exit_game)
        start_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        instructions_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
        exit_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
        root.mainloop()

    def goto_home():
        global label
        global label3
        photo_path = "homepage_ss.png"
        try:
            photo = tk.PhotoImage(file=photo_path)
            label = tk.Label(root,width=1300,height=700,image=photo)
            label.pack()
        except tk.TclError:
            messagebox.showerror("Error", f"Failed to load image from {photo_path}")
        buttons()
        root.mainloop()

    def setup_wordle_game():
        label7.destroy()
        pygame.mixer.init()
        pygame.mixer.music.load("buttonsound.mp3")
        pygame.mixer.music.play()
        for widget in root.winfo_children():
            widget.destroy()
        wordlegame()

    def play_sorrysound():
        pygame.mixer.init()
        pygame.mixer.music.load("sorry_audio.mp3")
        pygame.mixer.music.play()

    def play_congrtassound():
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\yashw\OneDrive\Desktop\wordle project\congarts_audio (1).mp3")
        pygame.mixer.music.play()

    def start_game():
        pygame.mixer.init()
        pygame.mixer.music.load("buttonsound.mp3")
        pygame.mixer.music.play()
        levels()

    def show_instructions():
        pygame.mixer.init()
        pygame.mixer.music.load("buttonsound.mp3")
        pygame.mixer.music.play()
        global label
        global label1
        label.destroy()
        photo_paths = "instructions_ss2.png"
        try:
            photos = tk.PhotoImage(file=photo_paths)
            label1 = tk.Label(root,width =1300,height = 700,bg="white",image=photos)
            label1.pack()
        except tk.TclError:
            messagebox.showerror("Error", f"Failed to load image from {photo_paths}")
        exit_buttons = tk.Button(root,bg="light pink",font=("arial", 40, "bold"), text="Exit", command=exit_instruction)
        exit_buttons.place(relx=0.8, rely=0.85, anchor=tk.CENTER)
        root.mainloop()

    def exit_instruction():
        label1.destroy()
        goto_home()
        root.mainloop()

    def exit_game():
        pygame.mixer.init()
        pygame.mixer.music.load("buttonsound.mp3")
        pygame.mixer.music.play()
        root.destroy()
    goto_home()
    root.mainloop()
game()
