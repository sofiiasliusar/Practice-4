class Horse():
    def run(self):
        print('I\'m running')
# виведення апострофа
class Bird():
    def fly(self):
        print("I'm flying")

class Unicorn(Horse, Bird):
    pass

unicorn = Unicorn

unicorn.run()
unicorn.fly()
