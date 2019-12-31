import pandas as pd

max_definitions = [20, 30, 45, 68, 101]
session_limit = 50

with open("flashcards.csv", "r") as flashcards:
    flashcards = pd.read_csv(flashcards, header=None)

equals = "=========================================================="
dash = "---------------------------------------------------"

print(equals * 2)

for level in range(0, 5):
    print("Remaining questions at level", level, ":", len(flashcards.loc[flashcards[2] == level]), "/", max_definitions[level])

with open("last_level.txt", "r") as saved_level:
    for line in saved_level:
        line = line.strip()
        last_level = line
print("CURRENT LEVEL:", last_level)
print(equals * 2)

session_count = 0
current_level = int(last_level)

def check_for_max(current_level):
    if len(flashcards.loc[flashcards[2] == current_level + 1]) >= max_definitions[current_level + 1]:
        current_level += 1
        print(equals * 2, "\nNEXT LEVEL MAXED OUT.\nNEW LEVEL:", current_level)
        print(equals * 2)
        return True
    else:
        return False

while session_count < session_limit:
    if len(flashcards.loc[flashcards[2] == int(current_level)]) == 0:
        print( equals * 2, "\nNO MORE QUESTIONS AT LEVEL", current_level)
        x = 0
        while x in range(0, 5):
            if len(flashcards.loc[flashcards[2] == x]) > 0:
                current_level = x
                break
            else:
                x += 1
        if x == 5:
            print("NO MORE QUESTIONS.")
            print(equals * 2)
            break
        else:
            print("NEW LEVEL:", current_level)
            print(equals * 2)

    else:
        if current_level < 4 and check_for_max(current_level):
            current_level += 1

        level = flashcards.loc[flashcards[2] == current_level]
        for row in range(0,len(level)):
            if session_count < session_limit and check_for_max(current_level) == False:
                print(dash, " QUESTION", session_count, ":", dash, "\n", level.iloc[row][0])
                answer = input("ANSWER:")
                if answer == level.iloc[row][1]:
                    flashcards.loc[flashcards[0] == level.iloc[row][0], 2] += 1
                    print("CORRECT.")
                else:
                    print("WRONG.")
                    print("                                                CORRECT ANSWER:\n", level.iloc[row][1])
                session_count += 1

print(equals, "\nEND OF SESSION.")
print(equals)

with open("flashcards.csv", "w") as nowe_flashcards, open("answered_questions.csv", "a+") as answered:
    flashcards.loc[flashcards[2] < 5].to_csv(nowe_flashcards, header=False, index=False, line_terminator="\n")
    flashcards.loc[flashcards[2] == 5].to_csv(answered, header=False, index=False, line_terminator="\n")

if last_level != str(current_level):
    with open("last_level.txt", "w") as new:
        new.write(str(current_level))

for level in range(0, 5):
    print("Remaining questions at level", level, ":", len(flashcards.loc[flashcards[2] == level]), "/", max_definitions[level])
