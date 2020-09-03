#rachael graveling
#25/08/2020
#parallel arrays practice

#create arrays
names = []
scores = []
percentages = []
grades = []

#create loop for everything
for i in range (4):
  #input name
  name = input("Name: ")

  #input scores
  #validate score (not float or string)
  number = False
  while not number:
    number = True
    string_in = input("Score (out of 150): ")

    for letter in string_in:
      if letter < '0' or letter > '9':
        number = False
    
  score = int(string_in)

  #validate score (between 0 and 150)
  while score <0 or score >150:
    print("Please enter score again. It must be between 0 and 150.")
    score = int(input("Score (out of 150): "))

  
    
  #calculate percentage
  percentage = score/150 * 100

  #if statement to determine grades
  if percentage >=85:
    grade = "A"
  elif percentage <85 and percentage >= 70:
    grade = "B"
  elif percentage <70 and percentage >=55:
    grade = "C"
  elif percentage <55 and percentage >=40:
    grade = "D"
  else: 
    grade = "F"
  
  #round percentage
  percentage = round(percentage,2)

  #append info
  names.append(name)
  scores.append(score)
  percentages.append(percentage)
  grades.append(grade)

#print everything with formatting
print()
print (f'{"Name":20}{"Score":20}{"Percentage":20}{"Grade"}')

for i in range (4):
  print (f'{names[i]:20}{scores[i]:<20}{percentages[i]:<20}{grades[i]}')

print("a")


