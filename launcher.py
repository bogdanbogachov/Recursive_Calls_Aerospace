from CI import NHA
from CI import isCI
from CI import CI_finder
from CI import program_number
from CI import material_description
from CI import close

#Action choice

print(55*'-')
action = input("""Choose an action:
1 - Find an NHA for a part
2 - Check if a part is a CI
3 - Find a closest higher CI to a part
4 - Get PN info
""")
if action == "1":
    part = input("Enter your Part Number: ")
    print("Looking for NHA(s) for you")
    print(55*"-")
    a = NHA(part)
    if a == []:
        print("No NHA found or value entered is incorrect")
    else:
        for i in a:
            print(i)
    print(55*"-")
elif action == "2":
    part = input("Enter your Part Number (make sure to a enter a correct value\n"
            "with a dash number): ")
    print("Checking if your part is a CI")
    a = isCI(part)
    print(55*"-")
    if a:
        print("Your part is a CI")
    else:
        print("Your part is NOT a CI or value entered is incorrect")
    print(55*"-")
elif action == "3":
    part = input("Enter your Part Number: ")
    print("Looking for a closest higher CI")
    a = CI_finder(part)
    print(55*"-")
    if a is False:
        print("No CI found or value entered is incorrect")
    elif a == []:
        print("You have reached the end of product tree")
    else:
        print("""1 - CI PN\n2 - Name\n3 - Program\n4 - BOM level
        """)
        program_number(a)
    print(55*"-")
elif action == "4":
    part = input("Enter your Part Number: (make sure to a enter a correct value\n"
            "with a dash number): ")
    print("Fetching info for you")
    a = material_description(part)
    print(55*"-")
    if a == []:
        print("No info found or value entered is incorrect")
    else:
        print("""1 - PN\n2 - Name\n3 - Manufacturer
        """)
        for info in a:
            print(info)
    print(55*"-")
else:
    print(55*"-")
    print("Wrong choice")
    print(55*"-")

close() # closing connection to our database