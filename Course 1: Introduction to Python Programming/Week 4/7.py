def computegrade(score):
    if (score > 1.0 or score<0.0):
        print("The score must be between 0.0 and 1.0")
        exit()
    else:
        if score>=0.9:
            grade = 'A'
        elif score>=0.8:
            grade = 'B'
        elif score>=0.7:
            grade = 'C'
        elif score>=0.6:
            grade ='D'
        else:
            grade = 'F'
    return grade
score = float(input("Enter the score"))
grade = computegrade(score)
print("Grade : ",grade)
