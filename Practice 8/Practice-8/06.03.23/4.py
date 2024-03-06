class Table():
    def __init__(self, h, w, l):
        self.height = h
        self.width = w
        self.length = l
    def print_size(self):
        print(f'Висота: {self.height} cm \nШирина: {self.width} cm \nДовжина: {self.length} cm')


class KitchenTable(Table):
# class ім'я(по-батькові)
    def is_kitchen(self):
        if self.width <= 100 and self.length <= 100:
            print("Це кухонний стіл.")
        else: 
            print("Це НЕ кухонний стіл.")


table1 = Table(50, 100, 50)
# table1.print_size()
table2 = KitchenTable(150, 100, 150)
table2.print_size()
table2.is_kitchen()
table3 = KitchenTable(90, 90, 90)
table3.print_size()
table3.is_kitchen()
KitchenTable.is_kitchen(table1)