import numpy as np


def get_cost(store_infos):
    if len(store_infos) == 1:
        return store_infos[0]
    cost(store_infos)
    cost_sorted_stores = sorted(store_infos, key=lambda x: x['cost'], reverse=False)
    return cost_sorted_stores[0]


def cost(store_info):
    # store_info - availability, prices, distance, hour_intensity (-2 to 2)
    # Availability - Proportion of items available at the store
    # Prices - Total cost of the available items at the store
    # Distance
    # Hour_intensity - -2 is not much traffic, 2 is a lot of traffic

    theta = np.array([0.1, 0.1])
    distance_standardized = least_square(store_info, "distance")
    hour_intensity_standardized = least_square(store_info, "hour_intensity")
    for n in range(len(store_info)):
        X = np.array([distance_standardized[n], hour_intensity_standardized[n]])
        cost = np.dot(theta, X)
        store_info[n]['cost'] = cost
    return store_info


def least_square(store_info, search_term):
    vector = np.array([float(store[search_term]) for store in store_info])
    mean = sum(vector) / len(vector)
    width = max(vector) - min(vector)
    if width == 0:
        zero_array = []
        for n in range(4):
            zero_array.append(0)
        return zero_array
    return (vector - mean) / width


# print(get_cost([
#     {'name': 'Walmart Supercenter',
#      'address': '9218 FL-228, Macclenny, FL 32063, USA',
#      'distance': '100',
#      'availability': '0.4',
#      'prices': '404',
#      'hour_intensity': 2
#      }, {'name': 'Walmart Neighborhood',
#      'address': '9218 FL-228, Macclenny, FL 32063, USA',
#      'distance': '3',
#      'availability': '1.0',
#      'prices': '3',
#      'hour_intensity': -2
#      }]
# ))
