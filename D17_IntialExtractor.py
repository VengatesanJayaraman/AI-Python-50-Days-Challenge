import tkinter as tk

def extract_initials():
    full_name = entry.get().strip()
    if not full_name:
        result_label.config(text="Please enter a full name.")
        return

    words = full_name.split()
    initials = ''.join([word[0].upper() for word in words if word])
    result_label.config(text=f"Initials: {initials}")

# Setup GUI window
root = tk.Tk()
root.title("🆔 Initials Extractor")
root.geometry("400x200")

# Widgets
tk.Label(root, text="Enter Full Name:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Extract Initials", command=extract_initials, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the app
root.mainloop()
