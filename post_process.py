def menu_callback(previous_menu, main_menu):
    while True:
        print("""
What would you like to do next?
   1. 🔙 Previous Menu
   2. 🏠 Home
   3. ↩️  Exit
""")
        choice = input("Enter your choice (1-3):\n")

        if choice == "1":
            previous_menu()
        elif choice == "2":
            main_menu()
        else:
            edm_exit()

def edm_exit():
    print("\n You are exiting EDM. Good bye!!!!")
    exit()

# def our_sum(numbers): ## 1, 2, 4, 6, 7
#     sum = 0
#     # for number in numbers:
#     #     sum += number
#     count = 0
#     while count < len(numbers):
#         sum += numbers[count]
#         count += 1
    # return sum