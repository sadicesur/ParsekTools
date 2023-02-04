# =============================================================================
# ISA ATHMOSPHERIC CALCULATOR
# =============================================================================
import numpy as np

def atmosisa(h = 0,
             unit = "SI"):
    
    if unit != "SI":
        h = h*0.3048
    else:
        h = h
    
    t0   = 288.15   # Reference temperature [K]
    t11  = 216.65   # Reference temperature @ h = 11 km [K]
    p0   = 101325   # Reference pressure [Pa]
    p11  = 22632    # Reference pressure @ h = 11 km [K]
    g0   = 9.80665  # Reference gravitational acceleration [m/s2]
    r0   = 6.3781E6 # Radius of Earth [m]
    R    = 287.04   # Gas Constant
    gama = 1.4      # Specific Heat Ratio
    
    g  = g0*(1-2*h/r0)
    t  = t0 - 6.5*h/1000
    
    if h <= 11000:
    
        p = p0*(1-0.0065*(h/t0))**5.2561
        
    else:
        
        p = p11*np.exp(-g*(h-11000)/(R*t11))
    
    rho = p/(R*t)
    a   = np.sqrt(gama*R*t)
    
    return p, t, rho, a, g