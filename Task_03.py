# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from ctypes.wintypes import tagMSG
import copy

# Словарь вещей
THINGS_DICT = {"вилка": 1,
               "ложка": 1,
               "вода": 3,
               "ботинки": 3,
               "куртка": 5,
               "камера": 4,
               "чайник": 4,
               "палатка": 12,
               "еда": 5,
               "джинсы": 4,
               "посуда": 2,
               }
# Размер рюкзака
BAG_SIZE = 5


def bag_pack(things: dict[str, int], bag_volume: int, mode_greed=True) -> list[int | set]:
    """'Жадный' или 'Щедрый' рюкзак - забирает вещи пока есть место.
    В жадном режиме заполняет начиная с вещей от большего веса к меньшему,
    в щедром - наоборот, заполнение ведется от вещей с наименьшим весом.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    :mode_greed: режим работы True - жадный, False - щедрый
    """
    tmp_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=mode_greed))
    things_list: [int | set] = [0, set()]  # первый элемент - занятый размер, остальное - уложенные вещи
    # пока не наполнен рюкзак
    for t_key, t_val in tmp_dict.items():
        if (things_list[0] + t_val) <= bag_volume:
            things_list[1].add(t_key)
            things_list[0] += t_val

    return things_list


def bag_all_pack(things: dict[str, int], bag_volume: int) -> list:
    """Поиск всех вариантов упаковки.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    """
    bag_list: list[list[int | set]] = []
    best_case = 0
    # отобрать только подходящие вещи
    for t_key, t_val in things.items():
        # пропустить - если вещь не влазит в рюкзак
        if t_val <= BAG_SIZE:
            tmp_list = []
            for x in bag_list:
                # пропустить, если добавление невозможно к существующему набору
                weight = x[0] + t_val
                if bag_volume >= weight and not x[1].issubset(t_key):
                    y: list[int | set] = copy.deepcopy(x)
                    y[0] += t_val
                    y[1].add(t_key)
                    tmp_list.append(y)
                    if weight > best_case:
                        best_case = weight
            if len(tmp_list):
                for t in tmp_list:
                    bag_list.append(t)
            if bag_volume >= t_val:
                bag_list.append([t_val, {t_key}])
                if t_val > best_case:
                    best_case = t_val

    bag_list = list(filter(lambda b: b[0] == best_case, bag_list))
    return bag_list


def print_bag(bag: list[int | set]):
    """Вывод содержимого рюкзака."""
    for x in bag:
        if isinstance(x, int):
            print(f"Взято {x}", end=" | ")
        else:
            print(f"{x}")


def main():
    print(f"Размер рюкзака - {BAG_SIZE}")
    print("Перечень вещей:")
    print(THINGS_DICT)
    print("Жадный алгоритм:")
    print_bag(bag_pack(THINGS_DICT, BAG_SIZE))
    print()
    print("Щедрый алгоритм:")
    print_bag(bag_pack(THINGS_DICT, BAG_SIZE, False))
    print()
    print("Все наилучшие варианты:")
    for x in bag_all_pack(THINGS_DICT, BAG_SIZE):
        print_bag(x)


if __name__ == "__main__":
    main()
