class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

class Viber:
    messages = []
    @staticmethod
    def add_message(msg):
        Viber.messages.append(msg)
   
    @staticmethod    
    def remove_message(msg):
        Viber.messages.remove(msg)
    
    @staticmethod    
    def set_like(msg):
        if not msg.fl_like:
            msg.fl_like = True
        else:
            msg.fl_like = False

    @staticmethod     
    def show_last_message(number):
        for i in range(number * -1, 0, -1):
            print(Viber.messages[i])

    @staticmethod    
    def total_messages():
        return len(Viber.messages)
