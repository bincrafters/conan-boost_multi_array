#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostMulti_ArrayConan(base.BoostBaseConan):
    name = "boost_multi_array"
    url = "https://github.com/bincrafters/conan-boost_multi_array"
    lib_short_names = ["multi_array"]
    header_only_libs = ["multi_array"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_functional",
        "boost_iterator",
        "boost_mpl",
        "boost_static_assert",
        "boost_type_traits"
    ]


