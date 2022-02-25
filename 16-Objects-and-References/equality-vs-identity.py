students = ["Bob", "Tom", "Kate"]
athletes = students
nerds = ["Bob", "Tom", "Kate"]

print(students == athletes)
print(students == nerds)

print(students is athletes) #True, bo powiedzieliśmy systemowi, ze to jest to samo
print(students is nerds) # False, bo listy będą miały inne ID, czyli inną tożsamość

# https://www.blog.pythonlibrary.org/2017/02/28/python-101-equality-vs-identity/