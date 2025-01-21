import random
from Queue import *
from Clinic import *
from Patient import *


def simulate(total_hours, service_rate):
    total_seconds = total_hours * 60 * 60
    clinic = Clinic(service_rate)
    patient_queue = Queue()
    waiting_times = []

    for current_second in range(total_seconds):
        # Check if a new patient arrives (1 in 361 chance per seconds)
        if random.randrange(1,361) == 77:
            new_patient = Patient(current_second)
            patient_queue.enqueue(new_patient)

        # Check if the patient can see the doctor or not
        if not clinic.is_busy() and not patient_queue.is_empty():
            next_patient = patient_queue.dequeue()
            clinic.start_service(next_patient)
            waiting_times.append(next_patient.wait_time(current_second))

        clinic.tick()

    # Calculate average waiting time
    average_wait = sum(waiting_times) / len(waiting_times) / 60 if waiting_times else 0
    print(f"Average Wait: {average_wait:.2f} minutes | Patients Remaining: {patient_queue.size()}")


if __name__ == "__main__":
    print("Simulation for Service Time = Age / 5:")
    for _ in range(3):
        simulate(4, 5)

    print("\n" + "#" * 40 + "\n")

    print("Simulation for Service Time = Age / 10:")
    for _ in range(3):
        simulate(4, 10)
