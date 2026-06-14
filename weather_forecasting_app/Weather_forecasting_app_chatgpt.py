import tkinter as tk
import requests

# ======= GUI SETUP =======
window = tk.Tk()
window.title("Professional Weather App")
window.geometry("420x250")

# ======= INPUT FIELD =======
tk.Label(window, text="Enter City Name:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(window, width=28)
city_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)


# ======= DISPLAY LABEL =======
info_label = tk.Label(window, text="", justify="left", font=("Arial", 10))
info_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# ======= WEATHER FUNCTION =======
def get_weather():
    city = city_entry.get().strip()
    
    if not city:
        info_label.config(text="⚠ Please enter a valid city name!")
        return

    api_key = "72fa312d37447f34cb2274221871f11c"  # Put your API key here
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(base_url, params={
            "q": city,
            "appid": api_key,
            "units": "metric"
        })
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]

            # Rain detection
            rain_amount = data.get("rain", {}).get("1h", 0)

            if rain_amount == 0:
                rain_status = "⛅ No measurable rain in the last hour"
            else:
                rain_status = f"🌧 Rain last hour: {rain_amount} mm"

            output = (
                f"🌍 City: {city.title()}\n"
                f"🌡 Temperature: {temp:.1f} °C\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind_speed} m/s\n"
                f"🔽 Pressure: {pressure} hPa\n"
                f"{rain_status}"
            )

        else:
            output = "❌ City not found or invalid input."

    except:
        output = "⚠ Network error. Check your connection!"

    info_label.config(text=output)
    city_entry.delete(0, tk.END)  # Clear input field after request


# ======= BUTTON =======
search_btn = tk.Button(window, text="Search", font=("Arial", 10, "bold"),
                       bg="#007ACC", fg="white", command=get_weather)
search_btn.grid(row=0, column=4, padx=10)

window.mainloop()
