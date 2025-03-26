import random

# Base class for the random number generator
class RandomNumberGenerator:
    def __init__(self, lower_bound=0, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.random_number = self.generate_random_number()
    
    def generate_random_number(self):
        return random.randint(self.lower_bound, self.upper_bound)
    
    def get_random_number(self):
        return self.random_number

# Derived class for comparing user input
class NumberComparer(RandomNumberGenerator):
    def __init__(self, lower_bound=0, upper_bound=100):
        super().__init__(lower_bound, upper_bound)
    
    def get_user_input(self):
        try:
            user_input = int(input(f"Enter a number between {self.lower_bound} and {self.upper_bound}: "))
            if not self.lower_bound <= user_input <= self.upper_bound:
                raise ValueError("Number is out of bounds.")
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None
    
    def compare_numbers(self):
        user_input = self.get_user_input()
        if user_input is not None:
            if user_input < self.random_number:
                print("Your number is lower than the random number.")
            elif user_input > self.random_number:
                print("Your number is higher than the random number.")
            else:
                print("Congratulations! You guessed the number.")
            return
# Example usage
if __name__ == "__main__":
    comparer = NumberComparer()
    comparer.compare_numbers()
