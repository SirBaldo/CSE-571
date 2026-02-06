import matplotlib.pyplot as plt
import numpy as np

factors = [0.01, 0.03, 0.1, 0.3, 1.0]

mean_traj = [5.2847, 5.5751, 7.9622, 13.1556, 17.5371]
std_traj  = [3.3956, 4.2598, 4.9336, 7.3646, 13.9424]

mean_map = [6.5286, 7.1481, 9.7224, 16.0494, 21.7017]
std_map  = [4.4364, 5.3671, 5.8115, 9.5897, 18.0817]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.errorbar(factors, mean_traj, yerr=std_traj, marker='o', capsize=5, linewidth=2)
ax1.set_xlabel('Noise Factor (data = filter)')
ax1.set_ylabel('Mean Position Error')
ax1.set_title('Robot Position Error vs Noise Factor')
ax1.set_xscale('log')
ax1.grid(True, alpha=0.3)

ax2.errorbar(factors, mean_map, yerr=std_map, marker='s', capsize=5, linewidth=2, color='orange')
ax2.set_xlabel('Noise Factor (data = filter)')
ax2.set_ylabel('Mean Marker Error')
ax2.set_title('Landmark Error vs Noise Factor')
ax2.set_xscale('log')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ekf_slam_part_b.png', dpi=150, bbox_inches='tight')
plt.show()