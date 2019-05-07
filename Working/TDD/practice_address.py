"""Define a class called Address that has the attributes
below. All fields have a default value of “” (empty string)
except for country which is defaulted to “Canada”"""

class Address():
    def __int__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.postal_code = ""
        self.city = ""
        self.province = ""
        self.country = "Canada"

"""Define a main() function and within it, create two
Address instances, one called home_address, another 
called work_address. Assign values to the object fields.
Use the instances to print out each address"""
def print


def main():
    home_address = Address()
    home_address.address_line1 = "276 Moore Park ave"
    home_address.address_line2 = "175 Hilda ave"
    home_address.postal_code = "M2M"
    home_address.city = "North York"
    home_address.provice = "Ontario"

    print(" **** HOME ADDRESS **** ")
    print_address(home_address)


main()