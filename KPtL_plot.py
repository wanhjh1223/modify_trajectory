import numpy as np
import fitmodel as Model
import matplotlib.pyplot as plt

# curr_kptl_to_left_time = [-0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.0499999, 0]
# curr_kptl_to_left_data = [0.895657, 0.895419, 0.903008, 0.881629, 0.905715, 0.908594, 0.879598, 0.853757, 0.888359, 0.882916, 0.897063, 0.913203, 0.846841, 0.830689, 0.863662, 0.839596, 0.828381]
# curr_kptl_to_right_data = [0.141745, 0.147528, 0.14193, 0.14854, 0.130191, 0.113456, 0.124093, 0.12737, 0.120114, 0.123678, 0.11144, 0.112865, 0.0957938, 0.0554736, 0.0872025, 0.0778565, 0.0979865]
# left_kb = [0.836963, -0.0799495]
# rightt_kb = [0.0775529, -0.0777271]

# curr_kptl_to_left_time = [-0.95, -0.9, -0.85, -0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.0499999, 0]
# curr_kptl_to_left_data = [-0.315686, -0.311967, -0.30247, -0.292706, -0.305711, -0.277296, -0.272531, -0.271763, -0.26185, -0.27086, -0.255072, -0.245939, -0.249363, -0.223494, -0.228573, -0.201684, -0.220387, -0.197696, -0.205791, -0.195759]
# curr_kptl_to_right_data = [-2.18997, -2.17489, -2.16484, -2.1488, -2.15084, -2.1472, -2.13905, -2.14713, -2.13537, -2.145, -2.11719, -2.12061, -2.12616, -2.11411, -2.10621, -2.09993, -2.09977, -2.07933, -2.06137, -2.06343]
curr_kptl_to_left_time = [-0.7, -0.65, -0.6, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.0500001, 0]
curr_kptl_to_left_data = [0.815522, 0.790387, 0.787599, 0.75598, 0.72336, 0.71354, 0.680944, 0.689293, 0.698757, 0.641999, 0.63697, 0.647165, 0.624022, 0.59314]
curr_kptl_to_right_data = [0.19113, 0.18046, 0.177725, 0.168913, 0.137583, 0.145296, 0.131294, 0.118606, 0.129117, 0.108774, 0.104816, 0.114318, 0.0968585, 0.0833217]

# historyData_x = [ x * 0.1 - 1.0 for x in range(1, 11)]
# historyData_ly = kptlToLeft[0:10]
# historyData_Ry = kptlToRight[0:10]
historyData_x = curr_kptl_to_left_time
historyData_ly = curr_kptl_to_left_data
historyData_Ry = curr_kptl_to_right_data
poly1 = Model.LeastSquarePolyFit(historyData_x, historyData_ly, 4, 2)
poly2 = Model.LeastSquarePolyFit(historyData_x, historyData_Ry, 4, 2)


x1 = np.arange(-1.2, 1.5, 0.01)
l_y = poly1[0] + poly1[1] * x1
R_y = poly2[0] + poly2[1] * x1

pred_ly = poly1[0] + poly1[1] * 1.0
pred_ry = poly2[0] + poly2[1] * 1.0

level = x1 * 0.0

plt.figure()
plt.title('kptlPred')
plt.xlim((-1.2, 1.5))
plt.ylim((-1.2, 3))
plt.scatter(historyData_x, historyData_ly, s = 8, label='Left_historyData', marker='o')
plt.scatter(historyData_x, historyData_Ry,  s = 8,label='Right_historyData', marker='o')
# plt.scatter(1.0, pred_ly,s = 8, marker = '^')
# plt.scatter(1.0, pred_ry,s = 8, marker = '^')

plt.plot(x1, l_y, linewidth = '1.0', label='toEgoLeft')
plt.plot(x1, R_y, linewidth = '1.0', label='toEgoRight')
#plt.plot(x1, level, label = 'level')

plt.plot([-1.2,1.5],[0.0,0],color = 'black', linewidth = '0.5',linestyle = 'dashed')
plt.plot([1.0,1.0],[-1.2,3], color = 'black', linewidth = '0.5',linestyle = 'dashed')
plt.legend(['Left_historyData', 'Right_historyData', 'toEgoLeft', 'toEgoRight'])
# print(curr_kptl_to_left_time[1],curr_kptl_to_left_time[-1])
# plt.plot([curr_kptl_to_left_time[0],curr_kptl_to_left_time[-1]],[left_kb[1] * curr_kptl_to_left_time[0] + left_kb[0],left_kb[1] * curr_kptl_to_left_time[-1] + left_kb[0]],color = 'black', linewidth = '0.5',linestyle = 'dashed')

# plt.plot(x1, y3, label='mixpoly')
# plt.savefig('./picture/kptl_pred.png')
plt.show()



