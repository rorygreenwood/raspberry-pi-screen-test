import os
import random
import time

import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

is_animating = False
min_animation_time = random.choice(range(5, 12))
print('min animation time atstart: ', min_animation_time)
print(type(min_animation_time))
def animate_gif(label, image_path):
    global is_animating
    is_animating = True
    print('animate gif called with:', image_path)
    gif_image = Image.open(image_path)

    all_frames = []
    for frame in ImageSequence.Iterator(gif_image):
        frame = frame.convert('RGBA')
        photo = ImageTk.PhotoImage(frame)
        all_frames.append(photo)
    print('new frames added')
    # Display the animation
    index = 0
    start_time = time.time()

    def animation(index):
        nonlocal start_time
        global is_animating
        global min_animation_time
        # print("Updating image:", index)
        label.configure(image=all_frames[index])
        index += 1
        if index == len(all_frames) - 1:
            end_time = time.time()
            elapsed_time = (end_time - start_time)
            if elapsed_time > min_animation_time:
                is_animating = False
                min_animation_time = random.choice(range(5, 12))
                print('min animation time: ', min_animation_time)
                root.after(100, update_label)
            else:
                index = 0
                is_animating = True
        if is_animating:
            label.after(35, lambda: animation(index))

    animation(index=index)

def update_label():
    global is_animating
    if not is_animating:
        image_path = "sprites/" + os.listdir('sprites')[random.randint(0, len(os.listdir('sprites')) - 1)]
        print("New image path:", image_path)
        animate_gif(label, image_path)
    else:
        root.after(100, update_label) 

root = tk.Tk()
root.geometry("100x100")
root.configure(background='black')
label = tk.Label(root, bg='black')
label.pack()

print('loading first one')
animate_gif(label, 'sprites/' + os.listdir('sprites')[0])
print('starting update')
update_label()
print('starting loop')
root.mainloop()