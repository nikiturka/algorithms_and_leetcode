def select_stations(states_needed, stations):
    final_stations = set()

    while states_needed:  # Пока есть штаты, которые нужно покрыть
        best_station = None
        states_covered = set()

        # Поиск радиостанции, которая покрывает наибольшее количество незакрытых штатов
        for station, states in stations.items():
            covered = states_needed & states  # Находим штаты, которые покрывает текущая радиостанция
            if len(covered) > len(states_covered):  # Если покрывает больше штатов
                best_station = station
                states_covered = covered

        # Удаляем покрытые штаты из списка необходимых
        if best_station is not None:
            final_stations.add(best_station)
            states_needed -= states_covered  # Удаляем покрытые штаты

    return final_stations


# Штаты, которые нужно покрыть
all_states_needed = {"Калифорния", "Орегон", "Вашингтон", "Невада", "Аризона", "Юта"}

# Радиостанции и их покрытия
all_stations = {
    "Радиостанция 1": {"Калифорния", "Орегон"},
    "Радиостанция 2": {"Орегон", "Вашингтон"},
    "Радиостанция 3": {"Невада"},
    "Радиостанция 4": {"Аризона"},
    "Радиостанция 5": {"Юта", "Невада"},
}

# Запускаем функцию
selected = select_stations(all_states_needed, all_stations)

# Выводим результаты
print("Выбранные радиостанции:", selected)
