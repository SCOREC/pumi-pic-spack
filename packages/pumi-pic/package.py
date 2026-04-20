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
    version(
            'pumitally',
            git="https://github.com/Fuad-HH/pumi-pic.git",
            branch='make_search_class'
    )

    variant("cabana", default=True, description="Build with cabana")
    variant("pic", default=False, description="Build with position independent code (-fPIC)")
    variant("shared", default=False, description="Build shared libraries")

    conflicts("+pic", when="+shared")
    conflicts("+shared", when="+pic")

    depends_on('mpi')
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("cmake", type="build")

    depends_on("engpar@master")
    conflicts(
        "^engpar~pic~shared",
        when="+shared",
        msg="PUMI-PiC builds shared or links into shared consumers; EnGPar must be built with +pic or +shared",
    )
    conflicts(
        "^engpar~pic~shared",
        when="+pic",
        msg="PUMI-PiC builds shared or links into shared consumers; EnGPar must be built with +pic or +shared",
    )
    
    depends_on("kokkos@4.7.00")
    depends_on("omega-h@11.0.0-scorec +kokkos")
    depends_on("cabana@0.6.1", when="+cabana")
    depends_on("cabana@0.6.1", when="@pumitally")

    for arch in CudaPackage.cuda_arch_values:
        cuda_dep = "+cuda cuda_arch={0}".format(arch)
        depends_on("kokkos {0}".format(cuda_dep), when=cuda_dep)
        depends_on("omega-h {0}".format(cuda_dep), when=cuda_dep)
        depends_on("cabana {0}".format(cuda_dep), when=cuda_dep)

    def cmake_args(self):
        args = []
        args.append("-DCMAKE_CXX_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicxx))
        args.append("-DCMAKE_C_COMPILER:FILEPATH={0}".format(self.spec["mpi"].mpicc))
        if "+shared" in self.spec:
            args.append("-DBUILD_SHARED_LIBS=ON")
        elif "+pic" in self.spec:
            args.append("-DCMAKE_POSITION_INDEPENDENT_CODE=ON")
        if "+cabana" in self.spec:
            args.append("-DENABLE_CABANA=ON")
        return args


