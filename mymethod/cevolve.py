#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[14]:


get_ipython().run_cell_magic('cython', '-a ', 'import numpy as np\ncimport numpy as np\ndef c_evolve(np.ndarray r_i,np.ndarray ang_speed_i,double timestep,int nsteps):\n    cdef np.ndarray v_i = np.empty_like(r_i)\n\n    for i in range(nsteps):\n        norm_i = np.sqrt((r_i**2).sum(axis = 1))\n\n        v_i = r_i[:,[1,0]]\n        v_i[:, 0] *= -1\n        v_i /= norm_i[:, np.newaxis]\n\n        d_i =timestep * ang_speed_i[:, np.newaxis] * v_i\n\n        r_i += d_i')


# In[ ]:




