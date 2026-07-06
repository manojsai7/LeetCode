class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start time (ascending), then by end time (descending)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        valid_intervals = 0
        max_end = -1
        
        for start, end in intervals:
            # If this interval sticks out further than our current umbrella
            if end > max_end:
                valid_intervals += 1
                max_end = end  # Update the umbrella
                
        return valid_intervals