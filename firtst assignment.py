print("Determine whether you are eligible for a discount on movie ticket")
Is_student = input("Are you student? Yes/No:")
age = int(input("Enter your age: "))
if age <= 12:
    print("You are elligible for a discount on movie ticket")
elif 13 <= age <= 18 and Is_student == "yes":
    print("You are elligible for a discount on movie ticket")
else:
    print("You are not offered an discount for movie ticket")