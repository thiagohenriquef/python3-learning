class Car:
    def __init__(self, max_speed):
        self.speed = 0
        self.max_speed = max_speed

    def speed_up(self, velocity=5):
        self.speed = self.speed + velocity if self.speed + \
            velocity <= self.max_speed else self.max_speed
        return self.speed

    def brake(self, delta=5):
        self.speed = self.speed - delta if self.speed - delta >= 0 else 0
        return self.speed


if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        print(c1.speed_up(8))

    for _ in range(25):
        print(c1.brake(delta=20))
