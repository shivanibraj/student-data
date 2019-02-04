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

# grade = cal_grade(7.90)
# print "Grade for given cgpa: 7.98: ", grade

stud_formatted_data = {}
"""
  stud_formatted_data = {
    "2014" = {
      "CS" = [stud1_record, stud2_record, ..],
      "IT" = [stud10_record, stud11_record, ..].
      ...
      ...,
      "ME" = [stud1_record, stud2_record, ..]
    },
    "2015" = {
      "p059" = [row_data1 ],
      "fpat019" = [row_data2],
      "CS" = [stud31_record, stud32_record, ..],
      "IT" = [stud41_record, stud42_record, ..].
      ...
      ...,
      "Civil" = [stud1_record, stud2_record, ..]
    },
    ...
    ...
    ...,
    "2019" = {
      "CS" = [stud6_record, stud7_record, ..],
      "IT" = [stud41_record, stud42_record, ..].
      ...
      ...,
      "B.Sc." = [stud1_record, stud2_record, ..]
    },
  }
"""

csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

students_record = []
with open('students_data.csv', 'r') as readFile:
  reader = csv.reader(readFile, delimiter = " ")
  students_record = list(reader)
  # Header: ['ID', 'Student Name', 'Student Email', 'Branch Code', 'Academic Batch', 'CGPA', 'Sign_In_Count']
  for row_data in students_record[1:]:
    if stud_formatted_data.get(row_data[4], None):
      if stud_formatted_data[row_data[4]].get(row_data[3], None):
        stud_formatted_data[row_data[4]][row_data[3]].append(row_data)
      else:
        stud_formatted_data[row_data[4]][row_data[3]] = []
        stud_formatted_data[row_data[4]][row_data[3]].append(row_data)
    else:
      stud_formatted_data[row_data[4]] = {}
      stud_formatted_data[row_data[4]][row_data[3]] = []
      stud_formatted_data[row_data[4]][row_data[3]].append(row_data)

  for batch, branch_data in stud_formatted_data.items():
    # ./2014/
    os.makedirs("./{}".format(batch))
    for branch, branch_student_data in branch_data.items():
      # ./2014/CS/
      os.makedirs("./{}/{}".format(batch, branch))
      studs_row_data = []
      header = ["StduentName", "Email", "Grade"]
      studs_row_data.append(header)
      for row in branch_student_data:
        new_row_data = []
        new_row_data.append(row[1])
        new_row_data.append(row[2])
        grade = cal_grade(float(row[5]))
        new_row_data.append(grade)
        studs_row_data.append(new_row_data)

      with open("./{}/{}/student_records.csv".format(batch, branch), 'w') as writeFile:
        writer = csv.writer(writeFile, dialect='myDialect')
        writer.writerows(studs_row_data)
      writeFile.close()     
readFile.close()
