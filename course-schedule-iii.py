class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        pq = []
        total_duration = 0

        for duration, last_date in courses:
            heapq.heappush(pq,-duration)
            total_duration += duration
            if total_duration>last_date:
                total_duration += heapq.heappop(pq)
        
        return len(pq)