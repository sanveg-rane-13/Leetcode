class Solution:

    def __init__(self, w: List[int]):
        self.numbers = [i for i in range(len(w))]
        self.probability = w

    def pickIndex(self) -> int:
        return choices(self.numbers, self.probability)[0]
