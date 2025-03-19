from bmi_calculator import calculate_bmi, categorize_bmi

def main():
    print("BMI Calculator")
    height_feet = int(input("Enter height (feet): "))
    height_inches = int(input("Enter height (inches): "))
    weight_pounds = float(input("Enter weight (pounds): "))

    bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
    category = categorize_bmi(bmi)

    print(f"Your BMI is: {bmi}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()