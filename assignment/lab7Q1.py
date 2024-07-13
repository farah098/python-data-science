# Other method for user input
#  class PangramCheck:
#   def __init__(s): # initialize
#     s.sentence = ""

#   def isPangram(s): # method for input
#     s.sentence = input("Enter a sentence: ")
#     # checking whether the sentence have all the 26 alphabet or not
#     letters = set('abcdefghijklmnopqrstuvwxyz')
#     for char in letters:
#       if char not in s.sentence.lower():
#         return False
#     return True

#   def pangramDetermine(s):
#     # method to print out whether the sentence is pangram or not
#     pangram = s.isPangram()
#     if pangram == True:
#       print(f"Sentence: {s.sentence}")
#       print("Pangram: Yes")
#     else:
#       print(f"Sentence: {s.sentence}")
#       print("Pangram: No")

# check = PangramCheck()
# check.pangramDetermine()
#