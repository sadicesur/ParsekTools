# =============================================================================
# SHOCK RELATIONS
# =============================================================================

from parsektools.isa_athmosphere import *
from parsektools.isentropic_flow import *

gama = 1.4

def normal_shock(h, m):
    
    [p0, t0, rho0, a0, g0] = atmosisa(h, "SI")
    
    
    p1   = p0*((2*gama*m**2-(gama-1))/(gama+1))
    pt1  = ptot(p0, m) * (((gama+1)*m**2 / ((gama-1)*m**2 +2))**(gama/(gama-1))) * \
           ((gama+1)/(2*gama*m**2 - (gama-1)))**(1/(gama-1)) 
          
    t1   = t0 * (2*gama*m**2 - (gama-1)) * ((gama-1)*m**2 +2) / (gama+1)**2 / m**2
    tt1  = ttot(t0, m)
    
    rho1 = rho0 * ((gama+1)*m**2) / ((gama-1)*m**2 + 2)
    
    m1   = np.sqrt(((gama-1)*m**2 +2) / (2*gama*m**2 -(gama-1)))
    
    return p1, pt1, t1, tt1, rho1, m1 