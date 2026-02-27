class Springbreak:

    __DEFAULT_CAPACITY = 4

    def __init__(self, capacity=__DEFAULT_CAPACITY):
        self.__storage = [None] * capacity
        self.__capacity = capacity
        self.__current_count = 0

    def count(self):
        return self.__current_count

    def add_item(self, item):
        """BAD CODE
        # is there room for another item?
        if self.__current_count < self.__capacity:
            self.__storage[self.__current_count] = item
            self.__current_count += 1
        else:
            # create a larger object
            larger_object = [None] * (2*len(self.__storage))
            # move the contents of __storage to larger object
            for i in range(self.__current_count):
                larger_object[i] = self.__storage[i]
            self.__storage = larger_object
            self.add_item(item)
        """
        # GOOD CODE
        if self.__current_count == self.__capacity:
            # No room... Let's make some more room
            larger_object = [None] * (2 * self.__capacity)
            # copy existing contents to larger object
            for i in range(self.__current_count):
                larger_object[i] = self.__storage[i]
        # By the time the code gets to this line, we are 100%
        # certain there is room for a new item
        self.__storage[self.__current_count] = item
        self.__current_count += 1
