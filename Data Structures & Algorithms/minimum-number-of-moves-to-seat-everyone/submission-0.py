class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        shifts = 0
        for i in range(len(students)):
            shifts += (abs(students[i]-seats[i]))
        
        return shifts
