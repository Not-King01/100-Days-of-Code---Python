import art, random, game_data

random_a = random.randint(0, len(game_data.data) - 1)
random_b = random.randint(0, len(game_data.data) - 1)
score = 0

# Ensure random_b is different from random_a
while random_b == random_a:
    random_b = random.randint(0, len(game_data.data) - 1)


def compare(A_or_B, followers_a, followers_b):
    """Compares the follower counts and checks if the user's choice is correct."""
    if followers_a > followers_b:
        return A_or_B == 'A'
    else:
        return A_or_B == 'B'


def user_input():
    global random_a, random_b, score
    c = data(random_a, random_b)
    print(art.logo)
    print(f"Compare A: {c[0]}, {c[4]}, from {c[6]}")  # Name, description, country
    print(art.vs)
    print(f"Against B: {c[1]}, {c[5]}, from {c[7]}")  # Name, description, country
    value = input("Who has more followers? Type 'A' or 'B': ").upper()

    ans = compare(value, c[2], c[3])  # Compare follower counts
    if ans:
        score += 1
        print(f"You're right! Current Score: {score}.")
        # Update random_a to the correct choice and generate new random_b
        random_a = random_a if value == 'A' else random_b
        random_b = random.randint(0, len(game_data.data) - 1)
        while random_b == random_a:
            random_b = random.randint(0, len(game_data.data) - 1)
        user_input()
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        score = 0


def data(a, b):
    """Returns data for the two compared individuals."""
    name_a = game_data.data[a]["name"]
    name_b = game_data.data[b]["name"]
    followers_a = game_data.data[a]["follower_count"]
    followers_b = game_data.data[b]["follower_count"]
    description_a = game_data.data[a]["description"]
    description_b = game_data.data[b]["description"]
    country_a = game_data.data[a]["country"]
    country_b = game_data.data[b]["country"]
    return [name_a, name_b, followers_a, followers_b, description_a, description_b, country_a, country_b]


# Start the game
user_input()
