from dao.property_dao import PropertyDAO
from models.property import Property

property_dao = PropertyDAO()

class PropertyService:
    def __init__(self):
        self.property_dao = property_dao

    def add_property(self, property: Property):
        return self.property_dao.create_property(property)

    def get_property(self, id: int):
        return self.property_dao.get_property(id)

    def list_all_properties(self):
        return self.property_dao.get_all_properties()

    def update_property(self, property: Property):
        if property.is_available:
            return self.property_dao.update_property(property)
        else:
            raise Exception("Cannot update a property that has already been sold.")

    def remove_property(self, id: int):
        property = self.get_property(id)
        if property and property.is_available:
            return self.property_dao.delete_property(id)
        else:
            raise Exception("Cannot delete a property that has already been sold.")

    def buy_property(self, id: int, buyer_id: int):
        property = self.get_property(id)
        if property:
            if property.is_available:
                property.mark_as_sold(buyer_id)
                self.property_dao.update_property(property)
                return property
            else:
                raise Exception("Property is already sold.")
        else:
            raise Exception("Property not found.")
