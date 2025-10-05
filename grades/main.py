grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good = []
pas = [] #pass is a keyword
fail = []

for i in range(8):
    if grades[i] >= 90:
        excellent.append(grades[i])
    elif grades[i] >= 70 and grades[i] <= 89:
        good.append(grades[i])
    elif grades[i] >= 50 and grades[i] <= 69:
        pas.append(grades[i])
    elif grades[i] < 50:
        fail.append(grades[i])

print("Excellent: ", excellent)
print("Good: ", good)
print("Pass: ", pas)
print("Fail: ", fail)