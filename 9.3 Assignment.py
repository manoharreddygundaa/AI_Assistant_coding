class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee = None  # Initially fee is not updated

    def fee_update(self, amount):
        self.fee = amount

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Fee:", self.fee if self.fee is not None else "Not Updated")
student1 = sru_student("Manohar", 101, "Yes")
student1.fee_update(50000)
student1.display_details()
