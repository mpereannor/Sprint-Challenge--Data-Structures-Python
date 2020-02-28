import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#attempt1
# duplicates.append(names_1)
# for name in names_2:
#   if not name in duplicates:
#     duplicates.append(name)

#attempt2
# duplicates = names_1 + names_2
# duplicates = list(set(duplicates))


#attempt3
# duplicates = names_1 + names_2
# for name in duplicates:
#   if duplicates[name] == duplicates[name + 1]:
#     del duplicates[name + 1]
#   else:
#     continue

#attempt4
#runtime 4 secs
# total = names_1 + names_2 
# for num in total: 
#     if num not in duplicates: 
#         duplicates.append(num) 

#attempt5
#runtime 4.4
# total = names_1 + names_2 
# [duplicates.append(x) for x in total if x not in duplicates]
class BinarySearchTree:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        return self.left.insert(value)
    elif value >= self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        return self.right.insert(value)
    return value
           
  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left != None:
        return self.left.contains(target)
      else: 
        return False
    elif target >= self.value: 
      if self.right != None:
        return self.right.contains(target)
      else: 
        return False
    else: 
      return False
      

binary = BinarySearchTree('names')
for names in names_1:
  binary.insert(names)
for name in names_2:
  if binary.contains(name):
    duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
