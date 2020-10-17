def get_cost(store_infos):
    store_infos = map(cost, store_infos)

    # sort(store_infos, cost)
    return store_infos[0]


def cost(store_info):
    # store_info - availability, prices, distance, hour_intensity (-2 to 2)

    store_info['cost'] = cost
    return store_info