# Install the required packages (if not already installed)
!pip install pygal
!pip install pygal_maps_world

# Import the World class from pygal_maps_world module
from pygal_maps_world.maps import World
from pygal.style import Style
from IPython.display import SVG

# Create a Style object with custom colors
custom_style = Style(colors=('#FF0000', '#0000FF', '#00FF00', '#000000', '#FFD700'))

# Create a world map using Worldmap() class
worldmap = World(style=custom_style)

# Set the title of the map
worldmap.title = 'Some Countries Starting from Specific Letters'

# Add the countries with their codes and respective colors
worldmap.add('"E" Countries', ['ec', 'ee', 'eg', 'eh', 'er', 'es', 'et'])
worldmap.add('"F" Countries', ['fr', 'fi'])
worldmap.add('"P" Countries', ['pa', 'pe', 'pg', 'ph', 'pk', 'pl', 'pr', 'ps', 'pt', 'py'])
worldmap.add('"Z" Countries', ['zm', 'zw'])
worldmap.add ('"A" Countries', ['ad', 'ae', 'af', 'al', 'am', 'ao', 'aq', 'ar', 'at', 'au', 'az'], color='black')

# Save the map as SVG
worldmap.render_to_file('abc.svg')
print("success")
# Display the map directly in the notebook
SVG(filename='abc.svg')
