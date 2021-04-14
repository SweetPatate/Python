#Given a text as input, find and output the longest word.
txt = input()

txt_list = txt.split(" ")
#print(txt_list)

dictman = {i:len(i) for i in txt_list}
#print(dictman)

maxman = max(dictman[i] for i in txt_list)
#print(maxman)

for i in dictman:
  if dictman[i] == maxman:
    print(i)