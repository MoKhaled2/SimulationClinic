import random #inserting the library to use "randrange"

class Patient:
    def __init__(self, arrival_time):
        self.age = random.randrange(20, 61)
        self.arrival_time = arrival_time

    def get_age(self):
        return self.age

    def wait_time(self, current_time):
        """
        Compute the amount of time the patient
        waited in the queue before entering
        """
        return current_time - self.arrival_time
