# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from ctypes.wintypes import tagMSG
import copy
from typing import Dict, List

THINGS_DICT = {"fork": 1,
               "spoon": 1,
               "water": 3,
               "boots": 3,
               "jacket": 5,
               "camera": 4,
               "teapot": 4,
               "tent": 12,
               "food": 5,
               "jeans": 4,
               "socks": 1,
               }


# "жадный" рюкзак - забирает вещи пока есть место,
# по принципу - хватай самый большой, при этом может проигнорировать случай когда
# более мелкими предметами можно заполнить рюкзак более полно
def bag_dummy(things: dict[str, int], bag_volume: int) -> dict[int, list]:
    tmp_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))
    things_list: [str] = []
    total_volume = 0
    # пока не наполнен рюкзак
    for t_key, t_val in tmp_dict.items():
        if (total_volume + t_val) <= bag_volume:
            things_list.append(t_key)
            total_volume += t_val

    return {total_volume: things_list}


# "умный" рюкзак - старается взять как можно больше вещей
# all_solution - вернуть все возможные решения если True
# иначе - наиболее оптимальное
# результат словарь key - размер, set - перечень предметов
def bag_smart(things: dict[str, int], bag_volume: int, all_solution=False) -> dict[int, list]:
    bag_dict: dict[int, list[str]] = {}
    tmp_bag: dict[int, list[str]] = {}

    for t_key, t_val in things.items():
        tmp_dict = {}
        if len(tmp_bag):
            for x, y in tmp_bag.items():
                tmp = try_push_things({t_val, [t_key]}, {x, y})

        # if len(tmp_bag):
        #     tmp_dict = {}
        #     for b_key, b_val in tmp_bag.items():
        #         if b_key + t_val <= bag_volume:
        #             new_val = copy.deepcopy(b_val)
        #             for x in new_val:
        #                 x.append(t_key)
        #             tmp_dict[b_key + t_val] = new_val
        #     if len(tmp_dict):
        #         tmp_bag.update(tmp_dict)
        if t_val <= bag_volume:
            tmp_bag.setdefault(t_val, []).append([t_key])


    if all_solution:
        bag_dict = tmp_bag
    else:
        bag_dict = {x: y for x, y in tmp_bag.items() if x == max(tmp_bag.keys())}
    return bag_dict


# Проверка возможности укладки наборов в рюкзак
def try_push_things(things_1: dict[int, list[str]], things_2: dict[int, list], bag_size: int) -> dict[list[str]] | None:
    result = None
    if things_1[0] + things_2[0] <= bag_size:
        things_new = copy.deepcopy(things_1[1]).append(copy.deepcopy(things_2[1]))
        result = {things_1[0] + things_2[0]: things_new}
    return result


def main():
    print(THINGS_DICT)
    print(bag_dummy(THINGS_DICT, 7))
    print(bag_smart(THINGS_DICT, 7))


if __name__ == "__main__":
    main()
