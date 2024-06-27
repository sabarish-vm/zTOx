from argparse import ArgumentParser, RawTextHelpFormatter
import astropy.cosmology as cosmo
import astropy.units as u

def ztox() :
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument('z',type=float,
                        help="Pass the value of the redshift",
                        )
    args = parser.parse_args()

    try :
        zin = args.z
    except :
        print('Provide a value of z')

    H0=67.36
    OmegaM0=0.3153
    OmegaB0=0.05
    OmegaDE=0.6847
    Tcmb0=2.725*u.K
    model=cosmo.LambdaCDM(H0=H0,Om0=OmegaM0,Ob0=OmegaB0,Ode0=OmegaDE,Tcmb0=Tcmb0)

    agez = model.age(zin)
    age0 = model.age(0)
    lookbacktime = age0 - agez
    hz = model.H(zin)
    comovingZ = model.comoving_distance(zin)
    dAz = model.angular_diameter_distance(zin)
    dLz = model.luminosity_distance(zin)
    scaleFac=1/(1+zin)
    Tcmbz=Tcmb0/scaleFac
    Rhz = 1/hz
    print('\n')
    print(  'Age of the universe at z = {}        : '.format(zin), f"{agez:.3f}")
    print(  'Lookback time to z = {}              : '.format(zin), f"{lookbacktime:.3f}")
    print(  'Comoving distance to z = {}          : '.format(zin), f"{comovingZ:.3f}")
    print(  'Angular diameter distance to z = {}  : '.format(zin), f"{dAz:.3f}")
    print(  'Luminosity distance to z = {}        : '.format(zin), f"{dLz:.3f}")
    print(  'Hubble parameter at z = {}           : '.format(zin), f"{hz:.3f}")
    print(  'Hubble radius at z = {}              : '.format(zin), f"{Rhz:.3f}")
    print(  'Normalized scale factor at z = {}    : '.format(zin), f"{scaleFac:.3f}")
    print(  'Temperature of CMB  at z = {}        : '.format(zin), f"{Tcmbz:.3f}")
    print('')
