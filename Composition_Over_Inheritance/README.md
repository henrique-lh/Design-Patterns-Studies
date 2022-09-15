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

The purpose of Bridge Pattern is separate the abstraction from the implementation

In this case, the "abstraction" will be the filtering classes, while the "implementation" will be the output classes

```python
# The “implementations” hidden behind the scenes.

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
```

## Solution 3: The Decorator Pattern

What if we wanted to apply two different filters to the same log? The previous solutions wouldn't work, once there's an assymemetry between the interfaces they offer and the interface they wrap: they offer a `log()` method but call their handler’s `emit()` method. Wrapping one filter in another would result in an AttributeError when the outer filter tried to call the inner filter’s `emit()`.

A possible solution is: provide the same interface for both the filters and handlers classes

```python
# The filter calls the same method it offers

class LogFilter:

    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger

    def log(self, message):
        if self.pattern in message:
            self.logger.log(message)


log1 = FileLogger(sys.stdout)
log2 = LogFilter('Error', log1)

log1.log('Noisy: this logger always produces output')

log2.log('Ignored: this will be filtered out')
log2.log('Error: this is important and gets printed')
```

But note the one place where the symmetry of this design breaks down: while filters can be stacked, output routines cannot be combined or stacked. Log messages can still only be written to one output.
