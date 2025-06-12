import tkinter as tk
from tkinter import ttk, messagebox

def calculate_macros():
    try:
        # Get and convert inputs
        weight_lbs = float(weight_entry.get())
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()
        activity = activity_var.get()
        goal = goal_var.get()

        # Convert to metric
        weight_kg = weight_lbs * 0.453592
        height_cm = (feet * 12 + inches) * 2.54

        # BMR calculation (Mifflin-St Jeor Equation)
        if gender == "Male":
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

        # Activity multiplier
        activity_levels = {
            "Sedentary": 1.2,
            "Lightly active": 1.375,
            "Moderately active": 1.55,
            "Very active": 1.725,
            "Super active": 1.9
        }
        tdee = bmr * activity_levels[activity]

        # Adjust calories based on goal
        if goal == "Lose weight":
            calories = tdee - 500
        elif goal == "Gain weight":
            calories = tdee + 500
        else:
            calories = tdee

        # Macronutrient breakdown (30% protein, 40% carbs, 30% fat)
        protein_cal = calories * 0.30
        carbs_cal = calories * 0.40
        fat_cal = calories * 0.30

        protein_grams = protein_cal / 4
        carbs_grams = carbs_cal / 4
        fat_grams = fat_cal / 9

        result = (
            f"Calories per day: {int(calories)} kcal\n"
            f"Protein: {int(protein_grams)}g\n"
            f"Carbs: {int(carbs_grams)}g\n"
            f"Fats: {int(fat_grams)}g"
        )
        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
window = tk.Tk()
window.title("Macro Calculator (Imperial Units)")
window.geometry("400x550")

tk.Label(window, text="Macro Calculator for Athletes", font=("Arial", 16)).pack(pady=10)

# Input fields
tk.Label(window, text="Weight (lbs):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height:").pack()
height_frame = tk.Frame(window)
height_frame.pack()
tk.Label(height_frame, text="Feet").grid(row=0, column=0)
feet_entry = tk.Entry(height_frame, width=5)
feet_entry.grid(row=0, column=1)
tk.Label(height_frame, text="Inches").grid(row=0, column=2)
inches_entry = tk.Entry(height_frame, width=5)
inches_entry.grid(row=0, column=3)

tk.Label(window, text="Age:").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Label(window, text="Gender:").pack()
gender_var = tk.StringVar(value="Male")
ttk.Combobox(window, textvariable=gender_var, values=["Male", "Female"]).pack()

tk.Label(window, text="Activity Level:").pack()
activity_var = tk.StringVar(value="Moderately active")
ttk.Combobox(window, textvariable=activity_var, values=[
    "Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"
]).pack()

tk.Label(window, text="Goal:").pack()
goal_var = tk.StringVar(value="Maintain weight")
ttk.Combobox(window, textvariable=goal_var, values=[
    "Lose weight", "Maintain weight", "Gain weight"
]).pack()

tk.Button(window, text="Calculate Macros", command=calculate_macros).pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label.pack()

window.mainloop()
