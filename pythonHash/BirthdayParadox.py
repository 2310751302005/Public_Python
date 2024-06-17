import random
'''
The problem described is essentially the Birthday Paradox, which states that in a group of 23 people, 
there's a better than even chance that two people share the same birthday. For groups of 30 or more, 
this probability is even higher.
To predict whether in a room with over 30 people there are at least two people sharing 
the same birth date (ignoring the year), you can use probability theory and simulation.
Here’s a Python algorithm to simulate this scenario:
'''
def has_shared_birthday(people_count, simulations=10000):
    # Number of simulations where at least two people share the same birthday
    shared_birthday_count = 0

    for _ in range(simulations):
        birthdays = [random.randint(1, 365) for _ in range(people_count)]
        if len(birthdays) != len(set(birthdays)):
            shared_birthday_count += 1

    # Probability of having at least two people sharing a birthday
    probability = shared_birthday_count / simulations
    return probability

people_count = 31  # You can set this to any number greater than 30
probability = has_shared_birthday(people_count)
print(f"The probability of having at least two people with the same birthday in a room of {people_count} people is {probability:.2f}")

'''Explanation:

    1.Function Definition: has_shared_birthday(people_count, simulations=10000) defines a function that calculates 
      the probability of having at least two people with the same birthday in a group of people_count people, 
      using simulations number of simulations.
    2.Simulation Loop: We run simulations (default 10,000) simulations. For each simulation:
        Generate a list of random integers (representing days of the year) between 1 and 365, one for each person in the group.
        Check if there are any duplicates in the list (i.e., if any two people share the same birthday).
    3.Counting Shared Birthdays: If there are duplicates, increment the count of simulations with shared birthdays.
    4.Probability Calculation: After all simulations, calculate the probability by dividing the count of shared birthdays 
      by the total number of simulations.

You can adjust people_count to any number greater than 30 to see how the probability changes with different group sizes.
This simulation-based approach provides an empirical probability, which can be very close 
to the theoretical probability, especially with a large number of simulations.'''