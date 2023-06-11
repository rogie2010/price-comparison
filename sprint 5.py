import tkinter as tk
from tkinter import messagebox


def compare_prices_weights():
    items = []

    for i in range(len(entry_prices)):
        price = float(entry_prices[i].get())
        weight = float(entry_weights[i].get())
        quantity = float(entry_quantities[i].get())
        name = entry_names[i].get()
        items.append((price, weight, quantity, name))

    budget = float(entry_budget.get())

    best_item = None
    best_price_per_weight = float('inf')

    for item in items:
        price, weight, quantity, name = item
        price_per_weight = price / weight
        if price_per_weight < best_price_per_weight:
            best_price_per_weight = price_per_weight
            best_item = item

    if best_item is None:
        messagebox.showinfo("Price & Weight Comparison", "No items found.")
    else:
        best_price, best_weight, best_quantity, best_name = best_item
        total_price = best_price * best_quantity
        if total_price <= budget:
            remaining_budget = budget - total_price
            messagebox.showinfo("Price & Weight Comparison",
                                f"The best item '{best_name}' costs ${total_price:.2f}, fits within your budget, and has the best price per unit weight.\nYou have ${remaining_budget:.2f} left.")
        else:
            messagebox.showinfo("Price & Weight Comparison",
                                "The best item has the best price per unit weight, but exceeds your budget.")

        # Display the details of the best item in a new window
        best_item_window = tk.Toplevel(window)
        best_item_window.title("Best Item Details")

        label_best_name = tk.Label(best_item_window, text=f"Name: {best_name}")
        label_best_name.pack()

        label_best_price = tk.Label(best_item_window, text=f"Price: ${best_price:.2f}")
        label_best_price.pack()

        label_best_weight = tk.Label(best_item_window, text=f"Weight: {best_weight} units")
        label_best_weight.pack()

        label_best_quantity = tk.Label(best_item_window, text=f"Quantity: {best_quantity}")
        label_best_quantity.pack()

        label_total_price = tk.Label(best_item_window, text=f"Total Price: ${total_price:.2f}")
        label_total_price.pack()


def add_item():
    # Create a frame to contain the item details
    item_frame = tk.Frame(window)
    item_frame.pack()

    # Create labels and entry fields for a new item
    label_name = tk.Label(item_frame, text="Name:")
    label_name.pack(side=tk.LEFT)

    entry_name = tk.Entry(item_frame)
    entry_name.pack(side=tk.LEFT)

    label_price = tk.Label(item_frame, text="Price:")
    label_price.pack(side=tk.LEFT)

    entry_price = tk.Entry(item_frame)
    entry_price.pack(side=tk.LEFT)

    label_weight = tk.Label(item_frame, text="Weight:")
    label_weight.pack(side=tk.LEFT)

    entry_weight = tk.Entry(item_frame)
    entry_weight.pack(side=tk.LEFT)

    label_quantity = tk.Label(item_frame, text="Quantity:")
    label_quantity.pack(side=tk.LEFT)

    entry_quantity = tk.Entry(item_frame)
    entry_quantity.pack(side=tk.LEFT)

    # Append the entry fields and the item frame to the respective lists
    entry_names.append(entry_name)
    entry_prices.append(entry_price)
    entry_weights.append(entry_weight)
    entry_quantities.append(entry_quantity)
    item_frames.append(item_frame)

    # Create a remove button for the item
    remove_button = tk.Button(item_frame, text="Remove", command=lambda: remove_item(item_frame))
    remove_button.pack(side=tk.LEFT)


def remove_item(item_frame):
    # Remove the item frame and its corresponding entry fields from the window
    item_frame.destroy()

    index = item_frames.index(item_frame)

    entry_names[index].destroy()
    entry_prices[index].destroy()
    entry_weights[index].destroy()
    entry_quantities[index].destroy()

    entry_names.pop(index)
    entry_prices.pop(index)
    entry_weights.pop(index)
    entry_quantities.pop(index)



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

# Create a frame to contain the item frames
items_frame = tk.Frame(window)
items_frame.pack()

# Create a button to remove items
remove_button = tk.Button(window, text="Remove Item",
                          command=lambda: remove_item(item_frames[-1]) if item_frames else None)
remove_button.pack()

# Create a button to compare prices and weights
compare_button = tk.Button(window, text="Compare", command=compare_prices_weights)
compare_button.pack()


# Create lists to store entry fields for names, prices, weights, and quantities
entry_names = []
entry_prices = []
entry_weights = []
entry_quantities = []
item_frames = []

# Run the main loop
window.mainloop()