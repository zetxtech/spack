# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Voronota(CMakePackage):
    """Voronota is a software tool for analyzing three-dimensional structures of biological macromolecules using the Voronoi diagram of atomic balls."""

    homepage = "https://github.com/kliment-olechnovic/voronota"
    url = "https://github.com/kliment-olechnovic/voronota/releases/download/v1.29.4242/voronota_1.29.4242.tar.gz"

    maintainers("zetxtech")

    license("MIT", checked_by="zetxtech")

    version("1.29.4242", sha256="cb7c23c8022a1fa71a6d8280f049423dca79c94a71ac28b99de7e86e45d3d67a")