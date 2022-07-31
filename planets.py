# Graphically represent the planets in the Solar System, with their radius and distance from the sun. 
# All units in km / AU.

# Import block
import matplotlib.pyplot as plt

# Variables

# Conversions
d_au = 151000000 # 1 AU, km
# Radii 
r_sun = 696340 / d_au 
r_earth = 6371  / d_au 
r_moon = 1737 / d_au
r_jupiter =  69911 / d_au
# Distances
d_sun_earth = 151000000 / d_au # 1 AU
d_earth_moon = 386242 / d_au 
d_sun_moon = d_sun_earth + d_earth_moon
d_sun_jupiter =  742150000 / d_au

# Plotting
figure, axes = plt.subplots()
# Create our planets
# TODO: Add more colors?
drawing_sun = plt.Circle( (0,0), r_sun, color = 'r')
drawing_earth = plt.Circle( (d_sun_earth, 0 ), r_earth, color = 'b')
drawing_moon = plt.Circle( (d_sun_moon, 0 ), r_moon, color = 'g')
drawing_jupiter = plt.Circle( (d_sun_jupiter, 0 ), r_jupiter, color = 'r')
# Add to drawing
axes.add_artist(drawing_sun)
axes.add_artist(drawing_earth)
axes.add_artist(drawing_moon)
axes.add_artist(drawing_jupiter)
#Set axis limits
axes.set_xlim([- d_sun_earth / 4 , d_sun_earth * 6])
axes.set_ylim([- d_sun_earth / 4, d_sun_earth / 4])
axes.set_aspect(1)
# Plot
plt.axis('scaled')
plt.title( 'The Solar System' )
plt.show()