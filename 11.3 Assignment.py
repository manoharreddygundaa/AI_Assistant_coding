# class ContactManagerArray:
#     def __init__(self):
#         self.contacts = []

#     # Add Contact
#     def add_contact(self, name, phone):
#         self.contacts.append({"name": name, "phone": phone})
#         print("Contact added")

#     # Search Contact
#     def search_contact(self, name):
#         for contact in self.contacts:
#             if contact["name"] == name:
#                 print("Found:", contact)
#                 return
#         print("Contact not found")

#     # Delete Contact
#     def delete_contact(self, name):
#         for i in range(len(self.contacts)):
#             if self.contacts[i]["name"] == name:
#                 del self.contacts[i]
#                 print("Contact deleted")
#                 return
#         print("Contact not found")


# # Example Usage
# cm = ContactManagerArray()
# cm.add_contact("Ravi", "9876543210")
# cm.add_contact("Anita", "9123456780")

# cm.search_contact("Ravi")
# cm.delete_contact("Ravi")
# cm.search_contact("Ravi")
# 
# class PriorityBookRequest:
#     def __init__(self):
#         self.queue = []

#     # enqueue() with priority
#     def enqueue(self, name, role, book):
#         request = {"name": name, "role": role, "book": book}

#         # Faculty gets higher priority
#         if role.lower() == "faculty":
#             self.queue.insert(0, request)
#         else:
#             self.queue.append(request)

#         print("Request added:", request)

#     # dequeue()
#     def dequeue(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#             return

#         request = self.queue.pop(0)
#         print("Processing request:", request)


# # Testing Priority Queue
# pq = PriorityBookRequest()

# pq.enqueue("Ravi", "Student", "Python")
# pq.enqueue("Dr.Sharma", "Faculty", "Machine Learning")
# pq.enqueue("Anita", "Student", "DBMS")

# pq.dequeue()
# pq.dequeue()
# pq.dequeue()
# class HelpDeskStack:
#     def __init__(self, size=10):
#         self.stack = []
#         self.size = size

#     # push(ticket)
#     def push(self, ticket):
#         if self.is_full():
#             print("Stack is full. Cannot add ticket.")
#             return
#         self.stack.append(ticket)
#         print("Ticket added:", ticket)

#     # pop()
#     def pop(self):
#         if self.is_empty():
#             print("No tickets to resolve.")
#             return
#         ticket = self.stack.pop()
#         print("Resolved ticket:", ticket)

#     # peek()
#     def peek(self):
#         if self.is_empty():
#             print("Stack is empty.")
#             return
#         print("Current top ticket:", self.stack[-1])

#     # check empty (Copilot suggestion)
#     def is_empty(self):
#         return len(self.stack) == 0

#     # check full (Copilot suggestion)
#     def is_full(self):
#         return len(self.stack) == self.size
# helpdesk = HelpDeskStack()

# helpdesk.push("WiFi not working")
# helpdesk.push("Login issue")
# helpdesk.push("Software installation")
# helpdesk.push("Printer problem")
# helpdesk.push("Email access error")

# helpdesk.peek()

# helpdesk.pop()
# helpdesk.pop()
# helpdesk.pop()
# helpdesk.pop()
# helpdesk.pop()
# class HashTable:
#     def __init__(self, size=10):
#         # Create empty hash table
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     # Hash function
#     def hash_function(self, key):
#         # Converts key into index
#         return hash(key) % self.size

#     # Insert operation
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         bucket = self.table[index]

#         # Update value if key already exists
#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 print("Updated:", key)
#                 return

#         # Otherwise add new key-value pair
#         bucket.append((key, value))
#         print("Inserted:", key)

#     # Search operation
#     def search(self, key):
#         index = self.hash_function(key)
#         bucket = self.table[index]

#         for k, v in bucket:
#             if k == key:
#                 print("Found:", key, "->", v)
#                 return v

#         print("Key not found")
#         return None

#     # Delete operation
#     def delete(self, key):
#         index = self.hash_function(key)
#         bucket = self.table[index]

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 print("Deleted:", key)
#                 return

#         print("Key not found")
# ht = HashTable()

# ht.insert("Ravi", "9876543210")
# ht.insert("Anita", "9123456780")
# ht.insert("Rahul", "9988776655")

# ht.search("Anita")

# ht.delete("Ravi")
# ht.search("Ravi")
class CafeteriaQueue:
    def __init__(self):
        self.queue = []

    # Place order
    def place_order(self, student, item):
        order = {"student": student, "item": item}
        self.queue.append(order)
        print("Order placed:", order)

    # Serve order
    def serve_order(self):
        if len(self.queue) == 0:
            print("No orders to serve")
            return

        order = self.queue.pop(0)
        print("Order served:", order)

    # View next order
    def next_order(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Next order:", self.queue[0])
cafeteria = CafeteriaQueue()

cafeteria.place_order("Ravi", "Dosa")
cafeteria.place_order("Anita", "Idli")
cafeteria.place_order("Rahul", "Biryani")

cafeteria.next_order()

cafeteria.serve_order()
cafeteria.serve_order()
cafeteria.serve_order()