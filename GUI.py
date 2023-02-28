from tkinter import *
from user_chat import get_response, bot_name

BG_Orange = "#FF4500"
BG_color = "#FFFFFF"
Text_color = "#17202A"

Font = "Helvetica 14"
font_bold = "Helvetica 14 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()  
          
    def _setup_main_window(self):
        self.window.title("chat with us")
        self.window.resizable(width=False, height=False )
        self.window.configure(width=550 , height=550 , bg= BG_color )
        
        head_lablel = Label(self.window, bg = BG_color, fg = Text_color,
                            text = "Welcome", font= font_bold, pady = 12)
        head_lablel.place(relwidth=1)
        
        line = Label(self.window, width=630, bg = BG_Orange)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        self.text_widget= Text(self.window, width =15, height= 1, bg = BG_color, fg = Text_color,
                               font= Font, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)  
        bottom_label = Label(self.window, bg = BG_Orange, height=80)
        bottom_label.place(relwidth=1, rely=0.825) 
        
        self.msg_entry = Entry(bottom_label, bg = BG_color , fg = Text_color, font = Font)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        send_button = Button(bottom_label, text= "Send", font = font_bold, width= 15, bg = BG_Orange,
                             command=lambda:  self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    
    
    def  _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
if __name__  == "__main__":
    app = ChatApplication()
    app.run()