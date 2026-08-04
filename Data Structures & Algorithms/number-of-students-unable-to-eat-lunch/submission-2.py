class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        counts = Counter(students)
        print(counts)
        for s in sandwiches:
            if counts[s] > 0:
                counts[s] -= 1  
                print(counts)
            else:
                break
        
        for n in counts.values():
            result = result + n
        return result
