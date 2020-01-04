import pandas as pd

max_definitions = [20, 30, 45, 68, 101]
session_limit = 50

with open("flashcards.csv", "r") as flashcards:
    flashcards = pd.read_csv(flashcards, header=None)

equals = "=========================================================="
dash = "---------------------------------------------------"

print(equals * 2)

def questions(checked_level):
    questions = flashcards.loc[flashcards[2] == checked_level]
    return questions

for level in range(0, 5):
    print("Remaining questions at level", level, ":", len(questions(level)), "/", max_definitions[level])

with open("last_level.txt", "r") as saved_level:
    for line in saved_level:
        line = line.strip()
        last_level = line
print("CURRENT LEVEL:", last_level)
print(equals * 2)

current_level = int(last_level)

session_count = 0

def check_for_max(level):
    if level < 4 and len(questions(level + 1)) >= max_definitions[level + 1]:
        level += 1
        print(equals * 2, "\nNEXT LEVEL MAXED OUT.\nNEW LEVEL:", level)
        print(equals * 2)
        return True
    else:
        return False

while session_count < session_limit:
    if len(questions(level)) == 0:
        print( equals * 2, "\nNO MORE QUESTIONS AT LEVEL", level)
        for level in range(0, 5):
            if len(questions(level)) > 0:
                break
        if level == 5:
            print("NO MORE QUESTIONS.")
            print(equals * 2)
            break
        else:
            print("NEW LEVEL:", level)
            print(equals * 2)

    else:
        if check_for_max(level):
            level += 1

        for row in range(0,len(questions(level))):
            if session_count < session_limit:
                if check_for_max(level) == False:
                    questions_df = flashcards.loc[flashcards[2] == level]
                    print(dash, " QUESTION", session_count, ":", dash, "\n", questions_df.iloc[row][0])
                    answer = input("ANSWER:")
                    if answer == questions_df.iloc[row][1]:
                        flashcards.loc[flashcards[0] == questions_df.iloc[row][0], 2] += 1
                        print("CORRECT.")
                    else:
                        print("WRONG.")
                        print("                                                   CORRECT ANSWER:\n", questions_df.iloc[row][1])
                    session_count += 1
                else:
                    level += 1
                    break
            else:
                break

print(equals, "\nEND OF SESSION.")
print(equals)

with open("flashcards.csv", "w") as new_flashcards, open("answered_questions.csv", "a+") as answered:
    flashcards.loc[flashcards[2] < 5].to_csv(new_flashcards, header=False, index=False, line_terminator="\n")
    flashcards.loc[flashcards[2] == 5].to_csv(answered, header=False, index=False, line_terminator="\n")

if last_level != str(level):
    with open("last_level.txt", "w") as new:
        new.write(str(level))

for level in range(0, 5):
    print("Remaining questions at level", level, ":", len(questions(level)), "/", max_definitions[level])
