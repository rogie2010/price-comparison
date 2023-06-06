import tkinter as tk
from tkinter import messagebox


def compare_prices_weights():
    items = []

    for i in range(len(entry_prices)):
        price = float(entry_prices[i].get())
        weight = float(entry_weights[i].get())
        quantity = float(entry_quantities[i].get())
        items.append((price, weight, quantity))

    budget = float(entry_budget.get())

    best_item = None
    best_price_per_weight = float('inf')

    for item in items:
        price, weight, quantity = item
        price_per_weight = price / weight
        if price_per_weight < best_price_per_weight:
            best_price_per_weight = price_per_weight
            best_item = item

    if best_item is None:
        messagebox.showinfo("Price & Weight Comparison", "No items found.")
    else:
        best_price, best_weight, best_quantity = best_item
        total_price = best_price * best_quantity
        if total_price <= budget:
            remaining_budget = budget - total_price
            messagebox.showinfo("Price & Weight Comparison",
                                f"The best item costs ${total_price:.2f}, fits within your budget, and has the best price per unit weight.\nYou have ${remaining_budget:.2f} left.")
        else:
            messagebox.showinfo("Price & Weight Comparison",
                                "The best item has the best price per unit weight, but exceeds your budget.")


def add_item():
    # Create labels and entry fields for a new item
    label_price = tk.Label(window, text="Price:")
    label_price.pack()

    entry_price = tk.Entry(window)
    entry_price.pack()

    label_weight = tk.Label(window, text="Weight:")
    label_weight.pack()

    entry_weight = tk.Entry(window)
    entry_weight.pack()

    label_quantity = tk.Label(window, text="Quantity:")
    label_quantity.pack()

    entry_quantity = tk.Entry(window)
    entry_quantity.pack()

    # Append the entry fields to the respective lists
    entry_prices.append(entry_price)
    entry_weights.append(entry_weight)
    entry_quantities.append(entry_quantity)


# Create the main window
window = tk.Tk()
window.title("Price & Weight Comparison")

# Create labels for budget
label_budget = tk.Label(window, text="Budget:")
label_budget.pack()

# Create entry field for budget
entry_budget = tk.Entry(window)
entry_budget.pack()

# Create a button to add items
add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.pack()

# Create a button to compare prices and weights
compare_button = tk.Button(window, text="Compare", command=compare_prices_weights)
compare_button.pack()

# Create lists to store entry fields for prices, weights, and quantities
entry_prices = []
entry_weights = []
entry_quantities = []

# Run the main loop
window.mainloop()
