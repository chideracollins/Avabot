import scraper


class Item:
    def __init__(self, name, description=None) -> None:
        self.name = name
        self.description = description
    
    
class ItemInStore(Item):
    def __init__(self, specs) -> None:
        self.specifications = specs
        
        
    def related(self, products_links: list):
        pass


class ItemRequested(Item):
    def results(self):
        pass
        
        
def create_items(items: dict):
    items_created = []
    for name, desc in items.items():
        if len(desc) < 1:
            items_created.append(ItemRequested(name))
            continue
        items_created.append(ItemRequested(name, description=desc))
    return items_created