# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PumiPic(CMakePackage, CudaPackage):
    homepage      = "https://github.com/SCOREC/pumi-pic"
    git      = "https://github.com/SCOREC/pumi-pic"
    maintainers = ['Angelyr','jacobmerson','cwsmith']

    version("master", branch="master")
    version('2.1.4', commit='b6678b0a0b8c9ad1e143831bdc2920b944b0f5ff')
    version('2.1.3', commit='8130075d05f063413b8f637bcd9444a108e31f5b')

    variant("cabana", default=True, description="Build with cabana")

    depends_on('mpi')
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")

    depends_on("engpar")
    depends_on("kokkos@4.2.00")
    depends_on("omega-h@10.8.6-scorec +mpi +kokkos")
    depends_on("cabana@0.6.1 +mpi", when="+cabana")

    for arch in CudaPackage.cuda_arch_values:
        cuda_dep = "+cuda cuda_arch={0}".format(arch)
        depends_on("kokkos {0}".format(cuda_dep), when=cuda_dep)
        depends_on("omega-h {0}".format(cuda_dep), when=cuda_dep)
        depends_on("cabana {0}".format(cuda_dep), when=cuda_dep)

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx))
        if "+cabana" in self.spec:
            args.append("ENABLE_CABANA=ON")
        return args


