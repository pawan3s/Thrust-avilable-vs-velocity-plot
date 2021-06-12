# Thrust-avilable-vs-velocity-plot

Here we try to get the graphical solution of different aerodynamic parameters by plotting the thrust available and thrust required vs the velocity(knots) for an Airbus A321 at sea level at level flight.

We use basic python libraries like NumPy and Matplotlib. The obtained graph gives us information on min and max velocities. Based on thiswe can analyse that whether flight is possible at min velocityor not after we compare it with stallling velocity analytically.
The conditions and we have used here is for level flight condition.The concept can also be employed to graph for other condition like climbing flight, turning flight. 

The basic principle at level flight at Thrust produced will be equal to drag. 

Following inputs have been taken for Airbus A321
weight = 200000  lb
wing_area = 1318 ft^2
wing_span = 117.416666667 ft
cd0 = 0.0185
thrust = 66000 lb of thrust total
aspect_ratio = wing_span**2 / wing_area
e = 0.92
K = 1 / (pi * e * aspect_ratio)
densitity at sea level = 23.77E-4 slugs/ft^3

SOurce: https://en.wikipedia.org/wiki/Airbus_A321
