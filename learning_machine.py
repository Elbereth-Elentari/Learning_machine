import pandas as pd

max_definitions = [20, 30, 45, 68, 101]
session_limit = 50

with open("flashcards.csv", "r") as flashcards:
    flashcards = pd.read_csv(flashcards, header=None)

equals = "=========================================================="
dash = "----------------------------------------------------------"

print(equals * 2)

def question_count(checked_level):
    return len(flashcards.loc[flashcards[2] == checked_level])

def statistics():
    for level in range(0, 5):
        print("Remaining questions at level", level, ":", question_count(level), "/", max_definitions[level])
    return True

statistics()

with open("last_level.txt", "r") as saved_level:
    for line in saved_level:
        line = line.strip()
        last_level = line
print("CURRENT LEVEL:", last_level)
print(equals * 2)

level = int(last_level)

session_count = 0

def check_for_max(level):
    if level < 4 and question_count(level + 1) >= max_definitions[level + 1]:
        level += 1
        print(equals * 2, "\nNEXT LEVEL MAXED OUT.\nNEW LEVEL:", level)
        print(equals * 2)
        return True
    else:
        return False

def handle_finished_level(checked_level):
    print( equals * 2, "\nNO MORE QUESTIONS AT LEVEL", checked_level)
    for level in range(0, 5):
        if question_count(level) > 0:
            break
    if level == 5:
        print("NO MORE QUESTIONS.")
        print(equals * 2)
        return level
    else:
        print("NEW LEVEL:", level)
        print(equals * 2)
    return level

def motivation(level, session_count):
    if level < 4:
        to_max = max_definitions[level + 1] - question_count(level + 1)
    else:
        to_max = max_definitions[4] + 1
    to_end = session_limit - session_count
    level_end = question_count(level)
    motives = {to_max : "Remaining questions to max out next level:", level_end : "Remaining questions to finish this level:", to_end : "Remaining questions to end session:"}
    to_print = min([number for number in motives])
    print(motives[to_print], to_print)
    return True

def handle_1_question(df, index, row, session_count):
    print(dash * 2)
    print(row[0])
    answer = input()
    if answer == row[1]:
        df.iat[index, 2] += 1
    else:
        print(row[1])
    print(equals * 2)
    session_count += 1
    return df, session_count

def handle_questions_at_1_level(df, level, session_count):
    for index, row in df.loc[df[2] == level].iterrows():
        if session_count < session_limit:
            if check_for_max(level) == False:
                motivation(level, session_count)
                df, session_count = handle_1_question(df, index, row, session_count)
            else:
                level += 1
                break
        else:
            return df, level, session_count
    return df, level, session_count

while session_count < session_limit:
    if question_count(level) == 0:
        level = handle_finished_level(level)
    else:
        if check_for_max(level):
            level += 1
        flashcards, level, session_count = handle_questions_at_1_level(flashcards, level, session_count)

print("END OF SESSION.")
print(equals)

with open("flashcards.csv", "w") as new_flashcards, open("answered_questions.csv", "a+") as answered:
    flashcards.loc[flashcards[2] < 5].to_csv(new_flashcards, header=False, index=False, line_terminator="\n")
    flashcards.loc[flashcards[2] == 5].to_csv(answered, header=False, index=False, line_terminator="\n")

if last_level != str(level):
    with open("last_level.txt", "w") as new:
        new.write(str(level))

statistics()
