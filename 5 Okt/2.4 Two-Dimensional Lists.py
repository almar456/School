studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   antw = []
   index = -1
   for x in studentencijfers:
        index = index + 1
        antw.append(sum(studentencijfers[index])/len(studentencijfers[index]))
   return antw

def gemiddelde_van_alle_studenten(studentencijfers):
   gemStudent = gemiddelde_per_student(studentencijfers)
   antw = sum(gemStudent) / len(studentencijfers)
   return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))