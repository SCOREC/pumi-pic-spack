# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class OpenmcPumi(CMakePackage):
    """This is a fork of OpenMC (https://github.com/openmc-dev/openmc/) to
    integrate PumiPIC based accelerated tally: Pumi-Tally.

    OpenMC is a community-developed Monte Carlo neutron and photon transport
    simulation code. It is capable of performing fixed source, k-eigenvalue, and
    subcritical multiplication calculations on models built using either a
    constructive solid geometry or CAD representation. OpenMC supports both
    continuous-energy and multigroup transport. The continuous-energy particle
    interaction data is based on a native HDF5 format that can be generated from ACE
    files produced by NJOY. Parallelism is enabled via a hybrid MPI and OpenMP
    programming model."""

    homepage = "https://docs.openmc.org/"
    git = "https://github.com/Fuad-HH/openmc"
    maintainers("Fuad-HH")

    version("main", branch="decouple_pumi_tally", submodules=True)
    variant("openmp", default=True, description="Enable OpenMP support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("git", type="build")
    depends_on("hdf5+hl~mpi")
    depends_on("pumi-tally@openmc")

    def cmake_args(self):
        options = ["-DCMAKE_INSTALL_LIBDIR=lib"]  # forcing bc sometimes goes to lib64
        options += ["-DOPENMC_USE_PUMIPIC=ON"]

        use_newer_options = self.spec.satisfies("@0.13.1:")

        if use_newer_options:
            options += [self.define_from_variant("OPENMC_USE_OPENMP", "openmp")]
        else:
            options += [self.define_from_variant("openmp")]

        return options
