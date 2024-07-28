import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json
class Json:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Placeholder Fetcher")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Enter ID:").grid(row=0, column=0, padx=10, pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        fetch_button = tk.Button(self.root, text="Fetch", command=self.fetch_data)
        fetch_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.text_area = tk.Text(self.root, width=80, height=20)
        self.text_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
  
        save_button = tk.Button(self.root, text="Save", command=self.save_data)
        save_button.grid(row=2, column=0, columnspan=3, pady=10)
    
    def fetch_data(self):
        idd = self.entry.get()
        if not idd.isdigit():
            messagebox.showerror("Invalid ID", "enterID.")
            return
        url = f'https://jsonplaceholder.typicode.com/posts/{idd}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, json.dumps(data, indent=4))
        else:
            messagebox.showerror("Error",response.status_code)
            
    def save_data(self):
        data = self.text_area.get('1.0', tk.END).strip()
        if not data:
            messagebox.showwarning("No Data")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(data)
            messagebox.showinfo("Success", f"Data saved {file_path}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Json(root)
    root.mainloop()
