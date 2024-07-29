import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pyperclip
import keyboard
import time
import pyautogui
import cv2
import numpy as np
import os
import random
import mss

def email():
    while True:
     with open('emails.txt', 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)

     global line_bool
     global line_index

     if line_bool == True:
       line_index = line_index
     else:
      time.sleep(3)

      line_bool = True

      global line_number_entry

      line_start = int(line_number_entry.get())
      line_index = line_start

     monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

     threshold = 0.8

     window_title = "Rec Room"

     font = ImageFont.truetype("arial.ttf", 48)

     text_position = (400, 344)
     text_color = (255, 0, 0)
  
     color = (248,106,22)

     color2 = (186,43,38)

     color3 = (214,64,1)

     sscc = 0

     delay = 0.4

     if line_index == num_lines:
      break
      
     pyperclip.copy(lines[line_index].strip())
     print(f"Copied line {line_index+1}: {lines[line_index].strip()}")

     if '_' in lines[line_index].strip():
        line_index = (line_index + 1) % len(lines)
     else:

      reference_image1 = cv2.imread('template/SET.png', cv2.IMREAD_COLOR)

      screenshot1 = pyautogui.screenshot()
      screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

      result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

      min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

      if max_val1 > threshold:
        pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

      time.sleep(delay)

      email = (lines[line_index].strip())

      pyautogui.click()

      time.sleep(delay)

      reference_image1 = cv2.imread('template/ENTER.png', cv2.IMREAD_COLOR)

      screenshot1 = pyautogui.screenshot()
      screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

      result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

      min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

      if max_val1 > threshold:
        pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

      time.sleep(delay)

      pyautogui.click()

      time.sleep(delay)

      pyautogui.hotkey('ctrl', 'v')

      time.sleep(delay)

      reference_image1 = cv2.imread('template/SUBMIT.png', cv2.IMREAD_COLOR)

      screenshot1 = pyautogui.screenshot()
      screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

      result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

      min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

      if max_val1 > threshold:
         pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

      time.sleep(delay)

      pyautogui.click()

      time.sleep(delay)

      ref_image = cv2.imread('template/USE.png')

      screenshot = pyautogui.screenshot()

      img_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

      result = cv2.matchTemplate(img_cv, ref_image, cv2.TM_CCOEFF_NORMED)
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

      if max_val > 0.8:

        string = (email) + "\n"

        with open("AlreadyInUse.txt", "a") as f:
          f.write(string)

        reference_image1 = cv2.imread('template/BACK.png', cv2.IMREAD_COLOR)

        screenshot1 = pyautogui.screenshot()
        screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

        result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

        if max_val1 > threshold:
           pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

           time.sleep(delay)

           line_index = (line_index + 1) % len(lines)
      else:
        reference_image1 = cv2.imread('template/DONE.png', cv2.IMREAD_COLOR)

        screenshot1 = pyautogui.screenshot()
        screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

        result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

        if max_val1 > threshold:
           pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

           time.sleep(delay)

           pyautogui.click()

           time.sleep(1)

           line_index = (line_index + 1) % len(lines)

line_bool = False
line_index = 0

root = tk.Tk()
root.title("RecRoomEmailChecker")
root.configure(background="black")
root.geometry("474x355")
root.resizable(False, False)

background_image = Image.open("template/bg.jpg") 
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image  
background_label.place(x=0, y=0, relwidth=1, relheight=1)

line_number_label = tk.Label(root, text="Line Number:", fg="black", bg="white")
line_number_label.pack()
line_number_label.place(relx=0.5, rely=0.45, anchor="center")

line_number_entry = tk.Entry(root, width=60, fg="black", bg="white")
line_number_entry.pack()
line_number_entry.place(relx=0.5, rely=0.52, anchor="center")

button = tk.Button(root, text="Start", fg="black", bg="white", command=email)
button.pack()
button.place(relx=0.5, rely=0.6, anchor="center") 

root.mainloop()
