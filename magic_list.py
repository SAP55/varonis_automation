class MagicList:
    """
    Class that implements a simplified list by skipping boundary checks when possible.
    """
    def __init__(self, cls_type=None):
        """
        Init method
        :param cls_type: Object assigned types
        """
        super(MagicList, self).__init__()

        self._list = []

        if cls_type is not None:
            self.cls_type = cls_type

    def __len__(self):
        return len(self._list)

    def __getitem__(self, item):
        if item not in self._list:
            self._list.append(self.cls_type())

        return self._list[item]

    def __setitem__(self, item, val):
        if item in self._list:
            self._list[item] = val
        else:
            self._list.append(val)

    def __str__(self):
        return str(self._list)

    def insert(self, item, val):
        self._list.insert(item, val)

    def append(self, val):
        self.insert(len(self._list), val)
