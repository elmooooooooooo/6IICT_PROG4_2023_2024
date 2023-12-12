import tkinter as tk

app = tk.Tk()
app.title("Klikker-spel")

count = 0  # Initialize the count variable

def update_counter():
    global count
    count += 1
    invoer.set(str(count))  # Update the Entry widget with the new count

veld = tk.Entry(master=app, background="white", width=100)
veld.grid(row=0, column=0)

# Display the initial count in the Entry widget
invoer = tk.StringVar()
invoer.set(str(count))
veld["textvariable"] = invoer

knop1 = tk.Button(master=app, text="klik", command=update_counter)
knop1.grid(column=0, row=1)

app.mainloop()
