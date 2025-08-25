from tkinter import *
from tkinter import ttk
import requests 
from PIL import Image, ImageTk

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=98573e7474bd5eb0d4da2d07d642bd49").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("600x500")  # Adjusted window size for better layout

# Load and display the image
image = Image.open("C:/Users/Roshn/Downloads/Screenshot 2023-12-14 230509.png")
photo = ImageTk.PhotoImage(image)

image_label = Label(win, image=photo)
image_label.image = photo
image_label.place(x=50, y=50)  # Adjusted image position

# Other widgets and labels with adjusted positions and styling
name_label = Label(win, text="Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=200, y=20)

city_name = StringVar()
com = ttk.Combobox(win, values=city_name, font=("Times New Roman", 14), textvariable=city_name)
com.place(x=200, y=300, width=200)

# Adjusted positions and styles for weather information labels
w_label = Label(win, text="Weather Climate:", font=("Times New Roman", 15))
w_label.place(x=350, y=100)
w_label1 = Label(win, text="", font=("Times New Roman", 15))
w_label1.place(x=500, y=100)

wb_label = Label(win, text="Weather Description:", font=("Times New Roman", 15))
wb_label.place(x=350, y=150)
wb_label1 = Label(win, text="", font=("Times New Roman", 15))
wb_label1.place(x=500, y=150)

temp_label = Label(win, text="Temperature:", font=("Times New Roman", 15))
temp_label.place(x=350, y=200)
temp_label1 = Label(win, text="", font=("Times New Roman", 15))
temp_label1.place(x=500, y=200)

per_label = Label(win, text="Pressure:", font=("Times New Roman", 15))
per_label.place(x=350, y=250)
per_label1 = Label(win, text="", font=("Times New Roman", 15))
per_label1.place(x=500, y=250)

done_button = Button(win, text="Done", font=("Times New Roman", 18, "bold"), command=data_get)
done_button.place(x=240, y=360, width=120)

win.mainloop()

"""
Software: Visual Studio.
Library: Tkinter


For ComboBox data : 
Step 1: google “india state name list python”  than
Step 2: go to https://pythoncircle.com/post/156/list-of-indian-states-in-python-format/
Step 3 : copy  “Python List of Indian states:
”
Step 4: paste in list_name
 For weather Report Data:
Step 1 : “Google Weather API”(Have to make a account)
Step 2:  go to https://openweathermap.org/api
Step 3: go to Currunt
 weather data
Step 4 :  Copy “API call”  https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


"""