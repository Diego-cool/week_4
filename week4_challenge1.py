#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
# "Controlling complexity is the essence of programming"
# Hint: "Controlling" is 11 characters long.
print("Sub-string1")
result = ("Controlling complexity is the essence of programming")
print(result.find('Controlling'))
print(result[0:11])

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"
print("Sub-string2")
text=("Never trust a computer you can't throw out a window")
print(text[0::3])

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print("Sub-string3")
final=("It's great to work with computers. They don't argue, they remember everything and they don't drink your beer")
print(final[::-1])