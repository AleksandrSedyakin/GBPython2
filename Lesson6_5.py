class Stat:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stat):
    def draw(self):
        print('Ручка пошла')


class Pencil(Stat):
    def draw(self):
        print('Карандаш в деле!')


class Handle(Stat):
    def draw(self):
        print('Маркер размечает по красоте')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

stat_box = [pen, pencil, handle]
for stat in stat_box:
    stat.draw()