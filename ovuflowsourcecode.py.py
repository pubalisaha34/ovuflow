import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from tkcalendar import Calendar

# Function to calculate the ovulation day, fertile window, and next period date
def calculate_dates(start_date, cycle_length):
    # Calculate the predicted ovulation date (14 days before the next cycle)
    ovulation_day = start_date + timedelta(days=cycle_length - 14)
    
    # Calculate the fertile windows (5 days before ovulation and 1 day after)
    fertile_windows = []
    for i in range(3):  # Generate 3 consecutive fertile windows
        fertile_start = ovulation_day - timedelta(days=5) + timedelta(days=i*28)  # Shift by 28 days for next cycle
        fertile_end = fertile_start + timedelta(days=6)
        fertile_windows.append((fertile_start, fertile_end))
    
    # Calculate the next period date (start date of next cycle)
    next_period = start_date + timedelta(days=cycle_length)
    
    # Calculate the pregnancy test date (1 week after missed period)
    pregnancy_test_date = next_period + timedelta(days=7)
    
    # Calculate the due date (estimated 9 months from ovulation)
    due_date = ovulation_day + timedelta(weeks=40)
    
    return ovulation_day, fertile_windows, next_period, pregnancy_test_date, due_date

# Function to plot hormone levels during the cycle
def plot_hormone_levels(start_date, cycle_length, fertile_windows, health_condition, exercise_level):
    # Simulate hormone levels with adjustments based on health condition and exercise level
    days = np.arange(1, cycle_length + 1)
    
    if health_condition == "Normal":
        # Normal fluctuation with sine and cosine
        estrogen = np.cos((days - 14) / cycle_length * 2 * np.pi) * 0.7 + 0.5
        progesterone = np.sin((days - 14) / cycle_length * 2 * np.pi) * 0.7 + 0.5
        lh = np.cos((days - 12) / cycle_length * 2 * np.pi) * 0.5 + 0.5
    elif health_condition == "PCOS":
        # Adjusted fluctuation for PCOS
        estrogen = np.sin((days - 14) / cycle_length * 2 * np.pi) * 0.6 + 0.4
        progesterone = np.cos((days - 16) / cycle_length * 2 * np.pi) * 0.6 + 0.4
        lh = np.sin((days - 18) / cycle_length * 2 * np.pi) * 0.5 + 0.6
    elif health_condition == "Thyroid Issues":
        # Adjusted fluctuation for thyroid issues
        estrogen = np.cos((days - 14) / cycle_length * 2 * np.pi) * 0.8 + 0.6
        progesterone = np.sin((days - 15) / cycle_length * 2 * np.pi) * 0.8 + 0.5
        lh = np.cos((days - 12) / cycle_length * 2 * np.pi) * 0.6 + 0.4

    # Adjust hormone levels based on exercise level
    if exercise_level == "Very Active":
        estrogen *= 0.8
        progesterone *= 0.9
        lh *= 0.7
    elif exercise_level == "Sedentary":
        estrogen *= 1.2
        progesterone *= 1.1
        lh *= 1.1
    
    # Calculate ovulation day as the number of days since start_date
    ovulation_day = (start_date + timedelta(days=cycle_length - 14) - start_date).days
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, estrogen, label=f"Estrogen ({health_condition}, {exercise_level})", color='green')
    plt.plot(days, progesterone, label=f"Progesterone ({health_condition}, {exercise_level})", color='red')
    plt.plot(days, lh, label=f"LH ({health_condition}, {exercise_level})", color='blue')
    
    # Highlight ovulation day
    plt.axvline(x=ovulation_day + 1, color='orange', linestyle='--', label="Ovulation")
    
    # Highlight multiple fertile windows
    for fertile_start, fertile_end in fertile_windows:
        fertile_start_day = (fertile_start - start_date).days + 1
        fertile_end_day = (fertile_end - start_date).days + 1
        plt.axvspan(fertile_start_day, fertile_end_day, color='yellow', alpha=0.3, label="Fertile Window")
    
    plt.title(f"Hormone Levels and Ovulation Cycle\nCondition: {health_condition}, Exercise Level: {exercise_level}")
    plt.xlabel("Day of Cycle")
    plt.ylabel("Hormone Level")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to handle user inputs and display results
