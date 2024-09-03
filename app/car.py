class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_required_fuel(self, location_a: list,
                                location_b: list) -> float:
        x_a, y_a = location_a
        x_b, y_b = location_b
        distance = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
        return 2 * distance * self.fuel_consumption / 100
