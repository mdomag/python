import random

class CellularAutomaton:
    def __init__(self, rule, sequence_length, steps):
        self.rule = rule
        self.sequence_length = sequence_length
        self.steps = steps
        self.sequence = list("".join(random.choice('*_') for i in range(sequence_length+2)))
        self.sequence[0], self.sequence[-1] = self.sequence[-2], self.sequence[1] #zapetla sekwencje

    def evolve(self):
        print(f"zasada: {self.rule} dlugosc ciagu: {self.sequence_length } liczba krokow: {self.steps}")
        patterns = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
        print(f"{'STEPS'.center(self.sequence_length*5, '_')}")
        print(self.sequence[1:self.sequence_length +1])
        for _ in range(self.steps):
            temp = '_'
            for j in range(1, self.sequence_length+1):
                cur = int(self.rule[patterns.index(self.sequence[j-1]+self.sequence[j]+self.sequence[j+1])])
                self.sequence[j-1] = temp
                temp = '*' if cur else '_'
            self.sequence[self.sequence_length] = temp
            self.sequence[0], self.sequence[-1] = self.sequence[-2], self.sequence[1]
            print(self.sequence[1:self.sequence_length +1])
    
if __name__ == '__main__':
    print("podaj zestaw regul")
    rule = f'{int(input()):08b}'
    print("podaj dlugosc ciagu")
    sequence_length  = int(input())
    print("podaj liczbe krokow")
    steps = int(input())
    
    automaton = CellularAutomaton(rule, sequence_length, steps)
    automaton.evolve()