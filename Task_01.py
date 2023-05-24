# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# список для обработки
WORKING_LIST_1 = [1, 1, 2, 3, "F", "T", "F", 3, "o", "0", 0]
WORKING_LIST_2 = [1, 2, 3, 4, "F", "K", "X", "X", "0", 0, 8]


# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")
    print(f"{WORKING_LIST_2} - {double_items(WORKING_LIST_2)}")


if __name__ == "__main__":
    main()
