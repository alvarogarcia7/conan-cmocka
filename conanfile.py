from os import rename, remove, path

from conans import ConanFile, CMake
from conans.tools import download, check_sha256, unzip


class CmockaConan(ConanFile):
    name = 'cmocka'
    version = '1.1.3'
    sha256 = '43eabcf72a9c80e3d03f7c8a1c04e408c18d2db5121eb058a3ef732a9dfabfaf'
    license = 'Apache License 2.0'
    homepage = 'https://cmocka.org'
    url = 'https://github.com/SamuelMarks/conan-cmocka'
    description = 'an elegant unit testing framework for C with support for mock objects. It only requires the standard C library, works on a range of computing platforms (including embedded) and with different compilers.'
    no_copy_source = True
    find_pkg = 'FindCMocka.cmake'
    exports_sources = ['include/*', 'FindCMocka.cmake']
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'shared': [True, False]}
    default_options = 'shared=False'
    generators = 'cmake'

    def source(self):
        archive_name = '{name}-{version}.tar.xz'.format(name=self.name, version=self.version)
        download('https://cmocka.org/files/{ver}/{archive_name}'.format(
            ver=self.version.rpartition('.')[0], archive_name=archive_name
        ), archive_name)
        check_sha256(archive_name, self.sha256)
        unzip(archive_name)
        remove(archive_name)
        rename('{name}-{version}'.format(name=self.name, version=self.version), self.name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.name)
        cmake.build()

    def package(self):
        self.copy(pattern=self.find_pkg, dst='.', src='.', keep_path=True)
        self.copy("*.h", dst="include", src=self.name, keep_path=True)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
        self.env_info.CMAKE_MODULE_PATH = [self.package_folder]
