from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter
        
        # special case: if num == 0, robot should face South if at origin after full cycle
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3  # South
            return
        
        while num > 0:
            if self.dir == 0:  # East
                steps = min(num, self.w - 1 - self.x)
                self.x += steps
            elif self.dir == 1:  # North
                steps = min(num, self.h - 1 - self.y)
                self.y += steps
            elif self.dir == 2:  # West
                steps = min(num, self.x)
                self.x -= steps
            else:  # South
                steps = min(num, self.y)
                self.y -= steps

            num -= steps

            # If we hit boundary, turn
            if num > 0:
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]