import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import csv, time

video_name = "D:\BCI\sample-1.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def retrieve_input(textBox):
    #inputValue = textBox.get("1.0", "end-1c")
    #write_to_file(inputValue)
    write_to_file(textBox)
    #print(inputValue)

def write_to_file(textBox):
    with open('demo.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        print(textBox.get(), "I'm wrting this")
        w.writerow([textBox.get(), time.time()])
def write_to_file1(data):
    '''Get a list of all users and write it to the csv file'''

    with open('demo.csv', 'wb') as f:
        for line in data:
            f.write(line)
        #w = csv.writer(f, quoting=csv.QUOTE_ALL)
        #w.writerow([data])

        # writer = csv.writer(f)
        # for row in data:
        #     row = str(row)
        # writer.writerows(data)
def video_utility(label):
    print("Begin video_utility")
    for image in video.iter_data():
        image = Image.fromarray(image)
        image = image.resize((900,600),Image.ANTIALIAS)
        #frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        frame_image = ImageTk.PhotoImage(image)
        label.config(image=frame_image)
        label.image = frame_image
    print("End video_utility")

def play_video(label):
    print("Begin play_video")
    thread = threading.Thread(target=video_utility, args=(label,))
    thread.daemon = 1
    thread.start()
    print("End play_video")

if __name__ == "__main__":
    print("Begin main")
    root = tk.Tk()
    root.title("BCI Experimentation")
    root.geometry("900x700")
    my_label = tk.Label(root)
    my_label.pack()
    #my_label.grid(row=0)

    ButtonPlay = tk.Button(root, text="Begin Experiment",height = 3, width = 40, command= lambda: play_video(my_label))
    ButtonPlay.pack()
    #textBox = tk.Text(root, height = 1, width = 10)
    #textBox.pack()
    buttonEnter = tk.Button(root, height=1, width=10, text="Enter", command=lambda: retrieve_input(textBox))
    buttonEnter.pack(side="bottom")
    textBox = tk.Entry(root, width = 10)
    textBox.pack(side = "bottom")

    root.mainloop()
    print("End main")