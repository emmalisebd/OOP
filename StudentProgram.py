import StudentClass as sc

student1 = sc.Student('1234', 'Emmalise', '06/11/2002', 'junior')

student1.student_age()
student1.register_date()

print(f"Age is: {student1.get_age()}")
print(f"Student can register between {student1.get_rdate()}")
