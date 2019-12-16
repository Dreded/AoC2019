class SantaFuel():
    def __init__(self):
        with open(r'Day1_input.txt', 'r') as f:
            self.input = list(map(int,f.read().strip().split()))

    def PartOne(self):
        fuel = 0
        for mass in self.input:
            fuel += mass//3-2
        return fuel

    def PartTwo(self):
        fuel = 0
        for mass in self.input:
            while mass//3-2 > 0:
                mass = mass//3-2
                fuel += mass
        return fuel

answer = SantaFuel() # Test
print("PartOne: {}".format(answer.PartOne()))
print("PartTwo: {}".format(answer.PartTwo()))