import tkinter as tk
from tkinter import messagebox

# Dummy social media data
social_media_accounts = {
    "Facebook": ["https://www.facebook.com/"],
    "Twitter": ["https://twitter.com/"],
    "Instagram": ["https://www.instagram.com/"],
    "LinkedIn": ["https://www.linkedin.com/"],
    "Pinterest": ["https://www.pinterest.com/"]
}

def recommend():
    selected_platform = platform_var.get()
    if selected_platform:
        if selected_platform in social_media_accounts:
            url = social_media_accounts[selected_platform][0]
            messagebox.showinfo("Recommendation", f"We recommend {selected_platform}. You can visit {url}")
        else:
            messagebox.showerror("Error", "Selected platform not found in our database.")
    else:
        messagebox.showerror("Error", "Please select a platform.")

# UI setup
root = tk.Tk()
root.title("Social Media Recommendation")

platform_var = tk.StringVar(root)
platform_var.set("Facebook")  # Default selection

platform_label = tk.Label(root, text="Select a Social Media Platform:")
platform_label.pack()

platform_optionmenu = tk.OptionMenu(root, platform_var, *social_media_accounts.keys())
platform_optionmenu.pack()

recommend_button = tk.Button(root, text="Recommend", command=recommend)
recommend_button.pack()

root.mainloop()
