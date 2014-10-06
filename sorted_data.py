# import collections

entries = {}

with open("scores.txt") as file:
    for line in file:
        stripped_line = line.strip()
        restaurant_entry = stripped_line.split(":")
        restaurant, score = restaurant_entry
        entries[restaurant] = int(score)


# sorted_entries = collections.OrderedDict(sorted(entries.items()))
# for restaurant, rating in sorted_entries.items():
#     print "Restaurant %r is rated at %d" % (restaurant, rating)


for restaurant in sorted(entries):
    print "Restaurant %r is rated at %d" % (restaurant, entries[restaurant])
