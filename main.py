import sys


def usageInstruction():
    print(f"Usage : python3 {sys.argv[0]} <vendor>")
    print(f'If you want to see the list of all vendors, please type : python3 {sys.argv[0]} --vendors')
    print(f'You can type : [ python3 {sys.argv[0]} ALL ] to run the program with all vendors')

def appendCredentials(vendor):
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


def printResult():
    for user in users:
        print(f'\n\t\tFor the user {user}\n')
        for password in passwords:
            print(f'\t- {user}:{password}')

vendors = {
    'APC': ['./credentials/U_APC.txt', './credentials/P_APC.txt'],
    'Brocade': ['./credentials/U_Brocade.txt', './credentials/P_Brocade.txt'],
    'Cisco': ['./credentials/U_Cisco.txt', './credentials/P_Cisco.txt'],
    'Citrix': ['./credentials/U_Citrix.txt', './credentials/P_Citrix.txt'],
    'D-Link': ['./credentials/U_D-Link.txt', './credentials/P_D-Link.txt'],
    'Dell': ['./credentials/U_Dell.txt', './credentials/P_Dell.txt'],
    'EMC': ['./credentials/U_EMC.txt', './credentials/P_EMC.txt'],
    'HP': ['./credentials/U_HP.txt', './credentials/P_HP.txt'],
    'Huawei': ['./credentials/U_Huawei.txt', './credentials/P_Huawei.txt'],
    'IBM': ['./credentials/U_IBM.txt', './credentials/P_IBM.txt'],
    'Juniper': ['./credentials/U_Juniper.txt', './credentials/P_Juniper.txt'],
    'NetApp': ['./credentials/U_NetApp.txt', './credentials/P_NetApp.txt'],
    'Oracle': ['./credentials/U_Oracle.txt', './credentials/P_Oracle.txt'],
    'VMware': ['./credentials/U_VMware.txt', './credentials/P_VMware.txt'],
    '3Com': ['./credentials/U_3Com.txt', './credentials/P_3Com.txt']
}

vendors_lower = []
[vendors_lower.append(vendor.lower()) for vendor in vendors]

users = []
passwords = []

try:
    if sys.argv[1] == '--vendors':
        print("Here you have a list of all the vendors : ")
        for vendor in vendors:
            print(f"\t- {vendor}")
    elif sys.argv[1].lower() == 'all':
        for vendor in vendors:
            print(f'\t\t\tFor the vendor {vendor}')
            appendCredentials(vendor)
            printResult()
    elif sys.argv[1].lower() not in vendors_lower:
        print(f"{sys.argv[1]} is not in the vendors list.")
    else:
        for vendor in vendors:
            if sys.argv[1].lower() == vendor.lower():
                appendCredentials(vendor)
        printResult()
        print()

except:
    usageInstruction()