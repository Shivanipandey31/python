import random
# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
        {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }]
def correct_guess(guess,a_followers,b_followers):
    if (a_followers>b_followers):
        return guess=="a"
    else:
        return guess=="b" 

def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return(f"{account_name},a{account_descr} from {account_country}")

def random_account():
    return random.choice(data)
def game():
    score=0
    continue_game=True
    account_a=random_account()
    account_b=random_account()
    while (continue_game==True):
        while (account_a==account_b):
            account_b=random_account()
        print(f"compare A: {format_data(account_a)}")
        print("vs")
        print(f"compare B: {format_data(account_b)}")

        guess =input("Who has more followers A or B")
        a_followers=account_a["follower_count"]
        b_followers=account_b["follower_count"]
        is_correct=correct_guess(guess,a_followers,b_followers)
        if (is_correct):
            score=score+1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game=False
            print(f"Sorry, that's wrong. Final score: {score}")
        account_a=account_b
        account_b=random_account()

game()
            


    