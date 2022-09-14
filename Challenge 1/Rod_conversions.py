
def rod_to_meters(rods):
    meters = rods * 5.0292
    return meters

def meters_to_feet(meters):
    feet = meters / 0.3048
    return feet
    
def meters_to_miles(meters):
    miles = meters / 1609.34
    return miles

def rods_to_furlongs(rods):
    furlongs = rods / 40
    return furlongs

def miles_in_minutes(miles):
    minutes = miles / 60
    return minutes
    
def calculate():
    rods = float(input("Please enter value: "))
    meters = rod_to_meters(rods)
    feet = meters_to_feet(meters)
    miles = meters_to_miles(meters)
    furlongs = rods_to_furlongs(rods)
    minutes = miles_in_minutes(miles)

    return rods,meters, feet, miles, furlongs, minutes

def print_values():
    print(f" meters: {meters}")
    print(f" feet: {feet}")
    print(f" miles: {miles}")
    print(f" furlongs: {furlongs}")
    print(f" Minutes to walk {rods}: {minutes}")


rods,meters, feet, miles, furlongs, minutes = calculate()


if __name__ == '__main__':
    print_values()


