# By Aysin Oruz
# lifesum test code

# Import required libraries
import requests
import pprint
from collections import *

# Use pretty print to make it more readable
pp = pprint.PrettyPrinter(indent=2)


# Make the API call
def download_food_stats(offset=None):
    params = {'offset': offset}
    r = requests.get('https://api.lifesum.com/v1/foodipedia/foodstats', params=params)
    return r.json()


def count_ids(items, key):
    """
        This function counts the provided food/food category ids.
        """
    ids_to_count = {}

    for item in items:
        id = item[key]

        if id in ids_to_count:
            ids_to_count[item[key]] += 1
        else:
            ids_to_count[item[key]] = 1
    return ids_to_count


data = download_food_stats()
food_ids = count_ids(data['response'], 'food_id')
food_category_ids = count_ids(data['response'], 'food__category_id')

print "Please wait for a few minute..."

for i in xrange(150):
    data = download_food_stats(data['meta']['next_offset'])
    food_ids.update(count_ids(data['response'], 'food_id'))
    food_category_ids.update(count_ids(data['response'], 'food__category_id'))

ids_food_category = Counter(food_category_ids).most_common(n=5)
ids_food = Counter(food_ids).most_common(n=100)


print 'Top 5 Food Category IDs' \
      '\n-----------------------'
pp.pprint(ids_food_category)

print '\nTop 100 Food IDs'\
      '\n----------------'
pp.pprint(ids_food)




