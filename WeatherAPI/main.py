from tkinter import *
import requests
from PIL import Image, ImageTk


class WeatherApi(object):

    def __init__(self, master):
        self.master = master

        # Background Image
        # image = Image.open("images.jpg")
        # image = image.resize(600, 500)
        # img_icon = ImageTk.PhotoImage((image), Image.Resampling.NEAREST)

        # labels
        self.img_lbl = Label(self.master, bg='lightblue')
        self.img_lbl.place(x=0, y=0, width=600, height=500)

        heading_lbl = Label(self.img_lbl, bg='lightblue', text="Earth including over 20,000 cities!", fg="red", background="lightblue", font="Times 15 bold")
        heading_lbl.place(x=80, y=40)

        # frames
        self.frame_top = Frame(self.img_lbl, bg='skyblue', borderwidth=10)
        self.frame_top.place(x=80, y=80, width=400, height=50)

        self.frame_bottom = Frame(self.img_lbl, bg='lightgreen', borderwidth=10)
        self.frame_bottom.place(x=80, y=150, width=400, height=300)

        # entry
        self.user_entry = Entry(self.frame_top, font="Time 15 bold", bg="pink", width=25)
        self.user_entry.grid(row=0, column=0, sticky=W)

        # Button
        self.search_btn = Button(self.frame_top, text="Get Weather", width=12, fg="green", font="times 10 bold", command=self.weather_gather)
        self.search_btn.grid(row=0, column=1, padx=10)

        # result label
        self.res_lbl = Label(self.frame_bottom, bg="white", font="Times 15", justify=LEFT, anchor='nw')
        self.res_lbl.place(relwidth=1, relheight=1)

    def weather_gather(self):

        apiKey = "7040ea904442a45d6950ba584410ce59"
        baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
        cityName = self.user_entry.get()
        try:
            completeURL = baseURL + cityName + "&appid=" + apiKey
            responce = requests.get(completeURL)
            data = responce.json()
            self.res_lbl['text'] = f"Name : {data['name']}\nWeather Condition : {data['weather'][0]['description']}\nTemperature : {data['main']['temp']} "
        except:
            self.res_lbl['text'] = "There is an error! could not retrieve data"

def main():
    root = Tk()
    app = WeatherApi(root)
    root.title("Weather App")
    root.geometry("600x500+350+100")
    root.mainloop()


if __name__ == '__main__':
    main()
