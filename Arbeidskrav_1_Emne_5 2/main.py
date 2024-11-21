import tkinter as tk
from tkinter import ttk
from Arbeidskrav_1_Emne_5.Phonebook import Phonebook

def main():
    # Initialize Phonebook
    phonebook = Phonebook()

    # Import contacts
    phonebook.import_contacts_from_jsonl_file("People.jsonl")

    # Set up tkinter window
    root = tk.Tk()
    root.title("Phonebook Application")

    # Frame for search and sort
    control_frame = tk.Frame(root)
    control_frame.pack(pady=10, padx=10, fill=tk.X, expand=True)

    # Search functionality
    search_entry = tk.Entry(control_frame, width=10)
    search_entry.pack(side=tk.LEFT, padx=5)
    search_btn = tk.Button(control_frame, text="Search", command=lambda: search_contact(phonebook, search_entry, tree))
    search_btn.pack(side=tk.LEFT, padx=5)

    # Sort functionality
    tk.Label(control_frame, text="Sort by:").pack(side=tk.LEFT, padx=5)
    sort_by_var = tk.StringVar(value="firstname")
    sort_by_options = ["firstname", "lastname", "phone", "birthday", "street", "city"]
    sort_menu = ttk.Combobox(control_frame, textvariable=sort_by_var, values=sort_by_options, width=10)  # Adjusted width
    sort_menu.pack(side=tk.LEFT, padx=5)

    tk.Label(control_frame, text="Order:").pack(side=tk.LEFT, padx=5)
    order_var = tk.StringVar(value="asc")
    order_options = ["asc", "desc"]
    order_menu = ttk.Combobox(control_frame, textvariable=order_var, values=order_options, width=5)  # Adjusted width
    order_menu.pack(side=tk.LEFT, padx=5)

    sort_btn = tk.Button(control_frame, text="Sort", command=lambda: sort_contacts(phonebook, sort_by_var.get(), order_var.get(), tree))
    sort_btn.pack(side=tk.LEFT, padx=5)

    # Treeview widget
    tree = ttk.Treeview(root, columns=("First Name", "Last Name", "Phone", "Birthday", "Street", "City"), show='headings', height=30)
    tree.heading("First Name", text="First Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Phone", text="Phone")
    tree.heading("Birthday", text="Birthday")
    tree.heading("Street", text="Street")
    tree.heading("City", text="City")

    # Set column widths
    tree.column("First Name", width=120)
    tree.column("Last Name", width=120)
    tree.column("Phone", width=100)
    tree.column("Birthday", width=100)
    tree.column("Street", width=150)
    tree.column("City", width=100)

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Functions for tkinter
    def update_treeview():
        tree.delete(*tree.get_children())
        contacts = phonebook.get_all_contacts()
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

    def search_contact(_phonebook, _search_entry, _tree):
        search_term = search_entry.get().lower()
        results = phonebook.search_contact(search_term)
        tree.delete(*tree.get_children())
        for result in results:
            tree.insert('', tk.END, values=result)

    def sort_contacts(_phonebook, sort_by, order, _tree):
        valid_sort = phonebook.sort_contacts(sort_by, order)
        if valid_sort:
            update_treeview()

    # Display initial contacts
    update_treeview()

    root.mainloop()

if __name__ == '__main__':
    main()
