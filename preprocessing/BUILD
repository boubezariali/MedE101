package(default_visibility = ["//visibility:public"])

py_library(
    name = "sentence_splitting_utils",
    srcs = ["sentence_splitting_utils.py"],
)

py_binary(
    name = "preprocessing_main",
    srcs = ["preprocessing_main.py"],
    deps = [
        ":sentence_splitting_utils",
        ":string_cleaning_utils",
        "//file_utils:array_io_utils",
    ],
)

py_library(
    name = "string_cleaning_utils",
    srcs = ["string_cleaning_utils.py"],
    data = [":listed_data"],
    deps = [
        "//file_utils:array_io_utils",
        "//file_utils:runfile_utils",
    ],
)

filegroup(
    name = "listed_data",
    srcs = [
        "punctuation.txt",
        "stopwords.txt",
    ],
)
