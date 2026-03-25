# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PumiTally(CMakePackage, CudaPackage):
    homepage      = "https://github.com/Fuad-HH/PumiUMTally"
    git      = "https://github.com/Fuad-HH/PumiUMTally.git"
    maintainers = ["Fuad-HH"]

    version("main", branch="main")
    version("openmc", branch="integrate_pp_search_class")

    depends_on('mpi')
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("cmake", type="build")

    depends_on("pumi-pic@pumitally+shared")

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx))
        args.append("-DCMAKE_C_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicc))
        args.append("-DBUILD_SHARED_LIBS=ON")
        args.append("-DPUMITALLYOPENMC_ENABLE_TESTS=OFF")

        return args


