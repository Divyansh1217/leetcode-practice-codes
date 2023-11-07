class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
         qadam = 0
         seats=sorted(seats)
         students.sort()
         for st in range(len(students)):
             qadam += abs(students[st] - seats[st])
         return qadam