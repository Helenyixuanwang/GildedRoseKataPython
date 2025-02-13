# test_gilded_rose.py
import unittest
from item import Item
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    # Original logical test
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]  # Exact name match
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)  # Changed to expect 80 
        self.assertEquals(5, sulfuras_item.sell_in)   # Changed to 5 to make it fail
        self.assertEquals("Sulfuras, Hand of Ragnaros", sulfuras_item.name)

    # Original syntax test
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()  # This fails with syntax error
        self.assertEquals(["Sulfuras, Hand of Ragnaros"], all_items)

    # New logical test 1
    def test_backstage_passes_quality_changes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)  #  Changed to 21 (regular increase) 
        self.assertEquals(10, items[0].sell_in)

    # New logical test 2
    def test_item_quality_never_negative(self):
        items = [Item("regular item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)  # Changed to expect 0 
        self.assertEquals(4, items[0].sell_in)   # Changed to not expect decrease

    # New logical test 3
    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)  # Should increase by 1
        self.assertEquals(4, items[0].sell_in)   # SellIn should decrease by 1

    # New logical test 4
    def test_conjured_item_quality(self):
        items = [Item("Conjured", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)  # Degrades by 2 
        self.assertEquals(4, items[0].sell_in)  # decrease by 1 

if __name__ == '__main__':
    unittest.main()
