

class Registry:
    request_count = 0
    staff_info = []
    def __init__(self, Date, Name, Staff_ID, Order_Status):
        Date = input("Please input the date")
        Name = input("Please input a name")
        Staff_ID = input("Please input a Staff ID")
        Order_Status = input("Please input current status of order")
        Registry.request_count += 1
        info_set = [Date, Name, Staff_ID, Registry.request_count, Order_Status]
        Registry.staff_info.append (info_set)

    def member_order(self):
        for si in Registry.staff_info:
            item = input("Please enter item")
            if item == "":
                print("Please enter valid item name")
            price = float(input("Please enter price"))
            quantity = int(input("Please enter quantity"))
            current_cost = price*quantity
            print(f"Items:{item} amounts to {current_cost}")

registry1 = Registry()
#Still wrong, might try another way
#If coding another method with inputs for parameters (Date, Name, Staff ID, Status), doesn't that
#invalidate the need for initialization? Or does initialized parameters act as placeholders?


