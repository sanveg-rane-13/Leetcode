# Number of recent calls
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        strt, end = t, t - 3000
        
        self.queue.append(strt)
        while self.queue and self.queue[0] < end:
            self.queue.popleft()
            
        return len(self.queue)