import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '7a6460d2c045df374fb1b4fcd26e79d9'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind'] 
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = wind['speed']

        weather_info = (f"City: {city}\n"
                        f"Temperature: {temperature}°C\n"
                        f"Pressure: {pressure} hPa\n"
                        f"Humidity: {humidity}%\n"
                        f"Weather: {weather_desc}\n"
                        f"Wind Speed: {wind_speed} m/s")
        
        return weather_info
    else:
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        if weather_info:
            result_lable.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create the input field for city
city_entry = tk.Entry(root, width=50)
city_entry.pack(pady=50)

# Create the button to get weather
get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=5)

# Create the label to display weather information
result_lable = tk.Label(root, text="", justify='left')
result_lable.pack(pady=10)

# Run the main event loop
root.mainloop()