import math

class Flower:
    def __init__(self, position, volume):
        #self.name = name    # имя человека
        #self.age = 1        # возраст человека position: int = 0
        self.position: int = position
        self.volume: int = volume
    def move(self, direction: str) -> None:     # метод 
        if (direction == "right"):
            self.position += 1
        if (direction == "left"):
            self.position -= 1
            


class Leika:
    position: int
    volume: int
    step_counter: int



def GeometricMean(a: float, b: float) -> float:
    return math.sqrt( a * a + b * b )


def main():
    print(GeometricMean(3, 4))
    a = Flower()
    a.move("right")
    print(a.position)

if __name__ == '__main__':
    main()