 Ovuflow - Ovulation and Fertility Tracker

Ovuflow  is a sophisticated Python-based desktop application designed to empower users in managing and tracking their menstrual and ovulation cycles. By providing insightful predictions of ovulation days, fertile windows, and pregnancy-related dates, Ovuflow also offers the ability to visualize hormone fluctuations across the cycle. It further customizes these insights based on health conditions (like PCOS and thyroid issues) and exercise activity levels, ensuring that every user's cycle is accounted for with personalized precision.

Features

- Ovulation Prediction & Fertile Windows**: Predicts ovulation day, multiple fertile windows, and calculates key milestones like the next period, pregnancy test date, and due date.
- Hormone Level Graphs: Visualizes estrogen, progesterone, and LH hormone levels throughout the cycle, adjusting for health conditions and exercise levels.
- Personalized Health Profiles : Offers functionality to adjust hormone levels based on selected health conditions (e.g., PCOS, thyroid issues) and exercise activity (e.g., Very Active, Sedentary).
- User-Friendly GUI: Easy-to-navigate interface for selecting cycle start dates, entering cycle lengths, and displaying results.
- Calendar Integration: Includes a calendar to select the start date of the menstrual cycle for better usability.



 Technologies Used

- Python 3.x: The primary programming language for developing the application.
- Tkinter : The core GUI toolkit used for creating the interactive interface.
- NumPy : Used for numerical calculations required for hormone level adjustments and simulations.
- Matplotlib: Employed for plotting hormone levels during the cycle, offering insightful visual feedback.
- tkcalendar: Integrated calendar widget for selecting dates in the application.

 Usage Instructions

 Start Date and Cycle Length

- Enter the start date of your last period in the `YYYY-MM-DD` format.
- Provide your cycle length (the number of days between periods).

Health Conditions and Exercise Levels

- Health Condition: Select from `Normal`, `PCOS`, or `Thyroid Issues` to adjust hormone levels accordingly.
- Exercise Level: Choose between `Very Active`, `Normal`, or `Sedentary` to factor in the impact of exercise on your hormone levels.

 Features to Explore

- Show Fertile Window: Predicts the days when you are most fertile.
- Show Pregnancy Test Date : Suggests when you should take a pregnancy test after a missed period.
- Show Estimated Due Date : Estimates the due date based on ovulation.
- Hormone Levels Graph : Visualizes your hormone levels (estrogen, progesterone, LH) throughout your cycle.

 Date Selection via Calendar

Click on the **Select Start Date from Calendar** button to easily choose the start date from a calendar widget.

 Code Explanation

 Key Functions

1. `calculate_dates(start_date, cycle_length)`
   - Calculates the ovulation day, fertile windows, next period, pregnancy test date, and due date based on the provided start date and cycle length.
   - Uses a simple mathematical approach to determine the ovulation day as 14 days before the next period.

2. `plot_hormone_levels(start_date, cycle_length, fertile_windows, health_condition, exercise_level)`
   - Simulates hormone fluctuations during the cycle using sine waves and adjusts for health conditions like PCOS and thyroid issues, as well as activity levels.
   - Generates a plot of estrogen, progesterone, and LH hormone levels throughout the cycle.
   - Highlights the ovulation day and fertile windows on the graph.

3. `display_results()`
   - Retrieves and formats all calculated results (ovulation, fertile windows, next period, etc.), saving them to a text file and preparing them for display.

4. `show_fertile_window()`, `show_pregnancy_test_date()`, `show_due_date()`
   - Displays results to the user based on the selected parameters using `messagebox`.

5. `show_graph()`
   - Displays a graph of hormone levels across the cycle, customized based on user inputs.

6. `show_calendar()`
   - Opens a calendar to allow users to select the start date of their cycle easily.

 Contributing

We welcome contributions to the **Ovuflow** project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request to the main repository.

Please ensure your code is well-documented and follows Python's PEP8 guidelines.

 Acknowledgements

- Tkinter : For building the interactive GUI.
- NumPy: For handling numerical operations required to simulate hormone levels.
- Matplotlib: For visualizing the hormone levels graphically.
- tkcalendar: For providing a calendar widget to easily select the start date.
- Health and Exercise Level Adjustments: This feature helps tailor predictions based on individual needs, enhancing the application's utility.

 Future Enhancements

- BBT Integration : Future versions may include a Basal Body Temperature (BBT) tracking feature to refine ovulation predictions.
- Mobile Application : An extension of Ovuflow for mobile devices (e.g., Android or iOS) for better accessibility.
- User Authentication : Implement user profiles for storing historical data securely.

