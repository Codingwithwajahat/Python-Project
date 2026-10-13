
import sys
import csv
from pathlib import Path

folder = Path("data")
output_folder = Path("output")
file = folder / "customers.csv"

output_folder.mkdir(exist_ok=True)

if not file.exists():
    print("File doesn't exist")
    sys.exit()


def load_customer():
    with open(file, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
        return data


def customer_validation(customer):
    if not customer["id"].strip():
        return "ID cannot be empty"

    if not customer["name"].strip():
        return "Name cannot be empty"

    if "@" not in customer["email"] or "." not in customer["email"]:
        return "Email format incorrect"

    try:
        age = int(customer["age"])
    except ValueError:
        return "Age must be an integer"

    if age <= 0:
        return "Age must be greater than 0"

    return True


read = load_customer()

valid_customer = []
invalid_customer = []

for customer in read:
    result = customer_validation(customer)

    if result == True:
        valid_customer.append(customer)
    else:
        invalid_customer.append({
            "customer": customer,
            "error": result
        })


output = output_folder / "cleaned-customer.csv"
in_output = output_folder / "invalid-customer.csv"


with open(output, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name", "email", "age"]
    )
    writer.writeheader()
    writer.writerows(valid_customer)


with open(in_output, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name", "email", "age", "error"]
    )
    writer.writeheader()

    for item in invalid_customer:
        customer = item["customer"]
        error = item["error"]

        writer.writerow({
            "id": customer["id"],
            "name": customer["name"],
            "email": customer["email"],
            "age": customer["age"],
            "error": error
        })


def summary_report():
    return {
        "Total customer": len(read),
        "Total valid customer": len(valid_customer),
        "Total invalid customer": len(invalid_customer),
        "Cleaned file": str(output),
        "Invalid file": str(in_output)
    }


print(summary_report())
