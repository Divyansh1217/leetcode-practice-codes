class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
         a = 0
         seats=sorted(seats)
         students.sort()
         for i in range(len(students)):
             a += abs(students[i] - seats[i])
         return a