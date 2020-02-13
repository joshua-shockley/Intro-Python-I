"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
for points in waypoints:
    print(points)

waypoints.extend([{"lat": 40, "lon": -110, "name": "yet another place"}])


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
# for points in waypoints:
#     print(points)

# waypoints[0].update({"lon": -130, "name": "not a real place"})
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for points in waypoints:  # this way is wrong way to get what i wanted from instructions
    print("values: ", points.values())
    print("keys: ", points.keys())

for points in waypoints:  # above is a list of dictionaries so first for loop throught the list to enter the dict and then use the .items() to pull out k&v from the dict
    for k, v in points.items():  # can't use .items() on a list so it goes here once into the list and accessing the dict
        print("the k&v:", k, v)
