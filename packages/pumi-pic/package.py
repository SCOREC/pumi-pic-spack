# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PumiPic(CMakePackage, CudaPackage):
    homepage      = "https://github.com/SCOREC/pumi-pic"
    git      = "https://github.com/SCOREC/pumi-pic"
    maintainers = ['Angelyr','jacobmerson','cwsmith']

    version('2.1.3', commit='8130075d05f063413b8f637bcd9444a108e31f5b')

    depends_on('mpi')
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on("kokkos@4.2.00")
    depends_on("engpar")
    depends_on("omega-h@10.8.6-scorec+kokkos")
    depends_on("cabana@0.6.1")

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx)),
            self.define("ENABLE_CABANA", True)
        ]
        return args


