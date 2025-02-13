# item_strategies.py
from abc import ABC, abstractmethod
from item import Item

class ItemStrategy(ABC):
    @abstractmethod
    def update_quality(self, item: Item) -> None:
        """Update the quality of an item based on its specific rules"""
        pass

class NormalItemStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in <= 0 and item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1

class AgedBrieStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in <= 0 and item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

class BackstagePassStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in <= 0:
            item.quality = 0
        item.sell_in = item.sell_in - 1

class SulfurasStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        # Sulfuras never changes
        # Sulfuras never changes quality and never needs to be sold
        item.quality = 80  # Always 80
        # Don't decrease sell_in since it never needs to be sold

class ConjuredStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        # Conjured items degrade twice as fast
        if item.quality > 0:
            item.quality = max(0, item.quality - 2)
            if item.sell_in <= 0:
                item.quality = max(0, item.quality - 2)
        item.sell_in = item.sell_in - 1
