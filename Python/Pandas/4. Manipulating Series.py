import pandas as pd

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]
planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

dist_planets = pd.Series(data = distance_from_sun, index = planets)

# We want time in minutes
# Speed of light = 18 x 10^6 KM/min
time_light = dist_planets / 18

# We want planets to which light takes less than 40 mins to reach
close_planets = time_light[time_light < 40]

print(close_planets)