class StockSpanner:

    def __init__(self):
        self.index = 0
        self.stack = []

    def next(self, price: int) -> int:
        # 1. Safely pop all smaller or equal elements.
        # "while self.stack" ensures we never check self.stack[-1] if it's empty!
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        # 2. Calculate the span based on whether the stack emptied out
        if not self.stack:
            # If stack is empty, this price is bigger than EVERYTHING before it
            res = self.index + 1
        else:
            # Otherwise, subtract the index of the closest bigger number
            res = self.index - self.stack[-1][1]
        
        # 3. CRITICAL: ALWAYS push the current item and increment index BEFORE returning
        self.stack.append((price, self.index))
        self.index += 1
        
        return res





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)