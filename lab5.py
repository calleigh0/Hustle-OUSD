#Lab 5 Calleigh Tanaka

#Task 1: Cat Greeting Function

def cat_greeting(word):
    print(f'cat says {word}')
    print(f'other cat says he wants to fight')
    print(f'bystander cat says fight! fight! fight!')
    print(f'leader cat says ENOUGH')
    print(f'cats all say meow')

cat_greeting('meow')

#Task 2: Superhero Power Function

def generate_superhero_power():
    name = "Calleigh"
    power = "telekenisis"
    print(f"{name}'s power is {power}")

generate_superhero_power()

#Task 3: Superhero Power Funtion with Return 

def generate_superhero_power1():
    power = "Telekenisis"
    return power

print(generate_superhero_power1())
    
#Task 4: Superhero Power Function with Arguments

def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!!"
    return message

print(generate_superhero_power2("calleigh", "telekenisis"))
print(generate_superhero_power2("jannifer", "teleportation"))
print(generate_superhero_power2("alicia", "invisibility"))
print(generate_superhero_power2("manica", "super human strength"))

#Task 5: Looping through Greetings

def cat_greetings_loop(greeting):
    for i in range(5):
        print(f'the cat says {greeting}')

cat_greetings_loop("meow")

#Task 6: Superhero Power Function with Multiple Powers

def generate_multiple_powers(powers):
    for i in (powers):
        print(i)

powers = ["telekenisis", "teleportation", "invisibility", "super strength", "immortality"]

generate_multiple_powers(powers)