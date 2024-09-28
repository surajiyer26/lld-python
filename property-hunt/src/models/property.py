class Property:
    def __init__(self, id: int, title: str, location: str, price: float, size: float, owner_id: int):
        self.id = id
        self.title = title
        self.location = location
        self.price = price
        self.size = size
        self.owner_id = owner_id
        self.buyer_id = None
        self.is_available = True

    def mark_as_sold(self, buyer_id : int):
        self.buyer_id = buyer_id
        self.is_available = False

    def __str__(self):
        if self.is_available:
            return f'{self.title} in {self.location}, {self.size} sqft, priced at ${self.price}'
        else:
            return f'{self.title} in {self.location} (Sold), {self.size} sqft, sold for ${self.price} to User {self.buyer_id}'
        