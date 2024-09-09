if(NOT DEFINED ENV{QNX_HOST})
    message(FATAL_ERROR "QNX_HOST env variable must be defined!")
endif()

if(NOT DEFINED ENV{QNX_TARGET})
    message(FATAL_ERROR "QNX_TARGET env variable must be defined!")
endif()

set(CMAKE_SYSTEM_PROCESSOR "aarch64" CACHE STRING "CMAKE_SYSTEM_PROCESSOR for QNX build")

set(QNX_ARCH "aarch64le")
set(arch "gcc_nto${QNX_ARCH}")
set(CMAKE_C_COMPILER_TARGET "${arch}")
set(CMAKE_CXX_COMPILER_TARGET "${arch}")

set(CMAKE_AR      "$ENV{QNX_HOST}/usr/bin/ntoaarch64-ar"      CACHE PATH "QNX ar Program")
set(CMAKE_RANLIB  "$ENV{QNX_HOST}/usr/bin/ntoaarch64-ranlib"  CACHE PATH "QNX ranlib Program")
set(CMAKE_NM      "$ENV{QNX_HOST}/usr/bin/ntoaarch64-nm"      CACHE PATH "QNX nm Program")
set(CMAKE_OBJCOPY "$ENV{QNX_HOST}/usr/bin/ntoaarch64-objcopy" CACHE PATH "QNX objcopy Program")
set(CMAKE_OBJDUMP "$ENV{QNX_HOST}/usr/bin/ntoaarch64-objdump" CACHE PATH "QNX objdump Program")
set(CMAKE_LINKER  "$ENV{QNX_HOST}/usr/bin/ntoaarch64-ld"      CACHE PATH "QNX Linker Program")
set(CMAKE_STRIP   "$ENV{QNX_HOST}/usr/bin/ntoaarch64-strip"   CACHE PATH "QNX Strip Program")

list(APPEND CMAKE_FIND_ROOT_PATH "$ENV{QNX_TARGET}"
                                 "$ENV{QNX_TARGET}/${QNX_ARCH}/usr")
message(STATUS "CMAKE_FIND_ROOT_PATH: ${CMAKE_FIND_ROOT_PATH}")

# Threads module fails to assign proper flags in cross compiler environment
# for QNX build so that the '-pthread' flag is added by a mistake.
# Flags below force internal logic to use libc thread implementation.
set(CMAKE_HAVE_LIBC_PTHREAD YES)
