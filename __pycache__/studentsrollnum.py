def Student(roll_numbers):
  english_students = []
  for i in range(0, len(roll_numbers), 2):
    english_students.append(roll_numbers[i])
  return english_students

T = int(input())
for _ in range(T):
  N = int(input())
  roll_numbers = list(map(int, input().split()))
  english_students = Student(roll_numbers)
  print(*english_students)
