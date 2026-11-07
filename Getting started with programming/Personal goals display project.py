# ================================
# PERSONAL GOALS DISPLAY
# ================================
import keyword 
# ---------- PART 1: import the keyword module ----------

#  One line. You need this for Part 7.


# ---------- PART 2: ask the three questions ----------
Person_name = input(" Enter your name")
Goal_name = input("Enter your goal")
Time_name = input("Enter when you want to reach it by")
# Use input() three times and store each answer in its own variable:
#   person_name    <- "Enter your name: "
#   goal_name     <- "Enter one skill you want to get better at: "
#      <- "Enter the month you want to reach it by: "


# ---------- PART 3: store the practice time ----------
daily_minutes =  30
# Store the number 30 in a variable called daily_minutes.
# Type it as 30, NOT as "30".


# ---------- PART 4: the heading ----------
print("\n MY PERSONAL GOAL PLAN\n")
# Print MY PERSONAL GOAL PLAN with one blank line above it and one below.
# Do it in a single print() using \n at the start and the end.


# ---------- PART 5: the four plan lines ----------
print("person_name:", Person_name)
print("goal_name:", Goal_name)
print("time_name:", Time_name)
print("Daily practice:", daily_minutes, "minutes")
# Four print() statements, each with a label and a variable separated by a comma:
#   Name: ...
#   Goal: ...
#   Target month: ...
#   Daily practice: ... minutes      <- this one has THREE values


# ---------- PART 6: two lines that join up ----------
print("Status:",end=(""))
print("Not started")
print("Reminder:",end=(" - "))
print("Pratice every day for 30 minutes!")
# Print "Status:" ending in a space, then "Not started" on the next print.
# Print "Reminder:" ending in " - ", then "Practise every day!" on the next print.
# Both pairs must appear on ONE line each in the output.


# ---------- PART 7: the sentence and the keywords -----------
print(Person_name, "plans to work on", Goal_name, "for", daily_minutes, "minutes every day until", Time_name)
print("\n Python has reserves for itself:\n")
print(keyword.kwlist)
# Print "In one sentence:" then one print() that joins the name, the goal,
# the minutes and the month into a readable sentence.
# Then print Python's reserved word list using