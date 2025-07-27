def life_in_weeks(age):
    weeks_in_a_year = 52
    years_left = 90 - age
    weeks_left = years_left * weeks_in_a_year
    print(f"You have {weeks_left} weeks left.")
    
# Call your function with a hardcoded value
life_in_weeks(56)  # Example: should output "You have 1768 weeks left."
