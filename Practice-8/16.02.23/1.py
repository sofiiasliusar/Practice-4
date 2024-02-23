class Building_Material():
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
concrete = Building_Material("Бетон", 2400, 75, 1.7, 100, 25, "висока", "екологічний", "сірий")        
concrete.info()
    