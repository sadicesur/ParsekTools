# =============================================================================
# SUTHERLAND'S VISCOSITY MODEL
# =============================================================================

# Reference Properties

v_ref = 1.716e-5 # the viscosity in kg/m-s
t_ref = 273.15
s_ref = 110.4 # an effective temperature in K (Sutherland constant)

def suther(temp):
    
    return v_ref * (temp/t_ref)**1.5 * ((t_ref + s_ref)/(temp + s_ref)) 