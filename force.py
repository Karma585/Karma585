print("Newtons second law of motion")
print("----------------------------------------")
 # Determine the missing value
print("Select the missing value")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (f)")
missing_value_choice = input("Enter the option number")

if missing_value_choice =="1":
    a = float(input("Enter acceleration (a): "))
    f = float(input("Enter the force(f): "))
    m = f / a
    print(f"mass (m) = {m}")

elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    f = float(input("Enter the force (f): "))
    a = f / m
    print(f"acceleration (a) = {a}")

elif missing_value_choice == "3":
    m = float(input("Enter mass (m:)"))
    a = float(input("Enter acceleration (a);"))
    f = m * a
    print(f"forcr (f) = {f}")

else:
    print("Invalid option selected")
