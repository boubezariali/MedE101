package(default_visibility = ["//visibility:public"])

py_library(
    name = "pattern_match_utils",
    srcs = ["pattern_match_utils.py"],
    deps = ["//file_utils:array_io_utils"],
)

py_binary (
    name = "pattern_match",
    srcs = ["pattern_match.py"],
    deps = [":pattern_match_utils"],
)

