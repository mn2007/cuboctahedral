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

