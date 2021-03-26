package(default_visibility = ["//visibility:public"])

py_library(
    name = "pattern_match_utils",
    srcs = ["pattern_match_utils.py"],
    deps = ["//file_utils:array_io_utils"],
)

py_binary(
    name = "pattern_match_main",
    srcs = ["pattern_match_main.py"],
    deps = [":pattern_match_utils"],
)

py_library(
    name = "stanza_utils",
    srcs = ["stanza_utils.py"],
)

py_library(
    name = "keyword_handler",
    srcs = ["keyword_handler.py"],
    deps = [
        "//file_utils:array_io_utils",
        "//preprocessing:string_cleaning_utils",
    ],
)
