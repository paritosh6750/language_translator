from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

# Initialize the main window
window = Tk()
window.title("Language Translator Using Google APIs")
window.minsize(600, 500)
window.maxsize(600, 500)


# Function to handle the translation
def translate():
    try:
        txt = text1.get(1.0, END).strip()  # Get text from input box
        c1 = combo1.get()  # Source language from combo1
        c2 = combo2.get()  # Target language from combo2

        if txt:  # If there is text to translate
            translator = Translator()

            # Get the language codes from the selected languages
            src_lang_code = [code for code, lang in language.items() if lang == c1][0]
            dest_lang_code = [code for code, lang in language.items() if lang == c2][0]

            # Perform translation
            translated_words = translator.translate(txt, src=src_lang_code, dest=dest_lang_code)

            # Clear the destination text box and insert the translated text
            text2.delete(1.0, END)
            text2.insert(END, translated_words.text)
        else:
            messagebox.showerror("Input Error", "Please enter text to translate")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))  # Display the actual error message for debugging


# Fetch available languages from googletrans
language = googletrans.LANGUAGES
lang_value = list(language.values())

# Create the first combobox for source language selection
combo1 = ttk.Combobox(window, values=lang_value, state='readonly')
combo1.place(x=100, y=20)
combo1.set("choose source language")

# Create the text box for source text
f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)
text1 = Text(f1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

# Create the second combobox for destination language selection
combo2 = ttk.Combobox(window, values=lang_value, state='readonly')
combo2.place(x=300, y=20)
combo2.set("choose target language")

# Create the text box for translated text
f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)
text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

# Create the Translate button
button = Button(window, text='Translate', font=('normal', 15), bg='yellow', command=translate)
button.place(x=230, y=300)

# Run the Tkinter event loop
window.mainloop()