
import os

from conan import ConanFile
from conan.tools.gnu import AutotoolsToolchain, Autotools
from conan.tools.layout import basic_layout
from conan.tools.apple import fix_apple_shared_install_name


class AbcConan(ConanFile):
    name = "abc"
    version = "1.0.0"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Abc here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "Makefile", "include/*", "src/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        basic_layout(self)

    def generate(self):
        at_toolchain = AutotoolsToolchain(self)
        at_toolchain.generate()

    def build(self):
        autotools = Autotools(self)
        autotools.make()

    def package(self):
        autotools = Autotools(self)
        autotools.install()
        fix_apple_shared_install_name(self)

    def package_info(self):
        self.cpp_info.libs = ["abc"]
