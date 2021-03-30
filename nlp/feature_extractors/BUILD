package(default_visibility = ["//visibility:public"])

py_library(
    name = "feature_extractor",
    srcs = ["feature_extractor.py"],
    deps = [
        "//nlp:keyword_handler",
    ],
)

py_library(
    name = "mimic_feature_extractor",
    srcs = ["mimic_feature_extractor.py"],
    deps = [
        ":feature_extractor",
        "//file_utils:array_io_utils",
        "//nlp:stanza_utils",
        "//preprocessing:string_cleaning_utils",
    ],
)

py_library(
    name = "clause_feature_extractor",
    srcs = ["clause_feature_extractor.py"],
    deps = [
        ":feature_extractor",
        "//file_utils:array_io_utils",
        "//nlp:stanza_utils",
        "//preprocessing:string_cleaning_utils",
    ],
)

py_test(
    name = "feature_extraction_test", 
    srcs = ["feature_extraction_test.py"],
    deps = [
        ":feature_extractor",
        ":mimic_feature_extractor",
    ],
)
