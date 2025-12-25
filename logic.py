import time
import sys
import random

# BOND Protocol: Serious Transparency & Fair Accountability
# Created by Sahil

class BondSystem:
    def __init__(self, app_name, security_grade, risk_level):
        self.app_name = app_name
        self.grade = security_grade  # A, B, C
        self.risk_level = risk_level # High, Medium, Low
        self.stipend_value = self.calculate_stipend(risk_level)
        self.is_authorized = False

    def calculate_stipend(self, risk):
        # Setting clear, simple values for data risk
        mapping = {"High": 150, "Medium": 50, "Low": 10}
        return mapping.get(risk, 5)

    def display_warning(self):
        print(f"\n{'='*45}")
        print(f"       BOND PROTOCOL: SECURITY WARNING")
        print(f"{'='*45}")
        print(f"APPLICATION: {self.app_name}")
        print(f"SECURITY RATING: [{self.grade}]")
        print(f"RISK FACTOR: {self.risk_level.upper()}")
        print(f"\nTRUTH: This app is requesting your Private Health Data.")
        print(f"DANGER: If leaked, your medical history could be exposed.")
        print(f"\nOUR GUARANTEE:")
        print(f"1. A ${self.stipend_value} stipend is LOCKED in Escrow for you.")
        print(f"2. Your data will be AUTO-DELETED in 10 seconds (Simulation).")
        print(f"{'='*45}")

    def start_protocol(self):
        self.display_warning()
        choice = input("Do you accept this danger? (Type 'YES' to proceed): ").strip().upper()

        if choice == "YES":
            self.is_authorized = True
            self.execute_protection_lifecycle()
        else:
            print("\n[BOND REJECTED]: No data was shared. You are safe.")

    def execute_protection_lifecycle(self):
        print(f"\n[BOND ACTIVE]: Funds secured. Data 'Rental' has begun.")
        
        # 1. Simulating the Auto-Delete Timer
        print("\n--- MONITORING DATA LIFECYCLE ---")
        for i in range(10, 0, -1):
            sys.stdout.write(f"\rTime until Auto-Deletion: {i}s remaining...")
            sys.stdout.flush()
            time.sleep(1)
        
        print("\n\n[SUCCESS]: Timer reached zero. Data scrubbed from servers.")
        
        # 2. Simulating the Fairness Audit (Checking for leaks)
        print("\n--- FINAL AUDIT REPORT ---")
        time.sleep(1)
        
        # Simulation: 30% chance of a breach for this demonstration
        breach_detected = random.random() < 0.3 
        
        if breach_detected:
            print(f"!!! ALERT: A verified server breach was detected !!!")
            print(f"BOND TRIGGERED: Since the company failed, ${self.stipend_value} is being")
            print(f"transferred to your account automatically. Status: COMPENSATED.")
        else:
            print("AUDIT COMPLETE: No leaks detected during the rental period.")
            print("Status: SECURE.")

# --- RUNNING THE DEMONSTRATION ---
if __name__ == "__main__":
    # You can change these values to test different scenarios
    my_app = BondSystem("HealthTrack Pro", "A", "High")
    my_app.start_protocol()