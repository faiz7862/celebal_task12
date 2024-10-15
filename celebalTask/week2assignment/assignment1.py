class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        standard_fare = super().fare()
        maintenance_charge = 0.1 * standard_fare
        total_fare = standard_fare + maintenance_charge
        return total_fare

# Example usage:
if __name__ == "__main__":
    bus = Bus("School Bus", 50)
    print(f"The total fare for the bus is: {bus.fare()}")
