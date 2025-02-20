# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

dm = 10
dk = dm * 1.6
t = (30 * 60 + 30) / (60 * 60)

speed = dk / t

print("Average speed =", speed, "km/hr")
print("Which is ridiculously fast.")

bolt_dk = 100 / 1000
bolt_t = 9.58 / (60 * 60)
bolt_speed = bolt_dk / bolt_t

print("Usain Bolt runs at", bolt_speed, "km/hr. For 100m only.")

kip_dk = 42.195
kip_t = (60 * 60 * 1 + 59 * 60 + 40.2) / (60 * 60)
kip_speed = kip_dk / kip_t

print("Eluid Kipchoge averaged", kip_speed, "for WR marathon.")
