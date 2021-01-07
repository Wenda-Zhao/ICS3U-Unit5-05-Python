#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for address


def calculate_address(addressee, apt_number, street_number, street_name,
                      city, province, postal_code):
    # this function is make address

    # process & output
    if apt_number != None:
        address = addressee + "\n" + apt_number + "\n" + street_number + " "
        + street_name + "\n" + city + "\n" + province + "\n" + postal_code
    else:
        address = addressee + "\n" + street_number + " " + street_name + "\n"
        + city + "\n" + province + "\n" + postal_code

    return address


def main():
    # this function is get input

    # input
    addressee = input("Enter your name:")
    question = input("Do you have Apt. Number?(y/n):")
    if question == 'y':
        apt_number = input("Enter your Apt. Number:")
    else:
        apt_number = None
    street_number = input("Enter your Street number:")
    street_name = input("Enter your Street name:")
    city = input("Enter your City:")
    province = input("Enter your Province:")
    postal_code = input("Enter your Postal Code:")

    # call function
    full_address = calculate_address(addressee, apt_number, street_number,
                                     street_name, city, province, postal_code)

    # output
    print(format(full_address))


if __name__ == "__main__":
    main()
