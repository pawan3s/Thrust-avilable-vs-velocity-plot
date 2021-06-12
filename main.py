from numpy import pi
import matplotlib.pyplot as plt

# Functions
def knots_to_ftpersec(speed):
    return speed * 1.68781

def thrust_required(rho_inf, v_inf, s, cd0_, k, w):
    cl = 2 * w / (rho_inf * v_inf ** 2 * s)
    return 0.5 * rho_inf * v_inf ** 2 * s * (cd0_ + k * cl ** 2)

# Inputs
weight = 200000  # lb
wing_area = 1318  # ft^2
wing_span = 117.416666667  # ft
cd0 = 0.0185
thrust = 66000  # lb of thrust total
aspect_ratio = wing_span**2 / wing_area
e = 0.92
K = 1 / (pi * e * aspect_ratio)
rho_sl = 23.77E-4  # in slugs/ft^3

x_vals_sl = [i for i in range(80, 750, 10)]

tr_sl = [thrust_required(rho_sl, knots_to_ftpersec(x), wing_area, cd0, K, weight) for x in x_vals_sl]


# Sea Level

plt.plot(x_vals_sl, tr_sl, 'k-', label=r"$T_R$ at Sea Level")
TA_sl = 0.7 * thrust
y_coords_sl = [TA_sl for _ in x_vals_sl]
takeoff_vel_sl = [180, 180]
cruise_velocity_sl_values = [11000, 46500]

plt.plot(x_vals_sl, y_coords_sl, 'k--',
          label='$T_A$ at Sea Level ({:,.0f} lb)'.format(TA_sl))

plt.plot(takeoff_vel_sl, cruise_velocity_sl_values, 'b-.',
         label="Takeoff Velocity ({} knots)".format(takeoff_vel_sl[0]))
plt.ylim(5000, 50000)
plt.xlim(50, 1550)
plt.ylabel('Thrust (lb)')
plt.xlabel('Velocity (kts)')
plt.title('Thrust Required & Thrust Available Curves')
plt.legend(loc='lower right')
#plt.show()
plt.savefig("output/chap2_1.png")
