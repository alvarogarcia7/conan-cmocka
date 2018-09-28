# Try to find CMOCKA
# Once done, this will define
#
# CMOCKA_FOUND        - system has CMOCKA
# CMOCKA_INCLUDE_DIRS - CMOCKA include directories

find_path(
	CMOCKA_INCLUDE_DIR
	NAMES cmocka.h
	PATHS ${CONAN_INCLUDE_DIRS_CMOCKA}
	)

set(CMOCKA_FOUND TRUE)
set(CMOCKA_INCLUDE_DIRS ${CMOCKA_INCLUDE_DIR})

mark_as_advanced(CMOCKA_INCLUDE_DIR)

