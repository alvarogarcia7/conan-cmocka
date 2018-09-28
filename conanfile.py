from os import rename, remove, path

from conans import ConanFile
from conans.tools import download, check_sha256, unzip


class CmockaConan(ConanFile):
    name = 'cmocka'
    version = '1.1.3'
    sha256 = '43eabcf72a9c80e3d03f7c8a1c04e408c18d2db5121eb058a3ef732a9dfabfaf'
    license = 'Apache License 2.0'
    homepage = 'https://github.com/elventear/cmocka'
    url = 'https://github.com/SamuelMarks/conan-cmocka'
    description = 'an elegant unit testing framework for C with support for mock objects. It only requires the standard C library, works on a range of computing platforms (including embedded) and with different compilers.'
    no_copy_source = True
    find_pkg = 'FindCMocka.cmake'
    exports_sources = ['include/*', 'FindCMocka.cmake']

    def source(self):
        archive_name = '{name}-{version}.tar.xz'.format(name=self.name, version=self.version)
        download('https://cmocka.org/files/{ver}/{archive_name}'.format(ver=self.version.rpartition('.')[0], archive_name=archive_name), archive_name)
        check_sha256(archive_name, self.sha256)
        unzip(archive_name)
        remove(archive_name)
        rename('{name}-{version}'.format(name=self.name, version=self.version), self.name)
        # download('https://raw.githubusercontent.com/owncloud/client/master/cmake/modules/{}'.format(self.find_pkg), self.find_pkg)
        # check_sha256(self.find_pkg, 'e8c4faa50f51bb3aefb1a4714cf2abd26db8ff35e08939c74a92f0b0b4ddb4de')

    def package(self):
        self.copy(pattern=self.find_pkg, dst='.', src='.', keep_path=True)
        # Copy the license files
        self.copy(path.join(self.name, 'doc', 'that_style', 'LICENSE'), dst='licenses', src=self.name)
        # Copying headers
        self.copy(pattern='*.h', dst='include', src=path.join(self.name, 'include'), keep_path=True)

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.env_info.CMAKE_MODULE_PATH = [self.package_folder]
