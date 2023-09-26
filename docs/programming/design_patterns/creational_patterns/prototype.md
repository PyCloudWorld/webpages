# Prototype
![prototype](images/prototype.png)

## CODE
```python
import copy

class Doors:
    def __init__(self, count: int = None):
        self.number_of_doors =  count

class Body:
    def __init__(self, color: str = None):
        self.color = color

class Chasis:
    def __init__(self, number: str = None):
        self.number = number

class Car:
    def __init__(self,
                 name: str = None,
                 door : Doors = None,
                 body: Body = None,
                 chasis: Chasis = None):
        self.name = name
        self.number_of_doors = door.number_of_doors
        self.body_color = body.color
        self.chasis_number = chasis.number

    def __str__(self):
        return str(self.name)

    def clone(self):
        return copy.deepcopy(self)


bmw_doors = Doors(5)
bmw_body = Body("black")
bmw_chasis = Chasis("ash24031986")
bmw = Car(name="BMW", door=bmw_doors, body=bmw_body, chasis=bmw_chasis)
bmw_new_model = bmw.clone()
```
