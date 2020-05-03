# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    
    def test_update_quality_for_item_before_sell_date_decreases_quality_by_1(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        
        GildedRose(items).update_inventory()
        
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)
    
    def test_update_quality_for_another_item_before_sell_date_decreases_quality_by_1(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=5, quality=7)]
        
        GildedRose(items).update_inventory()
        
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_update_quality_for_item_after_sell_date_decreases_quality_by_2(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        
        GildedRose(items).update_inventory()
        
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
    
    def test_update_quality_for_item_quality_does_not_drop_below_0(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=0)]
        
        GildedRose(items).update_inventory()
        
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_update_quality_for_aged_brie_before_sell_date_increases_quality_by_1(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)
    
    def test_update_quality_for_aged_brie_does_not_increase_above_50(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_update_quality_for_sulfuras_sell_in_and_quality_do_not_change(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_update_quality_for_backstage_pass_increases_quality_by_1(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_update_quality_for_backstage_pass_with_below_10_sell_in_increases_quality_by_2(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_update_quality_for_backstage_pass_with_below_5_sell_in_increases_quality_by_3(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_update_quality_for_backstage_pass_with_0_sell_in_has_quality_of_0(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=2)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_update_quality_for_backstage_pass_does_not_increase_above_50(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_update_quality_for_conjured_item_quality_decreases_by_2(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)
    
    def test_update_quality_for_conjured_item_quality_never_drops_below_0(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=0)]

        GildedRose(items).update_inventory()
        
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
