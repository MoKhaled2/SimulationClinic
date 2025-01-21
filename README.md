# Simulation of Clinic Service Process

This Python code simulates a clinic's patient service system. The goal is to track the average waiting time for patients and the number of patients remaining in the queue after a specific period. The clinic processes patients based on a service rate, which is influenced by the patient's age.

## Key Components of the Code:

### 1. **Imports**
   - `random`: Used to simulate patient arrival at the clinic.
   - `Queue`: A custom implementation of a queue data structure to manage the waiting list of patients.
   - `Clinic`: A custom class representing the clinic. This class handles the state of the clinic, including whether it's busy or available to serve a new patient.
   - `Patient`: A custom class representing a patient. It tracks when the patient arrives and calculates the wait time.

### 2. **Function: `simulate(total_hours, service_rate)`**
   This function simulates the clinic operation over a given time period (`total_hours`). It calculates the average waiting time for patients and the number of patients left in the queue.

   - `total_hours`: The number of hours the simulation runs for.
   - `service_rate`: The rate at which patients are served. It is used to determine the time it takes to serve each patient based on their age.

   **Simulation Steps:**
   1. **Generate New Patients**: Every second, there's a chance (1 in 361) that a new patient arrives. If a patient arrives, a new `Patient` object is created with the current second as the arrival time.
   
   2. **Serve the Patient**: If the clinic is not busy and there are patients in the queue, the clinic will start serving the next patient. The `waiting_times` list records the wait time for each patient.
   
   3. **Clinic Tick**: Each second, the `clinic.tick()` method is called to update the clinic's state (i.e., whether it's busy or free).

   4. **Calculate Average Waiting Time**: After the simulation ends, the average waiting time is calculated in minutes. It is determined by the sum of all waiting times divided by the number of patients served.

   5. **Print Results**: The average waiting time and the number of remaining patients in the queue are printed.

### 3. **Main Function**
   The main part of the program runs the simulation for two different service rates:
   - **Service Time = Age / 5**: Patients are served faster.
   - **Service Time = Age / 10**: Patients are served slower.

   It runs the simulation three times for each service rate and prints the results.

### 4. **Assumptions and Randomness**
   - The arrival of new patients follows a random process with a 1 in 361 chance every second.
   - The clinic is either serving a patient or idle, based on the availability of the doctor.
   
### Example Output:
   ```text
   Simulation for Service Time = Age / 5:
   Average Wait: 8.35 minutes | Patients Remaining: 3
   Average Wait: 7.92 minutes | Patients Remaining: 5
   Average Wait: 9.21 minutes | Patients Remaining: 2

   ########################################

   Simulation for Service Time = Age / 10:
   Average Wait: 12.43 minutes | Patients Remaining: 4
   Average Wait: 14.12 minutes | Patients Remaining: 7
   Average Wait: 13.67 minutes | Patients Remaining: 6
