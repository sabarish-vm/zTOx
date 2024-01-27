from argparse import ArgumentParser, RawTextHelpFormatter
import astropy.cosmology as cosmo

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

    z=0.1
    H0=67.36
    OmegaM0=0.3153
    OmegaB0=0.05
    OmegaDE=0.6847
    Tcmb0=0
    model=cosmo.LambdaCDM(H0=H0,Om0=OmegaM0,Ob0=OmegaB0,Ode0=OmegaDE,Tcmb0=Tcmb0)

    agez = model.age(zin)
    age0 = model.age(0)
    lookbacktime = age0 - agez
    hz = model.H(zin)
    comovingZ = model.comoving_distance(zin)
    dAz = model.angular_diameter_distance(zin)
    dLz = model.luminosity_distance(zin)
    Rhz = 1/hz
    print('\n')
    print( 'Age of the universe at z = {}        : '.format(zin), agez, 'Gyr')
    print(  'Lookback time to z = {}              : '.format(zin), lookbacktime, 'Gyr')
    print(  'Comoving distance to z = {}          : '.format(zin), comovingZ, 'Mpc')
    print(  'Angular diameter distance to z = {}  : '.format(zin), dAz, 'Mpc')
    print(  'Luminosity distance to z = {}        : '.format(zin), dLz, 'Mpc')
    print(  'Hubble parameter at z = {}           : '.format(zin), hz, 'km/s/Mpc')
    print(  'Hubble radius at z = {}              : '.format(zin), Rhz, 'Mpc')
    print(  'Normalized scale factor at z = {}    : '.format(zin), 1/(1+zin))
    print('\n')