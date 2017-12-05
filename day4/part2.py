from collections import Counter
try:
   f = open("input.txt")
except:
   f = open("day4/input.txt")
lines = f.read().split('\n')
valid=0
for line in lines:
   words = line.split()
   sorted_words = [''.join(sorted(word)) for word in words]
   c = Counter(sorted_words).most_common(1)
   if(c[0][1]==1):
      valid+=1
print(valid)