import datetime

# -------------------- Patient Class --------------------
class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def get_details(self):
        return f"{self.patient_id},{self.name},{self.age},{self.gender},{self.disease}"


# -------------------- Billing Class --------------------
class Billing:
    def __init__(self, consultation_fee, medicine_fee, room_charges):
        self.consultation_fee = consultation_fee
        self.medicine_fee = medicine_fee
        self.room_charges = room_charges

    def calculate_total(self):
        return self.consultation_fee + self.medicine_fee + self.room_charges


# -------------------- Hospital Management System --------------------
class HospitalManagementSystem:
    def __init__(self, filename="patient_records.txt"):
        self.filename = filename

    def add_patient(self):
        try:
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")

            patient = Patient(patient_id, name, age, gender, disease)

            consultation_fee = float(input("Enter Consultation Fee: "))
            medicine_fee = float(input("Enter Medicine Fee: "))
            room_charges = float(input("Enter Room Charges: "))

            billing = Billing(consultation_fee, medicine_fee, room_charges)
            total_bill = billing.calculate_total()

            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            record = (
                patient.get_details()
                + f",{consultation_fee},{medicine_fee},{room_charges},{total_bill},{date}\n"
            )

            with open(self.filename, "a") as file:
                file.write(record)

            print("\nPatient record added successfully.")
            print(f"Total Bill Amount: ₹{total_bill}")

        except ValueError:
            print("Invalid input. Please enter numeric values where required.")
        except Exception as e:
            print("An error occurred:", e)

    def view_records(self):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()

            if not records:
                print("No patient records found.")
                return

            print("\n--- Patient Records ---")
            for record in records:
                data = record.strip().split(",")
                print(
                    f"ID: {data[0]} | Name: {data[1]} | Age: {data[2]} | "
                    f"Gender: {data[3]} | Disease: {data[4]} | "
                    f"Total Bill: ₹{data[8]} | Date: {data[9]}"
                )

        except FileNotFoundError:
            print("No records file found.")
        except Exception as e:
            print("An error occurred:", e)

    def run(self):
        while True:
            print("\n--- Hospital Management System ---")
            print("1. Add Patient Record")
            print("2. View Patient Records")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_records()
            elif choice == "3":
                print("Exiting system. Thank you.")
                break
            else:
                print("Invalid choice. Please try again.")


# -------------------- Main Execution --------------------
if __name__ == "__main__":
    system = HospitalManagementSystem()
    system.run()
