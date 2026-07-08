class StockSpanner:

    def __init__(self):
        self.index = 0
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if not self.stack:
            res = self.index + 1
        else:
            res = self.index - self.stack[-1][1]
        
        self.stack.append((price, self.index))
        self.index += 1
        return res




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)