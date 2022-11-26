# import tkinter as tk


# def start():
#     global i, callback_id
#     text_label.config(text=i)
#     i += 1
#     callback_id = text_label.after(1000, start)


# def reset():
#     global i, callback_id
#     i = 0
#     if callback_id is not None:
#         text_label.after_cancel(callback_id)
#         callback_id = None
#     start()


# window = tk.Tk()
# window.geometry('400x400')

# text_label = tk.Label(window, text="start")
# text_label.pack()

# callback_id, i = None, 0
# tk.Button(window, text="reset", command=reset).pack()

# window.mainloop()


