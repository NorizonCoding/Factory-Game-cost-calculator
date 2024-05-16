cost = dict()


class Material:

    resource = "raw"

    def __init__(self, name):
        self.name = name


class Part:

    resource = "part"

    def __init__(self, name, parts, amount):
        self.name = name
        self.parts = parts
        self.amount = amount

    def cost_calc(self, number):
        global cost  # creates the dictionary
        for key in self.parts.keys():  # iterates through every part, the "key" variable has the key of the part
            if key.resource == "part":  # checks if key is string (aka raw resource)
                cost.update(key.cost_calc(self.parts[key] * number / self.amount))  # updates value
            else:
                if cost.get(key.name) is None:
                    cost.update({key.name: self.parts[key] * number / self.amount})
                else:
                    cost.update({key.name: cost.get(key.name) + (self.parts[key] * number / self.amount)})
        return cost




iron_ingot = Material("Iron Ingot")
copper_ingot = Material("Copper Ingot")
silicon_ingot = Material("Silicon Ingot")
titanium_ingot = Material("Titanium Ingot")
glass = Material("Glass")
magnet = Material("Magnet")
graphite = Material("Graphite")
graphene = Material("Graphene")
water = Material("Water")
grating_crystal = Material("Grating Crystal")
hydrogen = Material("Hydrogen")
deuterium = Material("Deuterium")
sulfuric_acid = Material("Sulfuric Acid")
carbon_nanotube = Material("Carbon Nanotube")


circuit_board = Part("Circuit Board", {iron_ingot: 2, copper_ingot: 1}, 2)
gear = Part("Gear", {iron_ingot: 1}, 1)
em_coil = Part("Magnetic Coil", {magnet: 2, copper_ingot: 1}, 2)
transistor = Part("Transistor", {silicon_ingot: 2, copper_ingot: 1}, 2)
steel = Part("Steel", {iron_ingot: 3}, 1)
titanium_glass = Part("Titanium Glass", {titanium_ingot: 2, glass: 2, water: 2}, 2)
crystal_casimir = Part("Casimir Crystal", {grating_crystal: 8, graphene: 2, hydrogen: 12}, 1)


cpu = Part("CPU", {circuit_board: 2, transistor: 2}, 1)
plane_filter = Part("Plane Filter", {crystal_casimir: 1, titanium_glass: 2}, 1)
electric_engine = Part("Electric Engine", {iron_ingot: 2, gear: 1, em_coil: 1}, 2)
turbine = Part("Magnetic Turbine", {electric_engine: 2, em_coil: 2}, 1)
super_ring = Part("Super-Magnetic Ring", {turbine: 2, magnet: 3, graphite: 1}, 1)
titanium_alloy = Part("Titanium Alloy", {titanium_ingot: 4, steel: 4, sulfuric_acid: 4}, 4)
solar_sail = Material("Solar Sail")
frame_material = Part("Frame Material", {carbon_nanotube: 4, titanium_alloy: 1, silicon_ingot: 1}, 1)


quantum_CPU = Part("Quantum Chip", {cpu: 2, plane_filter: 2}, 1)
deuterium_fuel = Part("Deuterium Fuel Rod", {titanium_alloy: 1, deuterium: 20, super_ring: 1}, 2)
dyson_component = Part("Dyson Sphere Component", {frame_material: 6, solar_sail: 6, cpu: 6}, 2)


carrier_rocket = Part("Small Carrier Rocket", {quantum_CPU: 2, deuterium_fuel: 4, dyson_component: 2}, 1)


