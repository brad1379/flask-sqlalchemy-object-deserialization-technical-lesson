# lib/post_load.py

from marshmallow import Schema, fields, post_load
from pprint import pprint

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
        
    def give_treat(self):
        self.tail_wagging = True
        
    def scold(self):
        self.tail_wagging = False

# schema

class DogSchema(Schema):
    name = fields.Str()
    breed = fields.Str()
    tail_wagging = fields.Boolean()

    # Take a dictionary of deserialized data and return a model
    @post_load
    def make_dog(self, data, **kwargs):
        return Dog(**data)

# deserialize

dog_schema = DogSchema()
dog_json = '{"name": "Snuggles", "breed": "Beagle", "tail_wagging": true}'
dog = dog_schema.loads(dog_json)
print(type(dog))             # => <class '__main__.Dog'>
print(isinstance(dog, Dog))  # => True
pprint(dog)                  # => <__main__.Dog object at 0x7efafa51c460>

pprint(dog_schema.dumps(dog)) # Output -> '{"name": "Snuggles", "breed": "Beagle", "tail_wagging": true}'
dog.scold()
pprint(dog_schema.dumps(dog)) # Output -> '{"name": "Snuggles", "breed": "Beagle", "tail_wagging": false}'
dog.give_treat()
pprint(dog_schema.dumps(dog)) # Output -> '{"name": "Snuggles", "breed": "Beagle", "tail_wagging": true}'
