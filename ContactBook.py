import tkinter as tk
from tkinter import simpledialog, messagebox

Contacts = {}

def add_contact(Storename, Phone, Email, Address):
    Contacts[Storename] = {'Phone': Phone, 'Email': Email, 'Address': Address}
    messagebox.showinfo("Success", f"Contact {Storename} added successfully")

def view_contact():
    if Contacts:
        contact_list = "\n".join([f"Storename: {storename}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\nAddress: {contact_info['Address']}\n" for storename, contact_info in Contacts.items()])
        messagebox.showinfo("Contact List", contact_list)
    else:
        messagebox.showinfo("Empty", "The Contact book is empty.")

def search_contact(storename):
    if storename in Contacts:
        contact_info = Contacts[storename]
        messagebox.showinfo("Contact Details", f"Storename: {storename}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\nAddress: {contact_info['Address']}")
    else:
        messagebox.showinfo("Not Found", f"Contact {storename} not found")

def update_contact(storename):
    if storename in Contacts:
        new_storename = simpledialog.askstring("Input", "Enter new name:")
        Contacts[new_storename] = Contacts.pop(storename)
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showinfo("Not Found", f"Contact {storename} not found.")

def delete_contact(storename):
    if storename in Contacts:
        del Contacts[storename]
        messagebox.showinfo("Success", f"Contact {storename} deleted successfully.")
    else:
        messagebox.showinfo("Not Found", f"Contact {storename} not found.")

def handle_choice(choice):
    if choice == '1':
        add_contact_window = tk.Toplevel(root)
        add_contact_window.title("Add Contact")

        storename_label = tk.Label(add_contact_window, text="Storename:")
        storename_label.pack()
        storename_entry = tk.Entry(add_contact_window)
        storename_entry.pack()

        phone_label = tk.Label(add_contact_window, text="Phone:")
        phone_label.pack()
        phone_entry = tk.Entry(add_contact_window)
        phone_entry.pack()

        email_label = tk.Label(add_contact_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(add_contact_window)
        email_entry.pack()

        address_label = tk.Label(add_contact_window, text="Address:")
        address_label.pack()
        address_entry = tk.Entry(add_contact_window)
        address_entry.pack()

        add_button = tk.Button(add_contact_window, text="Add Contact", command=lambda: add_contact(storename_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
        add_button.pack()

    elif choice == '2':
        view_contact()

    elif choice == '3':
        storename = simpledialog.askstring("Input", "Enter name to search:")
        search_contact(storename)

    elif choice == '4':
        storename = simpledialog.askstring("Input", "Enter name to update:")
        update_contact(storename)

    elif choice == '5':
        storename = simpledialog.askstring("Input", "Enter name to delete:")
        delete_contact(storename)

    else:
        messagebox.showinfo("Invalid Choice", "Please choose a valid option.")

root = tk.Tk()
root.title("Contact Book")

choice_label = tk.Label(root, text="Select an option:")
choice_label.pack()

choices = ['Add Contact', 'View Contact', 'Search Contact', 'Update Contact', 'Delete Contact']
for idx, choice in enumerate(choices, start=1):
    choice_button = tk.Button(root, text=choice, command=lambda c=str(idx): handle_choice(c))
    choice_button.pack()

root.mainloop()
