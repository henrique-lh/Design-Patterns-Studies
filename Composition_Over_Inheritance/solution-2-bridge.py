"""This solution use the Bridge Pattern"""

from logging import Filter
import sys
import syslog

# The "abstraction" that callers will see

class Logger(object):

    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.emit(message)


class FilteredLogger(Logger):

    def __init__(self, pattern, handler):
        self.pattern = pattern
        super().__init__(handler)

    def log(self, message):
        if self.pattern in message:
            super().log(message=message)

# The "implementation" hidden behind the scenes

class FileHandler:

    def __init__(self, file):
        self.file = file

    def emit(self, message):
        self.file.write(message + '\n')
        self.file.flush()


class SocketHandler:

    def __init__(self, sock):
        self.sock = sock

    def emit(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class SyslogHandler:

    def __init__(self, priority):
        self.priority = priority

    def emit(self, message):
        syslog.syslog(self.priority, message)


handler = FileHandler(sys.stdout)
logger = FilteredLogger('Error', handler)

logger.log('Ignored: this will not be logged')
logger.log('Error: this is important')