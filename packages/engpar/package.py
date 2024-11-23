# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Engpar(CMakePackage):
    homepage      = "https://github.com/SCOREC/EnGPar"
    git      = "https://github.com/SCOREC/EnGPar"
    maintainers = ['Angelyr','jacobmerson','cwsmith']

    version('master', branch='master')

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("cmake", type="build")
    depends_on('mpi')

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx)),
            self.define("CMAKE_C_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicc)),
            self.define("ENABLE_PARMETIS", False),
            self.define("ENABLE_PUMI", False),
            self.define("CMAKE_CXX_FLAGS", "-std=c++11")
        ]
        return args


