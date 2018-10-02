conan-cmocka
============

Packaging up cmocka in conan. Hosted on bintray: https://bintray.com/samuelmarks/cmocka/cmocka%3Asamuelmarks

## Developing conan-cmocka, rebuild with:
```bash
conan create . <your_username>/<your_channel>
```

## Usage

### Add a `conanfile.txt` with:
```ini
[requires]
cmocka/1.1.3@samuelmarks/stable

[generators]
cmake
```

### Add this to your `CMakeLists.txt`:
```cmake
enable_testing()
include(CTest)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

find_package(CMOCKA REQUIRED)
if (CMOCKA_FOUND)
    include_directories("${CONAN_INCLUDE_DIRS_CMOCKA}/include")
    add_executable(test_0 test/test_0.c)
    add_test(test_0 test_0)
    target_link_libraries(test_0 cmocka)
else ()
    message(could not find CMocka, did you run `conan install`?)
endif ()
```

Where `test/test_0.c` contains:
```c
#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include "cmocka.h"

/* A test case that does nothing and succeeds. */
static void null_test_success(void **state) {
    (void) state; /* unused */
}

int main(void) {
    const struct CMUnitTest tests[] = {
            cmocka_unit_test(null_test_success),
    };

    return cmocka_run_group_tests(tests, NULL, NULL);
}
```
