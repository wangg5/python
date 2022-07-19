# immutable data type in python
#======= tuple, set, string, integer, float, complex
#
#  mutable data type in python
#====== list, dict

s = "hello"
# 
for c in s:
    print(c)

if 'h' in s:
    print("h in hello")

for i in range(len(s)):
    print(f"s[{i}] = {s[i]}")
# we can not change any character in s.
# we can not do something like this: s[2] = 'k'
# There is a replace method for a string. However, this method
# will replace all some character in s.
# It returns a copy of the string where all occurrences of a substring are replaced with another substring. 
print(s.replace('l', 'k'))  # hekko
print(s) # hello

# if you really want to change a character in the string, you can do this.
s = s[:2] + 'k' + s[3:]
print(s)
