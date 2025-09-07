# Q1
class WasteCollection:
    def __init__(self, address_in, occupants_in, base_cost=500):
        self.address = address_in
        self.occupants = occupants_in
        self.num_collections = 0
        self.total_weight_collected = 0
        self.total_cost_due = base_cost
        self.bill_paid = False  # boolean

    def collect(self, weight):
        self.num_collections += 1
        self.total_weight_collected += weight
        self.calculate_collection_cost(weight)

    def calculate_collection_cost(self, weight):
        extra_weight = max(0, weight - 50)
        cost = extra_weight * 1.00
        self.total_cost_due += cost
        print("Collection cost for :", weight, "kg : €", cost)

    def calculate_average(self):
        if self.num_collections == 0:
            return 0
        return round(self.total_weight_collected / self.num_collections, 2)

    def calculate_average_per_person(self):
        if self.num_collections == 0:
            return 0
        return round(self.total_weight_collected / self.occupants / self.num_collections, 2)

    def pay_bill(self, amount):
        if amount >= self.total_cost_due:
            self.bill_paid = True
            return True
        else:
            self.total_cost_due -= amount
            return False

    def print(self):
        print("******************************************")
        print("*      Waste Collection Details          *")
        print("******************************************")
        print("Address         :", self.address)
        print("Number of Occupants           :", self.occupants)
        print("Number of Collections made   :", self.num_collections)
        print("Total weight collected       :", self.total_weight_collected)
        print("Total cost due       :", self.total_cost_due)
        print("Bill paid in full       :", self.bill_paid)


# main body of code
user_address = str(input("Enter the address :"))
user_occupants = int(input("Enter number of occupants"))

collection_1 = WasteCollection(user_address, user_occupants, 80)
collection_2 = WasteCollection(user_address, user_occupants, 45)
collection_3 = WasteCollection(user_address, user_occupants, 80)

collection_1.print()
print()
collection_2.print()
print()
collection_3.print()

class OfficeWasteCollection(WasteCollection):
