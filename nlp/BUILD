package(default_visibility = ["//visibility:public"])

py_library(
    name = "pattern_match_utils",
    srcs = ["pattern_match_utils.py"],
    deps = ["//file_utils:array_io_utils"],
)

py_binary (
    name = "pattern_match_main",
    srcs = ["pattern_match_main.py"],
    deps = [":pattern_match_utils"],
)

py_library (
    name = "feature_extractor",
    srcs = ["feature_extractor.py"],
    deps = [
        "//file_utils:array_io_utils",
        "//preprocessing:string_cleaning_utils",
        ":stanza_utils",
    ],
)

py_library(
    name = "stanza_utils",
    srcs = ["stanza_utils.py"],
)
