from item_finder import cost_calculate


def add_availability(store_info, availability):
    store_info['availability'] = availability
    return store_info


def add_prices(store_info, prices):
    store_info['prices'] = prices
    return store_info


def get_availabilities_and_prices(store_infos, shopping_list):
    availabilities = []
    costs = []
    for store in store_infos:
        availability_and_cost = cost_calculate(store['address'], shopping_list)
        availabilities.append(availability_and_cost[0])
        costs.append(availability_and_cost[1])

    store_infos = list(map(add_availability, store_infos, availabilities))
    store_infos = list(map(add_prices, store_infos, costs))
    return store_infos