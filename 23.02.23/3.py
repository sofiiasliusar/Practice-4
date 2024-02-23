class Building_Material():
    amount = 0
    # list = []

    def __init__(self, name, density, durability, thermal_conductivity, cost, strength, fire_resistance, eco_friendly, color):
        self.name = name
        self.density = density
        self.durability = durability
        self.thermal_conductivity = thermal_conductivity
        self.cost = cost
        self.strength = strength
        self.fire_resistance = fire_resistance
        self.eco_friendly = eco_friendly
        self.color = color

        Building_Material.amount +=1
        # Building_Material.list.append(self.name)

    def __del__(self):
        print(f"{self.name} вилучено зі списку матеріалів.")
        Building_Material.amount -=1
        # Building_Material.list.remove(self.name)
        if Building_Material.amount == 0:
            print(f"{self.name} це був останній матеріал.")
        else:
            print("Залишилась така кількість матеріалів: {0}".format(Building_Material.amount))
    
    def info(self):
        print(f"Матеріал: {self.name}.")
        print(f"Щільність: {self.density}.")
        print(f"Строк придатності: {self.durability} років.")
        print(f"Теплопровідність: {self.thermal_conductivity}.")
        print(f"Ціна: {self.cost}.")
        print(f"Міцність: {self.strength}.")
        print(f"Стійкість до горіння: {self.fire_resistance}.")
        print(f"Екологічність: {self.eco_friendly}.")
        print(f"Колір: {self.color}")

    def how_many():
        print("Rількість матеріалів: {0}".format(Building_Material.amount))
        # for name in Building_Material.list:
            # print(f"- {name}")

concrete = Building_Material("Бетон", 2400, 75, 1.7, 100, 25, "висока", "екологічний", "сірий")        
wood = Building_Material("Дерево", 600, 50, 0.1, 80, 10, "низька", "екологічний", "коричневий")
metal = Building_Material("Метал", 7800, 100, 50, 150, 80, "середня", "не екологічний", "сірий")
plastic = Building_Material("Пластик", 900, 30, 0.2, 50, 15, "низька", "не екологічний", "білий")
stone = Building_Material("Камінь", 2700, 150, 2.5, 120, 60, "висока", "екологічний", "сірий")
glass = Building_Material("Скло", 2500, 80, 1.0, 200, 40, "низька", "екологічний", "прозорий")

glass.info()

Building_Material.how_many()
del plastic
Building_Material.how_many()

