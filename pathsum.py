numbers = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#We need to have an iterator that starts at 1 and keeps going up. This will select the next bunch of numbers (e.g., 1 at first, then the next 2, then the next 3, and so on.)
#Select the numbers and add to an array. Select the max one. Add to the current. Then +1.

numbers = numbers.splitlines()
j = 0
for i in range(0, len(numbers)):
  tempnum = numbers[i].split(" ")
  maxnum = int(max(tempnum))
  j = j + maxnum
  print j

print j

#only adjacent numbers wtf