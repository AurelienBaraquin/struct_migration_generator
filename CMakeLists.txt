project("caca")

set(SRC
    "src/main.cpp"
    "src/migrations/PlayerV1_to_V2.cpp"
    "src/migrations/PlayerV2_to_V3.cpp"
    "src/migrations/PlayerV3_to_V4.cpp"
    "src/migrations/PlayerV4_to_V5.cpp"
    "src/migrations/PlayerV5_to_V6.cpp"
    "src/migrations/PlayerV6_to_V7.cpp"
    "src/migrations/PlayerV7_to_V8.cpp"
    "src/BinaryReaderRegistry.cpp"
)

add_executable(caca ${SRC})

target_include_directories(caca
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/include/aliases
        ${CMAKE_CURRENT_SOURCE_DIR}/include/versions
)
