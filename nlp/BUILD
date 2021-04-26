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

py_binary(
    name = "feature_extraction_main",
    srcs = ["feature_extraction_main.py"],
    deps = [
        "//nlp:data_module",
        "//nlp/data_models:comprehensive_data_model",
    ],
)

py_library(
    name = "stanza_utils",
    srcs = ["stanza_utils.py"],
)

py_library(
    name = "keyword_handler",
    srcs = ["keyword_handler.py"],
    data = [
        "//data/main_data:keywords",
    ],
    deps = [
        "//file_utils:array_io_utils",
        "//file_utils:runfile_utils",
        "//nlp:stanza_utils",
        "//preprocessing:string_cleaning_utils",
    ],
)

py_library(
    name = "data_module",
    srcs = ["data_module.py"],
)

py_library(
    name = "modifier_handler",
    srcs = ["modifier_handler.py"],
    deps = [
        ":stanza_utils",
    ],
)
