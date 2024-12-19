import numpy as np
import matplotlib.pyplot as plt

def flux_surface(R0,A,theta,kappa,delta):
    """Calculate R_s and Z_s for flux surfaces
    
    Arguments
    ----------
    R0: original radius
    A: don't know
    theta: array from 0 to 2pi
    kappa: don't know either
    delta: yet another unknown variable
    """
    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    return R_s, Z_s

flux_surfaces=flux_surface(2.5,2.2,np.linspace(0,2 * np.pi),1.5,0.3)

def plot_surface(R_s,Z_s,savefig=True):
    """Create a plot of the flux surface with labelled axes for R_s against Z_s
    
    Arguments
    ---------
    R_s: major radius, calculated from flux_surfaces function
    Z_s: height, calculated from flux surfaces function
    savefig: Boolean, default is True, saves figure as miller.png"""
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig:
        plt.savefig("miller.png")

plot_surface(flux_surfaces[0],flux_surfaces[1])

