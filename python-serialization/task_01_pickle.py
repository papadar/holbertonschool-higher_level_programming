#!/usr/bin/env python3
"""pickle the data"""
import pickle


class CustomObject:
    """This is the Custom object class"""
    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """this is the display method"""
        print(
            "Name: {}\nAge: {}\nIs Student: {}\n"
            .format(self.name, self.age, self.is_student)
        )

    def serialize(self, filename):
        """This is the serialise method"""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialise & create the class"""
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
                obj = cls(data.name, data.age, data.is_student)
                return obj
        except (
            FileNotFoundError,
            TypeError,
            EOFError,
            pickle.UnpicklingError,
            AttributeError,
            ImportError,
            IndexError,
            ValueError
        ):
            return None
