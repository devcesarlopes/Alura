age_years = float(input('enter age in years:\n'))
weight_lbs = float(input('enter weight in lbs:\n'))
heart_rate = float(input('enter heart rate in beats per minute:\n'))
time_min = float(input('enter time in minutes:\n'))
calories = ((age_years * 0.2757) + (weight_lbs * 0.03295) + (heart_rate * 1.0781) -
75.4991) * time_min / 8.368

print('Calories: {:.2f} calories'.format(calories))