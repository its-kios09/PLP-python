# Random Joke Generator 🤣
# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡

import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the JavaScript developer sad? Because he didn’t ‘null’ his feelings.",
    "How many programmers does it take to change a light bulb? None. That's a hardware problem!",
    "Why do Python programmers wear glasses? Because they can't C!",
    "What is a programmer's favorite place to hang out? The Foo Bar!",
    "Why did the Python programmer break up with the Java programmer? Because they had too many arguments!",
    "Why do Java developers wear glasses? Because they don’t see sharp!",
    "What do you call a group of 8 bits? A byte of laughter!",
    "What’s a programmer’s favorite kind of music? Algo-rhythms!",
    "Why do programmers hate nature? Too many bugs!"
]

# Select a random joke
random_joke = random.choice(jokes)

# Display the joke
print("🤣 Random Programming Joke 🤣")
print(random_joke)