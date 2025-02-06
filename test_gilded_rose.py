import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_backstage_passes_quality_changes(self):
        """Test that Backstage passes increase in quality as concert approaches"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
    
        # Quality should increase by 2 when there are 10 days or less
        self.assertEquals(22, items[0].quality)
        self.assertEquals(10, items[0].sell_in)

    def test_item_quality_never_negative(self):
        """Test that the quality of an item is never negative"""
        items = [Item("regular item", 5, 0)]  # Start with quality 0
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
    
        self.assertGreaterEqual(items[0].quality, 0)
        self.assertEquals(4, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
