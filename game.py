import random

def get_choices():
    player_choices = input("Enter a choice (rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)