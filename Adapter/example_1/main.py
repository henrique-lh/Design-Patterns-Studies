class Target:
    """The target defines the domain-specific interface used by the cliente code"""

    def request(self) -> str:
        return "Target: The default target's behavior"


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")

def main() -> None:
    print("\nClient: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adptee = Adaptee()
    print("Client: The Adaptee class has a weird interce. See, I don't understand it:")
    print(f"Adaptee: {adptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via Adapter:")
    adapter = Adapter()
    client_code(adapter)
    print()

if __name__ == "__main__":
    main()
