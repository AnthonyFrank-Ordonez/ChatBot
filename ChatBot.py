import customtkinter as ctk
from variables import check_content, system_exit


class Chatbot:
    def __init__(self, font_fam):
        self.window = ctk.CTk()
        self.window.geometry('600x550')
        self.window.title('CHATBOT: YOUR FRIENDLY NEIGHBOR BOT!')
        self.window.resizable(False, False)
        self.font = font_fam

        # widgets
        self.text_widget = ctk.CTkTextbox(self.window, height=500, width=600, font=('arial bold', 15))
        self.user_entry = ctk.CTkEntry(self.window, width=500, height=50, border_width=1, corner_radius=1)
        self.enter_btn = ctk.CTkButton(self.window, text='ENTER', width=100, height=50, corner_radius=1, font=font_fam,
                                       fg_color='green', hover_color='grey')

        # Configure some startups in textbox
        self.text_widget.insert(1.0, text='Bot: Welcome!, To the ChatBot!\n')
        self.text_widget.configure(cursor='arrow', state='disabled')

        # Bind the entry as well as the button
        self.user_entry.focus()
        self.user_entry.bind(sequence='<Return>', command=self.once_pressed_or_entered)
        self.enter_btn.bind(sequence='<Button-1>', command=self.once_pressed_or_entered)

        # Place Grid
        self.text_widget.grid(row=0, columnspan=5)
        self.user_entry.grid(row=1, columnspan=3)
        self.enter_btn.grid(row=1, column=4)

    def once_pressed_or_entered(self, event):
        """
        Get the contents or message from the entry widget

        :param event: Keybindings from the keyboard or that is set from the specific widgets
        :return:
        """
        content: str = self.user_entry.get()
        self.insert_message(content)  # call the insert_message function to insert the message

    def insert_message(self, msg_content: str, user='You'):
        """
        Insert message on the text widget as well as get the reply base on the user input

        :param msg_content: The message comes from the entry widget
        :param user: The default value which is the user or 'You'
        :return: None
        """
        # will not display anything if the user tries to input an empty value or string.
        if not msg_content:
            return

        elif msg_content in system_exit:
            exit()

        self.user_entry.delete(0, 'end')  # user message
        user_msg: str = f'{user}: {msg_content}\n'
        self.text_widget.configure(state='normal')
        self.text_widget.insert('end', user_msg)
        self.text_widget.configure(state='disabled')

        if match := check_content(msg_content):  # bot message
            bot_msg = f'Bot: {match}\n'
            self.text_widget.configure(state='normal')
            self.text_widget.insert('end', bot_msg)
            self.text_widget.configure(state='disabled')

        else:
            # bot reply if the questions asked is still not on the bot knowledge JSON
            bot_error_msg: str = "Bot: Sorry I can't understand what you are asking, can you please repeat that?\n"
            self.text_widget.configure(state='normal')
            self.text_widget.insert('end', bot_error_msg)
            self.text_widget.configure(state='disabled')

        self.text_widget.see('end')

    def run(self):
        """Run the app"""
        self.window.mainloop()


def main():
    """Main Function"""
    font: tuple = ('Arial Bold', 14)  # font that will utilize from the system
    bot = Chatbot(font)
    bot.run()


if __name__ == '__main__':
    main()
