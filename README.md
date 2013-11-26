This is gfortran + mpif77 version of Traub 2005 code (originally
modified for g77 by Michael Hines). The makefile has been modified to
generate the executables for figures 2, 6, 7A-D and the serial
version.

make groucho_fig2
make groucho_fig6
make groucho_fig7A
make groucho_fig7B
make groucho_fig7C
make groucho_fig7D
make groucho_serial

will create the corresponding executables. For all but the last one
you need mpif77 with gfortran. The last one can be done with gfortran
without mpi.

To run a specific executable, except groucho_serial, use the
run_groucho.sh script. The argument should be the specific groucho
executable you want to run. Run groucho_serial directly:

./groucho_serial


---------------
This has been tested on the following system (the output of `mpif77 -v`)

Using built-in specs.
COLLECT_GCC=/usr/bin/gfortran
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.6/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu/Linaro 4.6.3-1ubuntu5' --with-bugurl=file:///usr/share/doc/gcc-4.6/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.6 --enable-shared --enable-linker-build-id --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.6 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --enable-plugin --enable-objc-gc --disable-werror --with-arch-32=i686 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.6.3 (Ubuntu/Linaro 4.6.3-1ubuntu5) 

----------------
Subhasis Ray, NCBS, Bangalore, INDIA
ray dot subhasis at gmail dot com
