import numpy as np
import matplotlib.pyplot as plt

from solar_position_algorithm import SPA

# Load the SPA class
spa = SPA()



# * omega is the slope of the surface measured from the horizontal plane.
# * gamma is the surface azimuth rotation angle, measured from south to the
# projection of the surface normal on the horizontal plane, positive or negative 
# if oriented west or east from south, respectively.
omega_angle = 0.0  # degrees
gamma_angle = 15.0  # degrees

# Latitude and longitude for College Station, TX
cs_lat = 30.622370
cs_long = -96.325851
elevation = 103.0  # meters above sea level

def inc_ang(day, month=4, year=2022):
    return spa.incidence_angle(omega_angle, gamma_angle, year, month, day,
                                cs_lat, cs_long, elevation)


# Plot the incidence angles as a function of time of day
days = np.linspace(11,12,200)
inc_angles = np.array([inc_ang(day) for day in days])

plt.plot(days, inc_angles)
plt.ylabel("Incidence Angle (radians)")
plt.xlabel("Day (of April 2022)")
plt.show()
plt.close()


