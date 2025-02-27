students = []

# 添加学生成绩的函数
def add_student(student_id, name, score):
    student = (student_id, name, score)
    students.append(student)

# 删除学生成绩的函数
def del_student(student_id):
    global students
    students = [s for s in students if s[0] != student_id]

# 修改学生成绩的函数
def update_student(student_id, new_score):
    for i, student in enumerate(students):
        if student[0] == student_id:
            # 更新指定索引位置的学生信息
            students[i] = (student[0], student[1], new_score)
            break

# 查询学生成绩
def query_student(student_id):
    for student in students:
        if student[0] == student_id:
            return student
    return None

# 测试
add_student(1, "Alice", 85)
add_student(2, "Bob", 90)
print(query_student(1))  # 输出: (1, 'Alice', 85)
update_student(1, 95)
print(query_student(1))  # 输出: (1, 'Alice', 95)
del_student(1)
print(students)  # 输出: [(1, 'Alice', 95)]

