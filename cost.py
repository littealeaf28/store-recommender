def get_cost(store_infos):
    store_infos = map(cost, store_infos)

    # sort(store_infos)
    return "An optimal store, or some stats about the optimality of each store\
               to be interpreted later? "


def cost(store_info):

    store_info['cost'] = cost
    return store_info