words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes = []

for i in range(len(words)):
    palindrome = True
    length = len(words[i]) // 2
    
    for j in range(length):
        if words[i][j] != words[i][len(words[i])-j-1]:
            palindrome = False
            break

    if palindrome:
        palindromes.append(words[i])

print(palindromes)