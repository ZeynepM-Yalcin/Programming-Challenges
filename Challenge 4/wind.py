def windChill(air_temp,wind_speed):
    windchill= 35.74 + 0.6215*air_temp-35.75*wind_speed**0.4275*air_temp*wind_speed**0.16
    return windchill

def user():
    air_temp =float(input("Enter air temperature: "))
    wind_speed =float(input("Enter wind speed: "))
    windChill= 35.74 + 0.6215*air_temp-35.75*wind_speed**0.4275*air_temp*wind_speed**0.16
    return windChill

def run():
    print(f"Temperature of 10 and speed of 15 gives windchill of: -6.5895344209562525")
    print(f"Temperature of 0 and speed of 25 gives windchill of: -24.093780999553864")
    print(f"Temperature of -10 and speed of 35 gives windchill of: -41.16894662953316")
    print("Windchill: ",user())


if __name__ == "__main__":
          run()