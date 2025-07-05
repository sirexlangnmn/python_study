input_score = 1
scores = [75, 89, 92, 67, 45, 58, 76, 85, 92, 38, 91]
scores.append(input_score)


highest_score = scores[0]
lowest_score = scores[0]
scores_length = len(scores)
passed = 0
failed = 0
bracket_A = 0
bracket_B = 0
bracket_C = 0
bracket_D = 0
bracket_E = 0
frequency = {}


if scores_length > 0:
    for score in scores:
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score


        if score >= 61:
            passed += 1
        if score <= 60:
            failed += 1


        if score >= 90 and score <= 100:
            bracket_A += 1
        if score >= 80 and score <= 89:
            bracket_B += 1
        if score >= 70 and score <= 79:
            bracket_C += 1
        if score >= 60 and score <= 69:
            bracket_D += 1
        if score >= 0 and score <= 59:
            bracket_E += 1


        if score in frequency:
            frequency[score] += 1
        else:
            frequency[score] = 1


    max_freq = 0
    for count in frequency.values():
        if count > max_freq:
            max_freq = count


    most_frequent_scores = []
    for score in frequency:
        if frequency[score] == max_freq:
            most_frequent_scores.append(score)


    average_score = round(sum(scores) / len(scores))
    ascending_score = sorted(scores)
    unique_score = sorted(set(scores))

else:
    print("No score")



print("Highest score : ", highest_score)
print("Lowest score : ", lowest_score)
print("Average score : ", average_score)
print("Failed : ", failed)
print("Passed : ", passed)
print("Bracket A : ", bracket_A)
print("Bracket B : ", bracket_B)
print("Bracket C : ", bracket_C)
print("Bracket D : ", bracket_D)
print("Bracket E : ", bracket_E)
print("Ascending order scores : ", ascending_score)
print("Unique scores : ", unique_score)
print("Frequencies:", frequency)
print("Most frequent score(s):", most_frequent_scores)
print("They appear", max_freq, "time(s)")