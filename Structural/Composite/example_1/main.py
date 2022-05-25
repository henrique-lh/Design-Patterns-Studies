from abc import ABC, abstractmethod
from typing import List


# The component interface declares common operations for both
# simple and complex objects of a composition.
class Graphic(ABC):

    @abstractmethod
    def move(self, x: int, y: int):
        pass

    @abstractmethod
    def draw(self):
        pass

# The leaf class represents end objects of a composition. A
# leaf object can't have any sub-objects. Usually, it's leaf
# objects that do the actual work, while composite objects only
# delegate to their sub-components.
class Dot(Graphic):

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> str:
        return f"Draw a dot at {self.x=} and {self.y=}"

# All component classes can extend other components.
class Circle(Dot):

    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y)
        self.radius = radius

    def draw(self) -> str:
        return f"{super().draw()} with radius {self.radius}"

# The composite class represents complex components that may
# have children. Composite objects usually delegate the actual
# work to their children and then "sum up" the result.
class CompoundGraphic(Graphic):

    children: List[Graphic]

    # A composite object can add or remove other components
    # (both simple or complex) to or from its child list.
    def add(self, child: Graphic) -> None:
        CompoundGraphic.children.append(child)

    def remove(self, child: Graphic) -> None:
        CompoundGraphic.children.remove(child)

    def move(x, y) -> None:
        for child in CompoundGraphic.children:
            child.move(x, y)

    # A composite executes its primary logic in a particular
    # way. It traverses recursively through all its children,
    # collecting and summing up their results. Since the
    # composite's children pass these calls to their own
    # children and so forth, the whole object tree is traversed
    # as a result.
    def draw(self) -> None:
        """ 1. For each child component:

                - Draw the component.
                - Update the bounding rectangle.
            2. Draw a dashed rectangle using the bounding coordinates.

            The client code works with all the components via their base
            interface. This way the client code can support simple leaf
            components as well as complex composites.

            Structural Design Patterns / Composite
        """
        pass

# The client code works with all the components via their base
# interface. This way the client code can support simple leaf
# components as well as complex composites.
class ImageEditor:

    def __init__(self):
        all_ = CompoundGraphic()
        all_.add(Dot(1, 2))
        all_.add(Circle(5, 3, 10))
        # ...

    # Combine selected components into one complex composite component
    def group_selected(self, components: List[Graphic]):
        group = CompoundGraphic()
        group.add(components)
        group.remove(components)
        self.all_.add(group)
        # Alll components will be drawn
        self.all_.draw()
