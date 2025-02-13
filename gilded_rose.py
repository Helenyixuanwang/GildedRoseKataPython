# -*- coding: utf-8 -*-
# gilded_rose.py
from item import Item
from item_strategies import (
    NormalItemStrategy,
    AgedBrieStrategy,
    BackstagePassStrategy,
    SulfurasStrategy
)

class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # Create strategy mapping
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy()
        }
        self.default_strategy = NormalItemStrategy()

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, self.default_strategy)
            strategy.update_quality(item)
