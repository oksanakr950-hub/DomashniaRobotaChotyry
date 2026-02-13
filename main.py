class Sun:
    def shine(self):
        print("Sun is shining ☀️")

class Plant:
    def __init__(self, name):
        self.name = name
        self.height = 0

    def grow(self):
        self.height += 1
        print(f"{self.name} grows. Height: {self.height}")


sun = Sun()
plant = Plant("Flower")

for day in range(5):
    print(f"\nDay {day + 1}")
    sun.shine()
    plant.grow()
