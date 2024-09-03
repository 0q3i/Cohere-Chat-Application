import tkinter as tk
import api_fonc as cohere 
#import tk_fonc as ttk
response = None
message = None
# Function to send a message
def send_message():
    global response
    global message
    message = message_entry.get()
    if message:
        message_history.config(state=tk.NORMAL)
        message_history.insert(tk.END, f"You: {message}\n")
        message_history.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)
        response = cohere.chatLLM(message)
        if response:
            message_history.config(state=tk.NORMAL)
            message_history.insert(tk.END, f"Cohere: {response}\n")
            message_history.config(state=tk.DISABLED)
            message_entry.delete(0, tk.END)


# Create the main window
parent = tk.Tk()
parent.geometry("1200x800")
parent.title("Cohere Chat Application")

# Create a Text widget for message history
message_history = tk.Text(parent, wrap=tk.WORD, width=80, height=40)
message_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
message_history.config(state=tk.DISABLED)

# Create an Entry widget for entering messages
message_entry = tk.Entry(parent, width=30)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(parent, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

cohere.context(response, message)

# Start the Tkinter event loop
parent.mainloop()


