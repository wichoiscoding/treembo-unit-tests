class Product:
    def __init__(self, name: str, category: str, price: float):
        self._validate_category(category)
        self._validate_price(price)
        self.name = name
        self.category = category
        self.price = price

    @staticmethod
    def _validate_category(category: str):
        allowed_categories = ["Semillas", "Químicos"]
        if category not in allowed_categories:
            raise ValueError(f"Category '{category}' is not allowed. Use {allowed_categories}.")

    @staticmethod
    def _validate_price(price: float):
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, price={self.price})"


class Marketplace:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only instances of Product can be added.")
        self._products.append(product)

    def search_products(self, search_term: str):
        if not search_term:
            raise ValueError("Search term cannot be empty.")
        return [
            product for product in self._products
            if search_term.lower() in product.name.lower()
        ]

    def get_all_products(self):
        return self._products
