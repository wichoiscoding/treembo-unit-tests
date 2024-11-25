import pytest
from models.marketplace import Product, Marketplace

# Test for the Product class
def test_product_creation_valid():
    product = Product(name="Semillas de Maíz", category="Semillas", price=150.0)
    assert product.name == "Semillas de Maíz"
    assert product.category == "Semillas"
    assert product.price == 150.0

def test_product_invalid_category():
    with pytest.raises(ValueError, match="is not allowed"):
        Product(name="Herbicida", category="Herramientas", price=200)

def test_product_invalid_price():
    with pytest.raises(ValueError, match="must be greater than zero"):
        Product(name="Semillas", category="Semillas", price=-10)

# Test for the Marketplace class
@pytest.fixture
def marketplace():
    """Fixture to create a Marketplace instance for tests."""
    return Marketplace()

def test_add_product(marketplace):
    product = Product(name="Fertilizante Orgánico", category="Químicos", price=100)
    marketplace.add_product(product)
    assert product in marketplace.get_all_products()

def test_search_products_exact(marketplace):
    product = Product(name="Semillas de Girasol", category="Semillas", price=120)
    marketplace.add_product(product)
    results = marketplace.search_products("Semillas de Girasol")
    assert len(results) == 1
    assert results[0] == product

def test_search_products_partial(marketplace):
    product = Product(name="Semillas de Girasol", category="Semillas", price=120)
    marketplace.add_product(product)
    results = marketplace.search_products("Girasol")
    assert len(results) == 1
    assert results[0] == product

def test_search_products_no_match(marketplace):
    product = Product(name="Fertilizante Orgánico", category="Químicos", price=100)
    marketplace.add_product(product)
    results = marketplace.search_products("Insecticida")
    assert len(results) == 0

def test_search_empty_term(marketplace):
    product = Product(name="Semillas de Girasol", category="Semillas", price=120)
    marketplace.add_product(product)
    with pytest.raises(ValueError, match="cannot be empty"):
        marketplace.search_products("")

def test_add_invalid_object(marketplace):
    with pytest.raises(TypeError, match="Only instances of Product can be added"):
        marketplace.add_product("Not a product")
