from models.user import User
from models.property import Property

from services.user_service import UserService
from services.property_service import PropertyService

from ui.display_user import DisplayUser
from ui.display_property import DisplayProperty


def main():
    user_service = UserService()
    property_service = PropertyService()

    display_user = DisplayUser()
    display_property = DisplayProperty()

    user1 = User(1, 'Suraj', 'iyersuraj7@gmail.com')
    user_service.add_user(user1)
    display_user.display_user(user1)

    user2 = User(2, 'Coolraj', 'surajiyer@cred.club')
    user_service.add_user(user2)
    display_user.display_user(user2)

    property1 = Property(1, 'Beautiful House', "Banglore", 500000, 2500, "Crazyraj")
    property_service.add_property(property1)
    display_property.display_property(property1)

    property2 = Property(2, 'Modern Apartment', "Mumbai", 750000, 1200, "Crazyraj")
    property_service.add_property(property2)
    display_property.display_property(property2)

    try:
        bought_property = property_service.buy_property(1, 1) 
        print(f"Property bought by {user_service.get_user(1).name}: {bought_property}")
    except Exception as e:
        print(f"Error: {e}")

    print("Property List After Purchase:")
    for prop in property_service.list_all_properties():
        print(prop)

    try:
        property_service.buy_property(1, 2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
