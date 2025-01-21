class Clinic:
    def __init__(self, service_rate):
        self.service_rate = service_rate
        self.current_patient = None
        self.remaining_time = 0

    def is_busy(self):
        return self.current_patient is not None

    def start_service(self, patient):
        """
        Simulate the entering
        of the patients to the doctor
        """
        self.current_patient = patient
        self.remaining_time = ( patient.get_age() / self.service_rate ) * 60

    def tick(self):
        """
        Simulate the clock in the clinic
        one call for this methode means that 1 second has passed
        """
        if self.current_patient:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                self.current_patient = None
