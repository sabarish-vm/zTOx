import numpy as np
from classy import Class
from scipy.interpolate import interp1d
from scipy.integrate import quad
import pickle

lcdm = Class()
lcdm.set({'Omega_m' : 0.3153, 'Omega_Lambda' : 0.6847,'h':0.6736})
lcdm.compute()
bg=lcdm.get_background()

z_interp = np.hstack((
        np.linspace(0,1,int(1e4)),
        np.linspace(1.0001,10,int(1e4)),
        np.linspace(10.0001,1e2,int(1e5)),
        np.linspace(1.0001e2,1e5,int(1e6))
         ))
Rh = np.zeros_like(z_interp)

mydata1 = {
"age": interp1d(bg['z'],bg['proper time [Gyr]']), 
"hubble" : interp1d(z_interp,299792.46*np.vectorize(lcdm.Hubble)(z_interp)),
"RH" : interp1d(z_interp,1/(np.vectorize(lcdm.Hubble)(z_interp))),
}

mydata2 = {
"comoving" : interp1d(z_interp,np.vectorize(lcdm.comoving_distance)(z_interp)),
"dA" : interp1d(z_interp,np.vectorize(lcdm.angular_distance)(z_interp)),
"dL" : interp1d(z_interp,np.vectorize(lcdm.luminosity_distance)(z_interp)),
}

with open('lcdm1.pck', 'wb') as file_handle:
    pickle.dump(mydata1 , file_handle)

with open('lcdm2.pck', 'wb') as file_handle:
    pickle.dump(mydata2 , file_handle)
