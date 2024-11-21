try:
    filename = 'file1.txt'
    file = open(filename, "x")
    print(filename + " successfully created.")
except:
    print(filename + " already exists.")

print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Count Records")
print("E - Exit")

choice = ""

while choice.upper() != 'D':
    choice = input("ENTER SELECTION [A, B, C, D or E]: ")
    if choice.upper() == 'A':
        print("Add Record")
        addRec()
    elif choice.upper() == 'B':
        print("View Records")
        viewRec()
    elif choice.upper() == 'C':
        print("Clear All Records")
        clearRec()
    elif choice.upper() == 'D':
        print("Count All Records")
         countRec()
    elif choice.upper() == 'E':
        print("Thank you!")