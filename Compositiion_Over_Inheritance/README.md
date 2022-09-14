# The Composition Over Inheritance Principle

"Favor object composition over class inheritance", GoF.

This material was retired from [python-patterns.guide](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)

## Why should I avoid inheritance?

* Using inheritance stratagy means a class often needs to be specialized along several different designs axes at once.
* GoF called it as "a proliferation of classes". Observe the `subclas-explosion-problem.py` file

## Explaining the problem

In the first look, we have:

```python

# Initial class
class Logger(object):

    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush


# Two subclasses
class SocketLogger(Logger):

    def __init__(self, sock):
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class SyslogLogger(Logger):

    def __init__(self, priority):
        self.priority = priority

    def log(self, message):
        syslog.syslog(self.priority, message)
```

Now, imagine we just want to get the errors that the "Error" string appears:

```python

class FilteredLogger(Logger):

    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


f = FilteredLogger('Error', sys.stdout)
f.log('Ignored: this is not important')
f.log('Error: but you want to see this')
```

So here message is filtered and it's not written to the file. The problems is: the others classes won't deal with that case! For each class, we would need a `Filtered` class, it means, in the end of the classes design, you'll have $2 \times n$ classes, and now we have the "explosion of subclasses".

The class also violate the "Single Responsibility Principle"

## Solution 1: The Adapter Pattern

1. We keep the original `Logger`
2. We also keep the `FilteredLogger`
3. The destination is adapted to the behavior of a file, and `Logger` outputs the file

```python
import socket

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
# The socket received: Error: message number two\t
```

## Solution 2: The Bridge Pattern
