import unittest

from gilded_rose import Item, GildedRose
from approvaltests import verify, verify_all_combinations, verify_all_combinations_with_namer


class TestApprovals(unittest.TestCase):
    def test_single_item(self):
        items = [Item("normal item", 10, 5)]
        sut = GildedRose(items)

        # Act
        sut.update_quality()
        actual_updated_item = items[0]

        # Assert
        verify(actual_updated_item)

    def test_legendary_items_sell_in_and_quality_unchanged(self):
        def update_legendary_item(item):
            sut = GildedRose([item])
            sut.update_quality()
            output = f"{item.name} {item.sell_in} {item.quality}"
            return output

        verify_all_combinations(update_legendary_item,
    [
                [
                    Item("Sulfuras, Hand of Ragnaros", sell_in, 80)
                    for sell_in in range(-10, 10)
                ]
            ])


# 2024-12-24 Continue
# code is stashed locally but not pushed to remote
# TODO:
# looks like I'm on track to figuring this out
# add other item names, sell and quality
# Look to Java approvals for what values I used there
# See Win11 downloads folder for AI exmaple that seems close

    def test_multiple_items_via_combinations(self):
        item_names     = ["normal item", "Aged Brie"]
        sell_in_values = [ 0, 10, 20 ]
        quality_values = [ 0, 5, 10 ]
        # for sell_in_values in range(-5, 10)   - can I make this work?

        def update_single_item(name, sell_in, quality):
            items = [Item(name, sell_in, quality)]
            sut = GildedRose(items)
            sut.update_quality()
            output = f"{items[0].name} {items[0].sell_in} {items[0].quality}"
            return output

        verify_all_combinations(update_single_item, [item_names, sell_in_values, quality_values])

