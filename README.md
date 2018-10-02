conan-cmocka
============

Packaging up cmocka in conan.

## Build
```bash
conan create . <your_username>/<your_channel>
```
## Usage

Add this to your CMakeLists.txt:
```cmake
enable_testing()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include(CTest)

find_package(cmocka REQUIRED)
include_directories(${CONAN_INCLUDE_DIRS}/include)
add_executable(test_0 test/test_0.c)
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
