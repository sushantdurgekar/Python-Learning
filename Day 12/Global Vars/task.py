# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

def increase_enemies(enemy):
    enemy += 1
    print(f"enemies inside function: {enemy}")
    return enemy

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1


# increase_enemies()
enemies = increase_enemies(enemies)
# enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


