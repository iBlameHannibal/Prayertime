import requests
from tkinter import *

def get_prayer_times(city):
    url = f'https://api.aladhan.com/v1/timingsByCity?city={city}&country=Libya&method=2'
    response = requests.get(url)
    data = response.json()
    return data['data']['timings']

class PrayerTimesApp:
    def __init__(self, master):
        self.master = master
        master.title('Prayer Times in Libya')
        master.geometry('400x300')  # Increase the window size

        # Set background color
        master.configure(bg='#F4F4F4')

        self.city_label = Label(master, text='Enter City:', bg='#F4F4F4', font=('Arial', 12))
        self.city_label.grid(row=0, column=0, pady=10, padx=10)

        self.city_entry = Entry(master, font=('Arial', 12))
        self.city_entry.grid(row=0, column=1, pady=10, padx=10)

        self.get_times_button = Button(master, text='Get Prayer Times', command=self.display_prayer_times, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.get_times_button.grid(row=0, column=2, pady=10, padx=10)

        self.prayer_times_label = Label(master, text='', font=('Arial', 14), bg='#F4F4F4')
        self.prayer_times_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

    def display_prayer_times(self):
        city = self.city_entry.get()
        if not city:
            self.prayer_times_label.config(text='Please enter a city.')
            return

        prayer_times = get_prayer_times(city)

        times_text = "Prayer Times for {}: \n".format(city.capitalize())
        times_text += "\n".join([f"{prayer}: {time}" for prayer, time in prayer_times.items()])

        self.prayer_times_label.config(text=times_text)

if __name__ == "__main__":
    root = Tk()
    app = PrayerTimesApp(root)
    root.mainloop()

