cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(cookbook)

create("brownies")
create("beans")
create("potato")

def read(index):
    item = cookbook[index]
    print(item)

read(2)

def update(index , recipe):
    cookbook[index] = recipe
    print(cookbook)

update(0, "bear")

def destroy(index):
    if index in range(len(cookbook)):
        recipe = cookbook.pop(index)
        print(f"{recipe}has been removed")
    else:
        print("out of range, not available")

def list_all_recipes ():
    if cookbook:
        print("all recipes in cookbook")
        for index, recipe in enumerate(cookbook):
            print(f"{index}: {recipe}")

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
