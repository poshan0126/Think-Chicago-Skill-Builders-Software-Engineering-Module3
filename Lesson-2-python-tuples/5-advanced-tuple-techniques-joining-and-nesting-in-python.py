class CatalogMerger:
    def __init__(self, *catalogs):
        self.catalogs = catalogs

    def merge_catalogs(self):
        # Joining multiple catalogs into one using tuple concatenation
        combined_catalog = tuple()
        for catalog in self.catalogs:
            combined_catalog += catalog
        return combined_catalog

    def display_combined_catalog(self):
        combined_catalog = self.merge_catalogs()
        print("Combined Product Catalog:")
        for product_name, price in combined_catalog:
            print(f"{product_name}: ${price}")

# Example catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Create an instance of CatalogMerger with the example catalogs
merger = CatalogMerger(catalog1, catalog2)

# Display the combined catalog
merger.display_combined_catalog()
