class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:

            if students and students[0] == 1:
                if sandwiches and sandwiches[0] == 1:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    currentStudent = students.pop(0)
                    students.append(currentStudent)


            if students and students[0] == 0:
                if sandwiches and sandwiches[0] == 0:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    currentStudent = students.pop(0)
                    students.append(currentStudent)

            if sandwiches and students and  (not 0 in students) and sandwiches[0] == 0: 
                break

            if sandwiches and students and (not 1 in students) and sandwiches[0] == 1:
                break     
    
        return len(students)
                  