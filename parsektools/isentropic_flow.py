# =============================================================================
# ISENTROPIC FLOW RELATIONS
# =============================================================================

# Constants

R    = 287.04   # Gas Constant
gama = 1.4      # Specific Heat Ratio

def ptot(p, m):
    
    return p*(1+0.5*(gama-1)*m**2)**(gama/(gama-1))

def ttot(t, m):
    
    return t*(1+0.5*(gama-1)*m**2)
    
def rhot(rho, m):
    
    return rho*(1+0.5*(gama-1)*m**2)**(1/(gama-1))