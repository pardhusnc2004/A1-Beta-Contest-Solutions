class RecentCounter:
    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        st = t-3000
        while self.q and self.q[0] < st:
            self.q.pop(0)
        self.q.append(t)
        
        return len(self.q)