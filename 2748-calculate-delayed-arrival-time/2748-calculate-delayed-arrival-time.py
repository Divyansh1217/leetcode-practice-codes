class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        a=arrivalTime + delayedTime
        if a>=24:
            return int(a%24)
        else:
            return a