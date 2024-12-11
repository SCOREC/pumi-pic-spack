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

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on('mpi')

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx))
        args.append("-DCMAKE_C_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicc))
        args.append("ENABLE_PARMETIS=OFF")
        args.append("ENABLE_PUMI=OFF")
        args.append("CMAKE_CXX_FLAGS=-std=c++11")
        return args


