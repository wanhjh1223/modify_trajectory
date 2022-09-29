import numpy as np
import matplotlib.pyplot as plt


final_t = 4
vel = 8.72895
pos = 126.294

############### NEW ######################
a2 = vel
a3 = pos
final_pos = pos + 20

a0 = (final_pos - vel * final_t - pos) / (-2 * final_t * final_t * final_t)
a1 = (3 * (final_pos - vel * final_t - pos)) / (2 * final_t * final_t)

s = a0 * pow(final_t,3) + a1 * pow(final_t,2) + a2 * pow(final_t,1) + a3
print(a0, a1, a2, a3, s, 6 * a0 * final_t + 2 * a1)

################ old #####################
A2 = vel
A3 = pos

A0 = (final_t * 0 - vel + vel) / (3 * final_t * final_t)
A1 = 0.5 * (0 - 6 * A0 * final_t)

S = A0 * pow(final_t,3) + A1 * pow(final_t,2) + A2 * pow(final_t,1) + A3
print(A0, A1, A2, A3, S, 6 * A0 * final_t + 2 * A1)

################ plot ####################
x = np.arange(0,final_t,0.1)
y1 = a0 * pow(x,3) + a1 * pow(x,2) + a2 * pow(x,1) + a3
y2 = A0 * pow(x,3) + A1 * pow(x,2) + A2 * pow(x,1) + A3
plt.figure()
plt.subplot(1,3,1)
plt.plot(x, y1, label='new_pos')
plt.plot(x, y2, label='old_pos')
plt.legend(['new','old'])
plt.axis('square')
plt.subplot(1,3,2)
plt.plot(x, 3 * a0 * x * x + 2 * a1 * x + a2, label='new_vel')
plt.plot(x, 3 * A0 * x * x + 2 * A1 * x + A2, label='old_vel')
plt.legend(['new_vel','old_vel'])
plt.axis('square')
plt.subplot(1,3,3)
plt.plot(x, 6 * a0 * x + 2 * a1, label='new_acc')
plt.plot(x, 6 * A0 * x + 2 * A1, label='old_acc')
plt.legend(['new_acc','old_acc'])
plt.axis('square')
plt.show()
