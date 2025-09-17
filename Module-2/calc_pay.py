"""
Module 2 — Debugging Exercise
Author: Damitrious Rivera
File: calc_pay.py

"""

def compute_pay(hours: float, rate: float) -> float:
    """Return total pay with time-and-a-half for overtime hours over 40."""
    
    if hours < 0 or rate < 0:
        raise ValueError("Hours and rate must be non-negative.")
    overtime_hours = 0.0
    regular_hours = hours
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40

    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * rate * 1.5
    total = regular_pay + overtime_pay
    return total

def main():
    print("=== Module 2 Debugging Exercise ===")
   
    try:
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly rate: "))
        total = compute_pay(hours, rate)
        print(f"Total pay: ${total:.2f}")
    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()
