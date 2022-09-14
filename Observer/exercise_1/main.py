from __future__ import annotations
from abc import ABCMeta, abstractmethod
import tkinter as tk
from typing import List


class Publisher(metaclass=ABCMeta):

	"""
    The Publisher interface declares a set of methods for managing subscribers.
    """

	@abstractmethod
	def subscribe(self) -> None:
		"""
        Attach an observer to the subject.
        """
		pass

	@abstractmethod
	def unsubscribe(self) -> None:
		"""
        Detach an observer from the subject.
        """
		pass

	@abstractmethod
	def notify(self) -> None:
		"""
        Notify all observers about an event.
        """
		pass


class ConcretePublisher(Publisher):

	_state: str = None

	_subscribers_list: List[WindowSubscriber] = []

	def subscribe(self, new_window: WindowSubscriber) -> None:
		self._subscribers_list.append(new_window)

	def unsubscribe(self, removed_window) -> None:
		try:
			self._subscribers_list.remove(removed_window)
		except ValueError as e:
			raise(e)

	@classmethod
	def notify(cls, string: str) -> None:
		cls._state = string
		for obs in cls._subscribers_list:
			obs.update(cls)


class WindowSubscriber(metaclass=ABCMeta):

	def __init__(self, master) -> None:
		self.master = master
		self.master.geometry("800x400+200+200")
		self.frame = tk.Frame(self.master)

		self.text = tk.StringVar()
		self.text.set("Texto inicial - Ambas as janelas")
		self.label = tk.Label(self.frame, textvariable=self.text,  font=("Courier 22 bold"))
		self.label.pack(pady=20)

		self.entry = tk.Entry(self.frame, width=40)
		self.entry.focus_set()
		self.entry.pack(pady=20)

		self.change = tk.Button(self.frame, text=f"Change text", command=self.change_text)
		self.change.pack(pady=20)

		self.quit = tk.Button(self.frame, text = f"Quit this window.", command = self.close_window)
		self.quit.pack(pady=20)
		
		self.frame.pack(pady=20)

	def close_window(self) -> None:
		"""Close a window"""
		self.master.destroy()

	def change_text(self) -> None:
		string = self.entry.get()
		ConcretePublisher.notify(string)

	@abstractmethod
	def update(self, subject: Publisher) -> None:
		pass


class Win1Subscriber(WindowSubscriber):

	def __init__(self, master) -> None:
		super().__init__(master)

	def update(self, publisher: Publisher) -> None:
		new_text = f"{publisher._state} - Janela 1"
		self.text.set(new_text)

class Win2Subscriber(WindowSubscriber):

	def __init__(self, master) -> None:
		super().__init__(master)

	def update(self, publisher: Publisher) -> None:
		new_text = f"{publisher._state} - Janela 2"
		self.text.set(new_text)


def main() -> None:

	publisher = ConcretePublisher()

	root = tk.Tk()
	app = Win1Subscriber(master=root)
	publisher.subscribe(app)

	second_win = tk.Toplevel(root)
	app2 = Win2Subscriber(second_win)
	publisher.subscribe(app2)

	root.mainloop()

if __name__ == "__main__":
	main()
