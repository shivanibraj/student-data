import csv
import os

def cal_grade(cgpa1):
  if 9.0 <= cgpa1 <= 10.0:
    return 'O'
  elif 8.0 <= cgpa1<= 8.9:
    return 'A+'
  elif 7.0 <= cgpa1 <= 7.9:
    return 'A'
  elif 6.0 <= cgpa1 <= 6.9:
    return 'B+'
  elif 5.0 <= cgpa1 <= 5.9:
    return 'B'
  elif 5.0 <= cgpa1 <= 5.49:
    return 'C'
  elif 4.0 <= cgpa1 <= 4.9:
    return 'P'    
  else:
    return 'F' 
def min_max_norm(sign_in_count, x):
  """
  Normalizing a given value from sign_in_count list in the range a, b 
  """
  min_value = min(sign_in_count)
  max_value = max(sign_in_count)
  a = 0.0
  b = 10.0
  norm_value = a + b * ((x - min_value) / (max_value - min_value))
  return round(norm_value, 2)

stud_formatted_data = {}
csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
students_record = []
sign_in_count = []
with open('sample_student_data.csv', 'r') as readFile:
  reader = csv.reader(readFile, delimiter = " ")
  students_record = list(reader)

for row_data in students_record[1:]:
    sign_in_count.append(float(row_data[6]))



studs_row_data = []
header = ["StduentName", "Email", "Grade", "CGPA", "loginscore"]
studs_row_data.append(header)
for row in students_record[1:]:
    new_row_data = []
    new_row_data.append(row[1])
    new_row_data.append(row[2])
    grade = cal_grade(float(row[5]))
    new_row_data.append(grade)
    new_row_data.append(row_data[5])
        # appending login score
    n_value = min_max_norm(sign_in_count, int(row[6]))
    print(n_value)
    new_row_data.append(n_value)
    studs_row_data.append(new_row_data)

with open("student_records.csv", 'w') as writeFile:
  writer = csv.writer(writeFile, dialect='myDialect')
  writer.writerows(studs_row_data)
writeFile.close()     
readFile.close()