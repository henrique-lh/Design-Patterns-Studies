"""This solutino uses the Adapter pattern"""

import socket
import sys
import syslog


# Initial class
class Logger(object):

    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush


class FilteredLogger(Logger):

    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


class FileLikeSocket:

    def __init__(self, sock):
        self.sock = sock

    def write(self, message_and_newline):
        self.sock.sendall(message_and_newline.encode('ascii'))

    def flush(self):
        pass


class FileLikeSyslog:

    def __init__(self, priority):
        self.priority = priority

    def write(self, message_and_newline):
        message = message_and_newline.rstrip('\n')
        syslog.syslog(self.priority, message)

    def flush(self):
        pass


sock1, sock2 = socket.socketpair()

fs = FileLikeSocket(sock=sock1)
logger = FilteredLogger('Error', fs)
logger.log(message='Warning: message number one')
logger.log(message='Error: message number two')

print(f'The socket received: {sock2.recv(512)}')