# week5_lab.py
# Author: Rahim Rozani
# Business Domain: Wristwatches

product_name = "Seiko"
status = "pending"
quantity = 3
unit_price = 450.00
is_over_limit = unit_price * quantity > 1000.00

print(
    type(product_name),
    type(status),
    type(quantity),
    type(unit_price),
    type(is_over_limit),
)

subtotal = quantity * unit_price
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000.00

print("=== Purchase Request Summary ===")
print(f"Product Name: {product_name}")
print(f"Qty: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Requires Approval: {requires_approval}")

# User Input

user_qty = int(input("Enter a new quantity: "))
new_total = unit_price * user_qty * 1.07
print("=== New Purchase Request Summary ===")
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires Approval: {new_total > 1000}")
