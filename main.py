import sys


def usageInstruction():
    print(f"Usage : python3 {sys.argv[0]} <vendor>")
    print(f'If you want to see the list of all vendors, please type : python3 {sys.argv[0]} --vendors')


vendors = {
    'APC': ['./credentials/U_APC.txt', './credentials/P_APC.txt'],
    'Brocade': ['./credentials/U_Brocade.txt', './credentials/P_Brocade.txt'],
    'Cisco': ['./credentials/U_Cisco.txt', './credentials/P_Cisco.txt']
}

vendors_lower = []
[vendors_lower.append(vendor.lower()) for vendor in vendors]

try:
    if sys.argv[1] == '--vendors':
        print("Here you have a list of all the vendors : ")
        for vendor in vendors:
            print(f"\t- {vendor}")
    elif sys.argv[1].lower() not in vendors_lower:
        print(f"{sys.argv[1]} is not in the vendors list.")
    else:
        for vendor in vendors:
            if sys.argv[1].lower() == vendor.lower():
                users = []
                passwords = []
                list_number = 1
                for element in vendors[vendor]:
                    with open(element) as file:
                        for line in file:
                            if list_number == 1:
                                if line[-1] == '\n':
                                    users.append(line[:-1])
                                else:
                                    users.append(line)
                            else:
                                if line[-1] == '\n':
                                    passwords.append(line[:-1])
                                else:
                                    passwords.append(line)
                    list_number += 1
                list_number = 1
        for user in users:
            print(f'\n\t\tFor the user {user}\n')
            for password in passwords:
                print(f'\t- {user}:{password}')

except:
    usageInstruction()
