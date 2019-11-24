import pandas as pd

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
with open("flashcards.csv", "r") as flashcards:
    flashcards = pd.read_csv(flashcards, header=None)

while session_count < session_limit:

    # Check if there are questions at the current level. This is iterative, because we want to exhaust the current level.
    if len(flashcards.loc[flashcards[2] == int(current_level)]) == 0:
        print("NO MORE QUESTIONS AT LEVEL", current_level)
        # Find another level, save it as integer
        x = 0
        while x in range(0, 5):
            if len(flashcards.loc[flashcards[2] == x]) > 0:
                current_level = x
                break
            else:
                x += 1
        if x == 5:
            print("NO MORE QUESTIONS.")
            break
        else:
            print("NEW LEVEL:", current_level)

    else:
        # Check if the level directly above hasn't maxed up. If it has, we have to go to that level before continuing. The new level is saved as an integer.
        if current_level < 4:
            next_level = current_level + 1
            if len(flashcards.loc[flashcards[2] == next_level]) >= max_definitions[int(next_level)]:
                current_level += 1
                print("NEXT LEVEL MAXED OUT.\nNEW LEVEL:", current_level)
        row = flashcards.loc[flashcards[2] == current_level].sample(n=1)
        # Display as many questions as possible: either before session end, or before end of questions at the level.
        print("Question:", row[0].values[0])
        answer = input("Answer:")
        if answer == row[1].values[0]:
            flashcards.loc[flashcards[0] == row[0].values[0], 2] += 1
            print("Correct.")
        else:
            print("Wrong.")
            print(row[1].values[0])
        session_count += 1

print("END OF SESSION.")

with open("flashcards.csv", "w") as nowe_flashcards, open("answered_questions.csv", "a+") as answered:
    flashcards.loc[flashcards[2] < 5].to_csv(nowe_flashcards, header=False, index=False)
    flashcards.loc[flashcards[2] == 5].to_csv(answered, header=False, index=False)

if last_level != str(current_level):
    with open("last_level.txt", "w") as new:
        new.write(str(current_level))

for level in range(0, 5):
    print("Remaining questions at level", level, ":", len(flashcards.loc[flashcards[2] == level]), "/", max_definitions[level])
