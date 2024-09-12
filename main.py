# def words(file_path):
#     with open(file_path, 'r') as file:
#         text = file.read().lower()  
#         words = text.split() 
#         words = [word.strip('.,!?;:') for word in words] 
#         return len(words)

# def sentence(file_path):
#     with open(file_path, 'r') as file:
#         text = file.read()
#         sentences = text.replace('?', '.').replace('!', '.').split('.')  
#         sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  
#         return len(sentences)

# def lenght(file_path):
#     with open(file_path, 'r') as file:
#         text = file.read().lower() 
#         words = text.split()  
#         words = [word.strip('.,!?;:') for word in words]  
#         total_chars = sum(len(word) for word in words)
#         return total_chars / len(words)

# def common(file_path, n=1):
#     with open(file_path, 'r') as file:
#         text = file.read().lower()  
#         words = text.split()  
#         words = [word.strip('.,!?;:') for word in words]  
#         word_counts = {}
#         for word in words:
#             if word in word_counts:
#                 word_counts[word] += 1
#             else:
#                 word_counts[word] = 1
#         common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]
#         return common_words

# def analyze_text(file_path):
#     num_words = words(file_path)
#     num_sentences = sentence(file_path)
#     avg_word_length = lenght(file_path)
#     common_words = common(file_path)

#     print(f"Number of words: {num_words}")
#     print(f"Number of sentences: {num_sentences}")
#     print(f"Average word length: {avg_word_length:.2f}")
#     print("Most common words:")
#     for word, count in common_words:
#         print(f"{word}: {count}")

# analyze_text("example.txt")



# def simple_hash(input_string):
#     num_value = hash(input_string)
#     hex_string = hex(num_value)[2:]
#     padded_hex_string = hex_string.zfill(16)
    
#     return padded_hex_string

# input_string = "password123"
# hash_string = simple_hash(input_string)
# print(hash_string)







class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def view_courses(self):
        return self.courses
    
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def view_students(self):
        return self.students
    
class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def register_student(self, student):
        self.students.append(student)

    def create_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course):
        student.add_course(course)
        course.add_student(student)

    def drop_student(self, student, course):
        student.remove_course(course)
        course.remove_student(student)

school = School()

student1 = Student("John Doe", "101")
student2 = Student("Jonny Wane", "102")
student3 = Student("Bob Smith", "103")

school.register_student(student1)
school.register_student(student2)
school.register_student(student3)
 
course1 = Course("Math", "101")
course2 = Course("English", "102")
course3 = Course("Science", "103")

school.create_course(course1)
school.create_course(course2)
school.create_course(course3)

school.enroll_student(student1, course1)
school.enroll_student(student1, course2)
school.enroll_student(student2, course2)
school.enroll_student(student3, course3)

print("Students enrolled in course", course2.course_name)
for student in course2.view_students():
    print(student.name)

print("Courses student", student1.name, "is enrolled in:")
for course in student1.view_courses():
    print(course.course_name)
