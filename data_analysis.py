import csv

def read_data(file_path):
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def lowest_life_expectancy(data):
    min_expectancy = float("inf")
    min_country = ""
    min_year = ""
    for row in data:
        expectancy = float(row["Life expectancy (years)"])
        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_country = row["Entity"]
            min_year = row["Year"]
    return min_country, min_year

def highest_life_expectancy(data):
    max_expectancy = float("-inf")
    max_country = ""
    max_year = ""
    for row in data:
        expectancy = float(row["Life expectancy (years)"])
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_country = row["Entity"]
            max_year = row["Year"]
    return max_country, max_year

def average_life_expectancy(data, year):
    total_expectancy = 0
    count = 0
    for row in data:
        if row["Year"] == year:
            expectancy = float(row["Life expectancy (years)"])
            total_expectancy += expectancy
            count += 1
    if count == 0:
        return None
    average = total_expectancy / count
    return average

def country_with_min_expectancy(data, year):
    min_expectancy = float("inf")
    min_country = ""
    for row in data:
        if row["Year"] == year:
            expectancy = float(row["Life expectancy (years)"])
            if expectancy < min_expectancy:
                min_expectancy = expectancy
                min_country = row["Entity"]
    return min_country, min_expectancy

def country_with_max_expectancy(data, year):
    max_expectancy = float("-inf")
    max_country = ""
    for row in data:
        if row["Year"] == year:
            expectancy = float(row["Life expectancy (years)"])
            if expectancy > max_expectancy:
                max_expectancy = expectancy
                max_country = row["Entity"]
    return max_country, max_expectancy

data = read_data("life-expectancy.csv")

while True:
    year_of_interest = input("\nEnter the year of interest: ")
    if year_of_interest.isdigit():
        break
    else:
        print("Year not available, please enter a valid year.")

min_country, min_year = lowest_life_expectancy(data)
print(f"\nThe year and country with the lowest life expectancy: {min_year}, {min_country}")

max_country, max_year = highest_life_expectancy(data)
print(f"The year and country with the highest life expectancy: {max_year}, {max_country}")

average_expectancy = average_life_expectancy(data, year_of_interest)
if average_expectancy is None:
    print("\nThere is no data for that year. ")
else:
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across the world was: {average_expectancy:.2f}")

    min_country, min_expectancy = country_with_min_expectancy(data, year_of_interest)
    print(f"The country with the minimum life expectancy was: {min_country} with {min_expectancy:.3f}")

    max_country, max_expectancy = country_with_max_expectancy(data, year_of_interest)
    print(f"The country with the maximum life expectancy was: {max_country} with {max_expectancy:.3f}")

