
class RestaurantOrder:
    """Class to manage restaurant orders."""
    
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # Dictionary: item -> price
    
    def display_order(self):
        """Display the order details."""
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer: {self.customer_name}")
        print("Items:")
        for item, price in self.items.items():
            print(f"  {item}: ${price:.2f}")
    
    def calculate_subtotal(self):
        """Calculate subtotal of all items."""
        return sum(self.items.values())
    
    def calculate_total_bill(self, tax_rate=0.1):
        """Calculate total bill with tax."""
        subtotal = self.calculate_subtotal()
        tax = subtotal * tax_rate
        return subtotal + tax
    
    def print_bill_summary(self, tax_rate=0.1):
        """Print complete bill summary."""
        self.display_order()
        subtotal = self.calculate_subtotal()
        tax = subtotal * tax_rate
        total = self.calculate_total_bill(tax_rate)
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total Bill: ${total:.2f}\n")


# Dynamic input
order_id = input("Enter Order ID: ")
customer_name = input("Enter Customer Name: ")
num_items = int(input("Enter number of items: "))
items = {}
for _ in range(num_items):
    item = input("Enter item name: ")
    price = float(input(f"Enter price for {item}: "))
    items[item] = price

# Create instance and print bill
order = RestaurantOrder(order_id, customer_name, items)
order.print_bill_summary()