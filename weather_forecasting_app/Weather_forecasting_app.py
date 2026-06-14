import tkinter as tk
from tkinter import ttk
import requests

window = tk.Tk()
window.title("Weather forecasting app")  # عنوان النافذة
window.geometry("400x200")    # حجم النافذة


location_label = tk.Label(window, text="Location: ", font=("Arial", 10, "bold"))
location_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")


tk_entry = tk.Entry(window, width=25) #مكان ادخال اسم المدينة
tk_entry.grid(row=0, column=1, padx=10, pady=20, sticky="w")


info_label = tk.Label(window, text="", justify="left", font=("Arial", 10)) #معلومات الطقس
info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


def get_weather():
    city = tk_entry.get().lower().strip()
    api_key ="72fa312d37447f34cb2274221871f11c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"    
    response = requests.get(url)
    data = response.json()
    tk_entry.delete(0, tk.END)

    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        rain = data.get("rain", {}).get("1h", 0)

        if rain == 0:
            rain_text = "⛅ No measurable rain in the last hour"
        else:
            rain_text = f"🌧 Rain last hour: {rain} mm"

        info_label.config(text=(
        f"🌍 City: {city.title()}\n"
        f"🌡 Temperature: {temp:.1f} °C\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind Speed: {wind_speed} m/s\n"
        f"🔽 Pressure: {pressure} hPa\n"
        f"{rain_text}"))

    else:
        info_label.config(text="❌ City not found or error retrieving data.")

button = tk.Button(window, text="search",
                       bg="#CC004E", fg="white", command=get_weather, font=("Arial", 10, "bold"))
button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

window.mainloop()