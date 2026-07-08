class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.i = 0
        self.tally = 0
        self.sett = False
        self.nxt = 0          # index where the next letter starts

    def next(self) -> str:
        if not self.sett:
            if self.i >= len(self.s):
                return " "
            a = self.i
            while a + 1 < len(self.s) and self.s[a + 1].isdigit():
                a += 1
            self.tally = int(self.s[self.i + 1: a + 1])
            self.nxt = a + 1
            self.sett = True

        x = self.s[self.i]
        self.tally -= 1

        if self.tally == 0:
            self.i = self.nxt
            self.sett = False

        return x

    def hasNext(self) -> bool:
        return self.i != len(self.s)