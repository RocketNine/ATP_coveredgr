import unittest

from gilded_rose import Item, GildedRose
from approvaltests import verify

class TestApprovals(unittest.TestCase):
    def test_single_item(self):
        items = [Item("normal item", 10, 5)]
        sut = GildedRose(items)

        # Act
        sut.update_quality()
        actual_updated_item = items[0]

        # Assert
        verify(actual_updated_item)
