import unittest

from gilded_rose import Item, GildedRose
from approvaltests import verify, verify_all_combinations


class TestApprovals(unittest.TestCase):
    def test_single_item(self):
        items = [Item("normal item", 10, 5)]
        sut = GildedRose(items)

        # Act
        sut.update_quality()
        actual_updated_item = items[0]

        # Assert
        verify(actual_updated_item)


# 2024-12-24 Continue
# code is stashed locally but not pushed to remote
# TODO:
# Right now the combinations are being generated but no

    def test_multiple_items_via_combinations(self):
        item_names     = ["normal item", "Aged Brie"]
        sell_in_values = [ 0, 10, 20 ]
        quality_values = [ 0, 5, 10 ]

        def update_single_item(name, sell_in, quality):
            items = [Item(name, sell_in, quality)]
            sut = GildedRose(items)
            sut.update_quality()
            output = f"{items[0].name} {items[0].sell_in} {items[0].quality}"
            return output

        verify_all_combinations(update_single_item, [item_names, sell_in_values, quality_values])