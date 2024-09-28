from models.property import Property

class PropertyDAO:
    def __init__(self):
        self.properties = {}

    def create_property(self, property: Property):
        self.properties[property.id] = property
        return property
    
    def get_property(self, id: int):
        return self.properties.get(id)
    
    def get_all_properties(self):
        return list(self.properties.values())
    
    def update_property(self, property: Property):
        if property.id in self.properties:
            self.properties[property.id] = property
            return property
        return None
    
    def delete_property(self, id: int):
        if id in self.properties:
            return self.properties.pop(id)
        return None