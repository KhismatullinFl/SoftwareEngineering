class Tomato:
    states = ('цветет', 'зеленый', 'желтый', 'красный')
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]
    def grow(self):
        i = Tomato.states.index(self._state)
        if i < len(Tomato.states) - 1:
            self._state = Tomato.states[i+1]
    def is_ripe(self):
        return self._state == Tomato.states[-1]

class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i+1) for i in range(count)]
    def grow_all(self):
        for t in self.tomatoes:
            t.grow()
    def all_are_ripe(self):
        return all(t.is_ripe() for t in self.tomatoes)
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай.")
        else:
            print(f"{self.name}: не все помидоры созрели.")
    def knowledge_base():
        print('Поливайте, удобряйте, собирайте')

if __name__ == '__main__':
    Gardener.knowledge_base()
    bush = TomatoBush(3)
    g = Gardener('Иван', bush)
    while bush.tomatoes:
        g.work()
        print([t._state for t in bush.tomatoes]) 
        g.harvest()
