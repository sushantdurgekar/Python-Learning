enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# ## Local Scope

def drink_potion1():
    potion_strength=2
    print(potion_strength)

drink_potion1()
# ## print(potion_strength)

# ## Global Scope
player_health=10

def game():
    def drink_potion2():
        potion_strength=2
        print(player_health)

    drink_potion2()

game()
print(player_health)











