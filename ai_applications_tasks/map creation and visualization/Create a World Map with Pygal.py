#install the packages
!pip install pygal
!pip install pygal_maps_world

# Import the World class from the correct module
from pygal_maps_world.maps import World
from IPython.display import SVG

# Create a world map
worldmap = World()

# Set the title of the map
worldmap.title = 'Countries'

# Adding the countries
worldmap.add('Random Data', {
    'aq': 10,
    'cd': 30,
    'de': 40,
    'eg': 50,
    'ga': 45,
    'hk': 23,
    'in': 70,
    'jp': 54,
    'nz': 41,
    'kz': 32,
    'us': 66
})

# Save the map as SVG
worldmap.render_to_file('abc.svg')
print("Success")
# Display the map directly in the notebook
SVG(filename='abc.svg')
