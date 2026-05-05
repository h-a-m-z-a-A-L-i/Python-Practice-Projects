from tkinter import *
import requests

def get_quote():
    # Show loading state immediately
    canvas.itemconfig(quote_text, text="Thinking...", font=("Arial", 20, "italic"))
    window.update_idletasks()
    
    try:
        response = requests.get(url='https://api.kanye.rest')
        response.raise_for_status()
        data = response.json()
        quote = data['quote']
        
        # Adjust font size based on quote length
        if len(quote) > 100:
            canvas.itemconfig(quote_text, text=quote, font=("Arial", 18, "bold"))
        elif len(quote) > 50:
            canvas.itemconfig(quote_text, text=quote, font=("Arial", 22, "bold"))
        else:
            canvas.itemconfig(quote_text, text=quote, font=("Arial", 26, "bold"))
            
    except Exception:
        canvas.itemconfig(quote_text, text="Kanye is offline. Check your connection.", font=("Arial", 15, "bold"))

# UI Setup
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, 
    text="Fetching wisdom...", 
    width=250, 
    font=("Arial", 25, "bold"), 
    fill="white",
    justify="center"
)
canvas.grid(row=0, column=0)

# Button Setup
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(
    image=kanye_img, 
    highlightthickness=0, 
    command=get_quote, 
    bg="white", 
    activebackground="#f0f0f0",
    relief="flat",
    cursor="hand2"
)
kanye_button.grid(row=1, column=0, pady=20)

# Initial quote
get_quote()

window.mainloop()