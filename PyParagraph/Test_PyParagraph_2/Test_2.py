# The following code allowed us to round our results to the next or the last value or decimal place and to 
# export our results to a text file.
import math
import os

# The following code allowed us to locate our Test_Text_2.txt text file.
textpath = '/Users/azpunit/Desktop/Extra-Python-Challenge/PyParagraph/Test_PyParagraph_2/Test_Text_2.txt'

# The following code allowed us to read our text and assign a string to it.
with open(textpath, 'r') as text: 
    Raw_Text = text.read()

# The following code was used to sum the number of letters.
List_For_Letters_To_Count = Raw_Text.split(" ")
Total_Letters = 0
for words in List_For_Letters_To_Count:
    Total_Letters += len(words)

# The following code allowed us to have a lists of punctuation marks to be replaced with nothing or with a space.
Characters_To_Replace_With_Nothing = [",", "/", "[", "]", "(", ")", "{", "}", "$", "@", "#", "%", "&", "*", "_", "+", "=", ">", "<", "" ", " ""]
Characters_To_Replace_With_A_Space = ["-", "'"]

# The following code allowed us to create lists for counting the values in them by using the len() function.
List_Of_Words = []
List_Of_Words_2 = []
List_Of_Sentences = []

# The following code allowed us removed all the punctuation marks from our text that we didn't need.
for character in Characters_To_Replace_With_Nothing:
    Raw_Text = Raw_Text.replace(character, "", 100000000)

for character_1 in Characters_To_Replace_With_A_Space:
    Raw_Text = Raw_Text.replace(character_1, " ", 100000000)

# The following code allowed us to count the number of words and sentences in our text.
List_Of_Words = Raw_Text.split(" ")
List_Of_Sentences = Raw_Text.split(". ")
Word_Count = len(List_Of_Words)
Sentence_Count = len(List_Of_Sentences)

# The following code allowed us to define functions that round up to next decimal place and that rounds down to the last
# integer by still having a 0 after the coma. All of that was only done to thereafter arrive to the same results a those
# that were given to us in the prompt. 
def round_up(value, decimal=0): 
    multiplier = 10 ** decimal
    return math.ceil(value * multiplier) / multiplier

def round_down(value, decimal=0): 
    multiplier = 10 ** decimal
    return math.trunc(value * multiplier) / multiplier

# The following code allows to calculate the average number of letters per word and the average sentence lenght in
# terms of words. 
Average_Letter_Per_Word = round_up((Total_Letters/Word_Count), 1)
Average_Sentence_Lenght = round_down((Word_Count/Sentence_Count), 0)

# The following code allows to print our final text with the value that were previously found in terminal as it is
# in the prompt.
print(f"Paragraph Analysis")
print(f"----------------")
print(f"Appoximate Word Count: {Word_Count}")
print(f"Approximate Sentence Count: {Sentence_Count}")
print(f"Average Letter Count: {Average_Letter_Per_Word}")
print(f"Average Sentence Lenght: {Average_Sentence_Lenght}")

# The following code allowed me to create my Info_Text_Test_2.txt text file.
textpath_2 = os.path.join('/Users/azpunit/Desktop/Extra-Python-Challenge/PyParagraph/Test_PyParagraph_2/Info_Text_Test_2.txt')

# The following code allowed me to populate the results that I previously printed in terminal on my text file. 
with open(textpath_2, 'w') as text:    
    text.write(f"Paragraph Analysis\n")
    text.write(f"----------------\n")
    text.write(f"Appoximate Word Count: {Word_Count}\n")
    text.write(f"Approximate Sentence Count: {Sentence_Count}\n")
    text.write(f"Average Letter Count: {Average_Letter_Per_Word}\n")
    text.write(f"Average Sentence Lenght: {Average_Sentence_Lenght}\n")








