from dataclasses import dataclass
from magic_list import MagicList


def main():
    print("Hello World!")

    magic_list1 = MagicList()
    magic_list1[0] = 4
    magic_list1[1] = 5
    print(magic_list1)

    magic_list2 = MagicList(cls_type=Person)
    magic_list2[0].age = 4
    magic_list2[1].age = 5
    print(magic_list2)


@dataclass
class Person:
    age: int = 1


if __name__ == "__main__":
    main()
