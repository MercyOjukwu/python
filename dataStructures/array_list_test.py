import unittest

from dataStructures import array_list


class ArrayListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.arrayList = array_list.ArrayList()

    def test_that_object_exists(self):
        self.assertIsInstance(self.arrayList, array_list.ArrayList)

    def test_that_arraylist_can_be_added_to(self):
        self.arrayList.add("Mango")
        self.assertEquals(1, self.arrayList.size)

    # def test_that_multiple_elements_can_be_addedToList(self):
    #     self.arrayList.add("Mango")
    #     self.arrayList.add("Orange")
    #     self.arrayList.add("Pear")
    #     self.assertEquals(4, self.arrayList.size)

    # def test_that_element_can_beRemovedFromList(self):
    #     self.arrayList.add("Mango")
    #     self.arrayList.add("Orange")
    #     self.arrayList.add("Pear")
    #     self.arrayList.remove("Pear")
    #     self.assertEquals(2, self.arrayList.size)


if __name__ == '__main__':
    unittest.main()
