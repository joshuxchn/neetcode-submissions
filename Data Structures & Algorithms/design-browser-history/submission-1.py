class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        #need this var, nodes are different codes each time
        x = Node(url)
        if self.curr:
            self.curr.next = x
            x.prev = self.curr
        self.curr = x
        self.curr.next = None #clear forward history
        

    def back(self, steps: int) -> str:
        while steps != 0 and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val
        
        

    def forward(self, steps: int) -> str:
        while steps != 0 and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)