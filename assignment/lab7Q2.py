def isogram(p):

  p = p.lower()

  unique = set()

  for char in p:
    if char in char.isalpha():
      if char in unique:
        return False
      unique.append(char)
  print(unique)
  return True


p = input("Enter any word or phrase: ")
if isogram(p):
  print("Phrase/s: {p}")
  print("Isogram (Yes/No): Yes")
else:
  print("Phrase/s: {p}")
  print("Isogram (Yes/No): No")


# did not work
# def isogram(p):

# #   p = p.lower()

# #   ori_letters = len(p)
# #   unique_letters = len(set(ori_letters))


# #   return ori_letters == unique_letters

# #   # for char in p:
# #   #   if char in char.isalpha():
# #   #     if char in unique:
# #   #       return False
# #   #     unique.append(char)
# #   # print(unique)
# #   # return True
# def solve(word):
#    char_list = []
#    for char in word:
#       if char.isalpha():
#          if char in char_list:
#             return f"Word: {word} \nIsogram (Yes/No): No"
#             char_list.append(char)
#    return f"Word: {word} \nIsogram (Yes/No): Yes"

# s = input("Enter any word: ")
# print("")
# print(solve(s))

# # p = input("Enter any word or phrase: ")
# # if isogram(p):
# #   print("Phrase/s: {p}")
# #   print("Isogram (Yes/No): Yes")
# # else:
# #   print("Phrase/s: {p}")
# #   print("Isogram (Yes/No): No")
