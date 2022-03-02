from typing import Optional, List

class Component:
    def __init__(self,
                 name: str,
                 reward: str = None,
                 quant: int = None,
                 forward: Optional[List] = None ,
                 backward: Optional[List] = None):
        self.name = name
        self.reward = reward
        self.quant = quant
        self.forward = forward
        self.backward = backward

    def __repr__(self):

        return self.name

    def backwards(self,level = 0):
        if self.name:
            print('-' * level + self.name)
            if self.backward:
                for i in self.backward:
                    i.backwards(level + 1)

    def forwards(self,level = 0):
        if self.name:
            print('-' * level + self.name)
            if self.forward:
                for i in self.forward:
                    i.forwards(level + 1)
