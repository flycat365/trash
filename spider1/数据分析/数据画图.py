# -*- coding: utf-8 -*-

import numpy as np
import  .pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)

cos = np.cos(x)
sin = np.sin(x)

plt.plot(x, cos, '--', linewidth=2)
plt.plot(x, sin)

plt.show()