# -*- coding: utf-8 -*-
PRODUCTS = {
    "brie": "Aged Brie",
    "pass": "Backstage passes to a TAFKAL80ETC concert",
    "sulfuras": "Sulfuras, Hand of Ragnaros",
    "conjured": "Conjured Mana Cake",
}

MAX_QUALITY = 50
MIN_QUALITY = 0

class GildedRose(object):

    @staticmethod
    def _update_sell_in(item):
        if item.name != PRODUCTS["sulfuras"]:
            item.sell_in -= 1
        return item
    
    @staticmethod
    def _incr_quality(quality, amount, max=MAX_QUALITY):
        if quality + amount <= max:
            quality += amount
        return quality
    
    @staticmethod
    def _decr_quality(quality, amount, min=MIN_QUALITY):
        if quality - amount >= min:
            quality -= amount
        return quality
    
    @staticmethod
    def _expired(sell_in):
        return sell_in <= 0

    def __init__(self, items):
        self.items = items
    
    def update_inventory(self):
        for item in self.items:
            # update `sell_in` by one interval (day)
            item = GildedRose._update_sell_in(item)

            # quality of `brie` increases by 1
            if item.name == PRODUCTS["brie"]:
                item.quality = GildedRose._incr_quality(item.quality, 1)
            
            # quality of `backstage pass`
            # ... becomes 0 after concert day
            # ... increases by 3 if `sell_in` less than/equals 5
            # ... increases by 2 if `sell_in` less than/equals 10
            # ... increases by 1 if `sell_in` greater than 10
            if item.name == PRODUCTS["pass"]:
                if GildedRose._expired(item.sell_in):
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality = GildedRose._incr_quality(item.quality, 3)
                elif item.sell_in <= 10:
                    item.quality = GildedRose._incr_quality(item.quality, 2)
                else:
                    item.quality = GildedRose._incr_quality(item.quality, 1)
            
            # quality of `conjured` decreases by 2
            if item.name == PRODUCTS["conjured"]:
                item.quality = GildedRose._decr_quality(item.quality, 2)
            
            # quality of uncategorized items:
            # ... decreases by 1 if `sell_in` is greater than 0
            # ... decreases by 2 if `sell_in` is less than 0
            if item.name not in PRODUCTS.values():
                if GildedRose._expired(item.sell_in):
                    item.quality = GildedRose._decr_quality(item.quality, 2)
                else: 
                    item.quality = GildedRose._decr_quality(item.quality, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
        