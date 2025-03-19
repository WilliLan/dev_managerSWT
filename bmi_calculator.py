def calculate_bmi(height_feet, height_inches, weight_pounds):
    total_height_inches = (height_feet * 12) + height_inches
    height_meters = total_height_inches * 0.025
    weight_kg = weight_pounds * 0.45
    bmi = weight_kg / (height_meters ** 2)
    return round(bmi, 1)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"