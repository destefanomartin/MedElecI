# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:40:11 2022

@author: Deste
"""

import numpy as np 
import math as m 


Ra_media = 19.965 
Ra_tipo_a = 0.00223607
Ra_tipo_b = 0.0979879
Ra_inc = m.sqrt(Ra_tipo_a**2+Ra_tipo_b**2)

Rb_media = 19.768
Rb_tipo_a = 0.00133333
Rb_tipo_b = 0.097078
Rb_inc = m.sqrt(Rb_tipo_a**2+Rb_tipo_b**2)

Vf_media = 3.967 
Vf_tipo_a = 0.00152753
Vf_tipo_b = 0.012091
Vf_inc = m.sqrt(Vf_tipo_a**2+Vf_tipo_b**2)

dv_dvf = Rb_media/(Ra_media+Rb_media)
dv_dra = -Rb_media*Vf_media/(Ra_media+Rb_media)**2
dv_drb = Vf_media/(Ra_media+Rb_media)-Rb_media*Vf_media/(Ra_media+Rb_media)**2 

inc_comb = m.sqrt(dv_dra**2*Ra_inc**2+dv_dvf**2*Vf_inc**2+dv_drb**2*Rb_inc**2)
inc_exp = 2*inc_comb