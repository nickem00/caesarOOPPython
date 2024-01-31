import time


class Message:
    def __init__(self, src, dest, data):
        self.src = src          # sender
        self.dest = dest        # reciever
        self.data = data        # the content
        self.timestamp = time.ctime()  # when it was created

    def __str__(self):
        return (f'({self.timestamp})  {self.src} --> '
                f'{self.dest}  :  {self.data}')
