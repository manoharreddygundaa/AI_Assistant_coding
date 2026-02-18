#Write a function that converts a date from dd/mm/yyyy to yyyy-mm-dd and correctly handles leading zeros.

def convert_date(date_str):
    day, month, year = date_str.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
# Example usage
print(convert_date("5/3/2023"))    # Output: 2023-03-05
print(convert_date("15/12/2021"))  # Output: 2021-12-15