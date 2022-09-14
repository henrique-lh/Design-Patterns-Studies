from abc import ABC, abstractmethod


# All of our ducks need to implement the Duck interface
# Remember, when we say interface we really mean a supertype
# which in this case is an abstract class
class Duck(ABC):
    @abstractmethod
    def quack():
        pass

    @abstractmethod
    def fly():
        pass

# This is a concrete class that extends Duck
class MallardDuck(Duck):
    def quack():
        print("Quack")

    def fly():
        print("Fly fly fly!")


# And this is our new interace that all turkeys 
# will need to extend:
class Turkey(ABC):

    # Turkeys don't quack - they gobble
    @abstractmethod
    def gobble(self):
        pass

    # They can fly, but shorter distances than ducks
    @abstractmethod
    def fly(self):
        pass

# This is a concrete class that extends Turkey
class WildTurkey(Turkey):

    def gobble(self):
        print("Gobble gobble..")

    def fly(self):
        print("Flying for a short distance")


# Suppose that we are short on Ducks and the solution is to use some
# Turkey objects in their place. To do this, we would need to create
# an adapter:

# We start by implementing the interface of the type that we are 
# adapting to. Since we want to use Turkeys in the place of ducks
# but without the client having to know the Turkey interface, 
# we need to create an interface that implements what the client
# expects to see - in this case the Duck interface:
class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey: Turkey):
        # We get a reference to the object that we are adapting 
        # through the constructor
        self.turkey = turkey

    # Next we implement all the methods that the client expects,
    # in this case the quack() and fly() methods of the Duck.
    # Under the hood, the adapter calls the turkey methods:
    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()

def main() -> None:
    # All that remains is to test our adapter:
    duck: MallardDuck = MallardDuck()
    turkey: WildTurkey = WildTurkey()

    turkeyAdapter: Duck  = TurkeyAdapter(turkey)

    turkeyAdapter.fly()
    # Although the client calls the Duck quack() method,
    # under the hood this is translated to the turkey's gobble() method:
    turkeyAdapter.quack()

if __name__ == "__main__":
    main()