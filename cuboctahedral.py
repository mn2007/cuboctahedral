#
#  Copyright 2020 Masashi Noda
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import numpy as np

def main():
    atomname = input()
    lattice_constant = float(input())
    m = int(input()) # m_th magic number

# Number of atoms for cuboctahedral and icosahedral is same, and the number for icosahedral 
# is written as the formula (12.26) in the book "Physics of Atoms and Ions" by B. M. Smirnov.
    print((10*m**3+15*m**2+11*m+3)/3)
    print("comment line")

    for iz in range(-m,m+1):
        for iy in range(-m,m+1):
            for ix in range(-m,m+1):
                if (ix+iy+iz)%2==0 and iy<=-ix+2*m-abs(iz) and iy>=ix-2*m+abs(iz) and iy<=ix+2*m-abs(iz) and iy>=-ix-2*m+abs(iz):
                    array = np.array([float(ix), float(iy), float(iz)])
                    array=array*lattice_constant/2.0
                    print('%s %14.8f %14.8f %14.8f' % (atomname,array[0],array[1],array[2]))

if __name__=='__main__':
    main()

