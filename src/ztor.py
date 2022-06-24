#!/usr/bin/python3

import pickle
from argparse import ArgumentParser, RawTextHelpFormatter

parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

parser.add_argument('z',type=float,
                    help="Pass the value of the redshift",
                    )
args = parser.parse_args()

try :
    zin = args.z
except :
    print('Provide a value of z')

with open('data/lcdm1.pck', 'rb') as file_handle:
    temp_dict = pickle.load(file_handle)
    age = temp_dict["age"]
    hofz = temp_dict['hubble']
    RH = temp_dict['RH']
with open('data/lcdm2.pck', 'rb') as file_handle:
    temp_dict = pickle.load(file_handle)
    comoving = temp_dict["comoving"]
    dA = temp_dict['dA']
    dL = temp_dict['dL']

agez = age(zin)
age0 = age(0)
lookbacktime = age0 - agez
hz = hofz(zin)
comovingZ = comoving(zin)
dAz = dA(zin)
dLz = dL(zin)
Rhz = RH(zin)
print('\nAge of the universe at z = {}        : '.format(zin), agez, 'Gyr')
print(  'Lookback time to z = {}              : '.format(zin), lookbacktime, 'Gyr')
print(  'Comoving distance to z = {}          : '.format(zin), comovingZ, 'Mpc')
print(  'Angular diameter distance to z = {}  : '.format(zin), dAz, 'Mpc')
print(  'Luminosity distance to z = {}        : '.format(zin), dLz, 'Mpc')
print(  'Hubble parameter at z = {}           : '.format(zin), hz, 'km/s/Mpc')
print(  'Hubble radius at z = {}              : '.format(zin), Rhz, 'Mpc')
print(  'Normalized scale factor at z = {}    : '.format(zin), 1/(1+zin))
print('\n')