def display_results():
    start_date_str = start_date_entry.get()
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
        return
    
    try:
        cycle_length = int(cycle_length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Cycle Length", "Please enter a valid number for cycle length.")
        return
    
    # Get the predicted dates
    ovulation_day, fertile_windows, next_period, pregnancy_test_date, due_date = calculate_dates(start_date, cycle_length)
    
    # Store data in a dictionary
    user_data = {
        "start_date": start_date_str,
        "cycle_length": cycle_length,
        "ovulation_day": ovulation_day.strftime("%Y-%m-%d"),
        "fertile_windows": [(start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")) for start, end in fertile_windows],
        "next_period": next_period.strftime("%Y-%m-%d"),
        "pregnancy_test_date": pregnancy_test_date.strftime("%Y-%m-%d"),
        "due_date": due_date.strftime("%Y-%m-%d"),
    }
    
    # Save user data to a text file
    with open("user_data.txt", "w") as file:
        for key, value in user_data.items():
            file.write(f"{key}: {value}\n")
    
    return user_data

# Function to show Fertile Window Result
def show_fertile_window():
    user_data = display_results()
    fertile_message = f"You will likely ovulate on {user_data['ovulation_day']}.\n"
    fertile_message += "Your upcoming fertile windows are:\n"
    for i, (fertile_start, fertile_end) in enumerate(user_data["fertile_windows"], 1):
        fertile_message += f"Fertile Window {i}: {fertile_start} to {fertile_end}\n"
    messagebox.showinfo("Fertile Window", fertile_message)

# Function to show Pregnancy Test Date
def show_pregnancy_test_date():
    user_data = display_results()
    messagebox.showinfo("Pregnancy Test Date", f"You can take a pregnancy test on:\n{user_data['pregnancy_test_date']}")

# Function to show Due Date
def show_due_date():
    user_data = display_results()
    messagebox.showinfo("Estimated Due Date", f"Your estimated due date is:\n{user_data['due_date']}")

# Function to plot hormone levels graph
def show_graph():
    start_date_str = start_date_entry.get()
    cycle_length = int(cycle_length_entry.get())
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    ovulation_day, fertile_windows, _, _, _ = calculate_dates(start_date, cycle_length)
    
    # Get health condition and exercise level input
    health_condition = health_conditions.get()
    exercise_level = exercise_level_var.get()
    
    plot_hormone_levels(start_date, cycle_length, fertile_windows, health_condition, exercise_level)

# Function to display the calendar for date selection
def show_calendar():
    calendar_window = tk.Toplevel(root)
    calendar_window.title("Select Start Date")
    calendar_window.geometry("300x300")
    
    def get_selected_date():
        selected_date = calendar.get_date()
        start_date_entry.delete(0, tk.END)
        start_date_entry.insert(0, selected_date)
        calendar_window.destroy()
    
    calendar = Calendar(calendar_window, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.pack(pady=20)
    select_button = tk.Button(calendar_window, text="Select Date", command=get_selected_date)
    select_button.pack()

# Create the GUI window
root = tk.Tk()
root.title("Ovulation Calculator")
root.geometry("500x700")
root.configure(bg="#f8c0c0")  # Soft pink background color

# Instructions label
instructions_label = tk.Label(root, text="Enter the start date of your last period and your cycle length.", font=("Helvetica", 12), bg="#f8c0c0")
instructions_label.pack(pady=10)

# Start date entry
start_date_label = tk.Label(root, text="Start Date (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f8c0c0")
start_date_label.pack(pady=5)
start_date_entry = tk.Entry(root, font=("Helvetica", 12))
start_date_entry.pack(pady=5)

# Cycle length entry
cycle_length_label = tk.Label(root, text="Cycle Length (days):", font=("Helvetica", 12), bg="#f8c0c0")
cycle_length_label.pack(pady=5)
cycle_length_entry = tk.Entry(root, font=("Helvetica", 12))
cycle_length_entry.pack(pady=5)

# Health conditions dropdown
health_conditions_label = tk.Label(root, text="Health Condition:", font=("Helvetica", 12), bg="#f8c0c0")
health_conditions_label.pack(pady=5)
health_conditions = tk.StringVar(root)
health_conditions.set("Normal")
health_condition_menu = tk.OptionMenu(root, health_conditions, "Normal", "PCOS", "Thyroid Issues")
health_condition_menu.config(font=("Helvetica", 12))
health_condition_menu.pack(pady=5)

# Exercise level dropdown
exercise_level_label = tk.Label(root, text="Exercise Level:", font=("Helvetica", 12), bg="#f8c0c0")
exercise_level_label.pack(pady=5)
exercise_level_var = tk.StringVar(root)
exercise_level_var.set("Normal")
exercise_level_menu = tk.OptionMenu(root, exercise_level_var, "Very Active", "Normal", "Sedentary")
exercise_level_menu.config(font=("Helvetica", 12))
exercise_level_menu.pack(pady=5)

# Buttons to show results and graph
fertile_window_button = tk.Button(root, text="Show Fertile Window", command=show_fertile_window, font=("Helvetica", 12), bg="#ffb6b9", relief="flat")
fertile_window_button.pack(pady=10)

pregnancy_test_button = tk.Button(root, text="Show Pregnancy Test Date", command=show_pregnancy_test_date, font=("Helvetica", 12), bg="#ffb6b9", relief="flat")
pregnancy_test_button.pack(pady=10)

due_date_button = tk.Button(root, text="Show Estimated Due Date", command=show_due_date, font=("Helvetica", 12), bg="#ffb6b9", relief="flat")
due_date_button.pack(pady=10)

graph_button = tk.Button(root, text="Show Hormone Levels Graph", command=show_graph, font=("Helvetica", 12), bg="#ffb6b9", relief="flat")
graph_button.pack(pady=10)

# Calendar button
calendar_button = tk.Button(root, text="Select Start Date from Calendar", command=show_calendar, font=("Helvetica", 12), bg="#ffb6b9", relief="flat")
calendar_button.pack(pady=10)

# Run the GUI
root.mainloop()

