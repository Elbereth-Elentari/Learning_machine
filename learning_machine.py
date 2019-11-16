import csv
import random

max_definitions = [20, 30, 45, 68, 101]
session_limit = 50

# Saves a string for the last level
with open("last_level.txt", "r") as saved_level:
    for line in saved_level:
        line = line.strip()
        last_level = line
print("Last level:", last_level)

session_count = 0
current_level = int(last_level) # Current_level is an integer
with open("fiszki.csv", "r") as fiszki:
    fiszki = list(csv.reader(fiszki))
    random.shuffle(fiszki)
    while session_count < session_limit:

        # Check if there are questions at the current level. This is iterative, because we want to exhaust the current level.
        if sum(line[2] == str(current_level) for line in fiszki) == 0:
            print("NO MORE QUESTIONS AT LEVEL", current_level)
            # Find another level, save it as integer
            level = current_level - 1
            current_level = 0
            while level > 0:
                if sum(line[2] == str(level) for line in fiszki) >= max_definitions[level]:
                    current_level = level
                    break
                else:
                    level -= 1
            if current_level == 0:
                if sum(line[2] == "0" for line in fiszki) == 0:
                    x = 1
                    while x in range(1, 5):
                        if sum(line[2] == str(x) for line in fiszki) > 0:
                            next_level = x
                            break
                        else:
                            x += 1
                    if current_level == 0:
                        current_level = 5
            if current_level < 5:
                print("NEW LEVEL:", current_level)
            else:
                print("NO MORE QUESTIONS.")
                break

        else:
            for line in fiszki:
                if session_count < session_limit:
                    # Check if the level directly above hasn't maxed up.
                    # If it has, we have to go to that level before continuing.
                    # The new level is saved as an integer.
                    if current_level < 4:
                        next_level = current_level + 1
                        if sum(line[2] == str(next_level) for line in fiszki) >= max_definitions[int(next_level)]:
                            current_level += 1
                            print("NEW LEVEL:", current_level)
                    if line[2] == str(current_level):
                        # Display as many questions as possible: either before session end,
                        # or before end of questions at the level.
                        print("Question:", line[0])
                        answer = input("Answer:")
                        if answer == line[1]:
                            line[2] = str(int(line[2]) + 1)
                            print("Correct.")
                        else:
                            print("Wrong.")
                            print(line[1])
                        session_count += 1

with open("fiszki.csv", "w", newline = "") as nowe_fiszki, open("answered_questions.csv", "a+", newline = "") as answered:
    nowe_fiszki = csv.writer(nowe_fiszki)
    answered = csv.writer(answered)
    for line in fiszki:
        if int(line[2]) < 5:
            nowe_fiszki.writerow(line)
        else:
            answered.writerow(line)

if last_level != str(current_level):
    with open("last_level.txt", "w") as new:
        new.write(str(current_level))

for level in range(0, 5):
    remaining = sum(line[2] == str(level) for line in fiszki)
    print("Remaining questions at level", level, ":", remaining)
