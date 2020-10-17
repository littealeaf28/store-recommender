import numpy as np


def get_cost(store_infos):
    store_infos = list(map(cost, store_infos))
    cost_sorted_stores = sorted(store_infos.items(), key=lambda x: x['cost'], reverse=False)

    return cost_sorted_stores[0]


def cost(store_info):
    # store_info - availability, prices, distance, hour_intensity (-2 to 2)
    # Availability - Proportion of items available at the store
    # Prices - Total cost of the available items at the store
    # Distance
    # Hour_intensity - -2 is not much traffic, 2 is a lot of traffic

    theta = np.array([0.25, 0.25, 0.25, 0.25])
    X = np.array([least_square(store_info, "availability"), least_square(store_info, "prices"),
                  least_square(store_info, "distance"), least_square(store_info, "hour_intensity")])
    cost = np.dot(theta, X)
    store_info['cost'] = cost
    return store_info


def least_square(store_info, search_term):
    vector = np.array(store_info[search_term])
    mean = sum(vector) / len(vector)
    range = max(vector) - min(vector)
    return (vector - mean) ^ 2 / range
