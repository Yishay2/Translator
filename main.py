from deep_translator import GoogleTranslator
import tkinter as tk

root = tk.Tk()
root.title("Translator")
root.geometry("750x600")
root.maxsize(height=600, width=750)
languages = GoogleTranslator().get_supported_languages(as_dict=True)

label = tk.Label(root, text="Translator", font=("Arial", 28))
label.pack()
clicked = tk.StringVar()
clicked.set("auto")
clicked2 = tk.StringVar()
clicked2.set("english")

options = ["auto"] + list(languages.keys())
drop1 = tk.OptionMenu(root, clicked, *options)
drop1.place(x=480, y=80)

drop2 = tk.OptionMenu(root, clicked2, *options)
drop2.place(x=150, y=80)

textbox1 = tk.Text(root, height=10, width=45)
textbox1.place(x=10, y=120)
textbox2 = tk.Text(root, height=10, width=44)
textbox2.place(x=385, y=120)

Debounce_delay = 300


def translate_text(event=None):
    text1 = textbox2.get("1.0", tk.END).strip()
    target_lang = languages[clicked2.get()]
    source_lang = languages[clicked.get()] if clicked.get() != "auto" else "auto"
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text=text1)
    textbox1.delete("1.0", tk.END)
    textbox1.insert("1.0", translated)


def on_key_release(event):
    global timer
    if timer is not None:
        root.after_cancel(timer)
    timer = root.after(Debounce_delay, translate_text)


timer = None
textbox2.bind("<KeyRelease>", on_key_release)
tk.mainloop()
