# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog: 
    """
    simple dog class to learn object orientation programing

    Attributes:
    breed = bredd of dog
    fur_color = color of dog
    name= name of dog
    age= age of dog
    """
        
    def __init__ (self, breed, fur_color, name, age):
        """initialize new dog with breed, fur color, name, and age"""
        self.breed = breed         
        self.fur_color = fur_color
        self.name = name
        self.age =age

    def __str__(self):
        """string representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    
    def bark(self):
        return f"{self.name} says: Woof, Woof!"


if __name__== "__main__":
    berg_dog = Dog("labrador", "black", "logan", 9)
    aidan_dog=Dog("lab pitt mix", "grey", "cubbie", 9)
    
    print (berg_dog)
    print(aidan_dog)
    print()
    print(aidan_dog.bark())

