def print_details(**kwargs):
    print(kwargs)

print_details(course="ICS", year = 2.1, unit = "DSA")

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(course="ICS", year = 2.1, unit = "DSA")


