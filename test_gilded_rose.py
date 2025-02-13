import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # Original logical test
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(90, sulfuras_item.quality)  # Changed to 90 to make it fail
        self.assertEquals(5, sulfuras_item.sell_in)   # Changed to 5 to make it fail
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # Original syntax test
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()  # This fails with syntax error
        self.assertEquals(["Sulfuras"], all_items)

    # New logical test 1
    def test_backstage_passes_quality_changes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)  # This should fail
        self.assertEquals(10, items[0].sell_in)

    # New logical test 2
    def test_item_quality_never_negative(self):
        items = [Item("regular item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].quality)  # Changed to expect -1 to make it fail
        self.assertEquals(5, items[0].sell_in)   # Changed to not expect decrease

    # New logical test 3
    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)  # This should fail because Aged Brie increases in quality

    # New logical test 4
    def test_conjured_item_quality(self):
        items = [Item("Conjured", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].quality)  # This should fail as Conjured items degrade differently
        self.assertEquals(5, items[0].sell_in)  # This should fail as sell_in should decrease

if __name__ == '__main__':
    unittest.main()
