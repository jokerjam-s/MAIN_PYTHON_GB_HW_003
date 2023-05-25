# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from ctypes.wintypes import tagMSG

THINGS_DICT = {"fork": 1,
               "spoon": 1,
               "water": 3,
               "boots": 3,
               "jacket": 5,
               "camera": 4,
               "teapot": 3,
               "tent": 8,
               "food": 5,
               "jeans": 4,
               "socks": 1,
               }


# "глупый" рюкзак - забирает вещи пока есть место,
# по принципу - хватай больший
def bag_dummy(things: dict[str, int], bag_volume: int) -> dict[str, int]:
    tmp_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))
    bag_dict = {}
    total_volume = 0
    # пока не наполнен рюкзак
    for t in tmp_dict.items():
        if (total_volume + t[1]) <= bag_volume:
            bag_dict[t[0]] = t[1]
            total_volume += t[1]
    return bag_dict


# "умный" рюкзак - старается взять как можно больше вещей
# all_solution - вернуть все возможные решения если True
# иначе - наиболее оптимальное
# результат словарь key - размер, set - перечень предметов
def bag_smart(things: dict[str, int], bag_volume: int, all_solution=False) -> dict[int, list]:
    bag_dict: dict[int, list] = {}
    for t in things.items():
        for b in bag_dict.items():
            if b[0] + t[1] <= bag_volume:
                bag_dict[b[0] + t[1]] = [x.append(t[0]) for x in b[1]]
        bag_dict.setdefault(t[1], []).append(list(t[0]))

    return bag_dict

def main():
    print(THINGS_DICT)
    print(bag_dummy(THINGS_DICT, 15))
    print(bag_smart(THINGS_DICT, 15))

if __name__ == "__main__":
    main()
