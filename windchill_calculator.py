def calc_wind_chill(temp, wind_speed):
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)
    return wind_chill

def c_to_f(c_temp):
    return c_temp * (9/5) + 32

temp = float(input("What is the temperature? "))
temp_unit = input("Fahrenheit or Celsius (F/C)? ").upper()

if temp_unit == 'C':
    temp = c_to_f(temp)

for wind_speed in range(5, 65, 5):
    wind_chill = calc_wind_chill(temp, wind_speed)
    print(f"At temperature {temp:.2f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
