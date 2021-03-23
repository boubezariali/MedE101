package(default_visibility = ["//visibility:public"])

py_library (
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
        "//file_utils:array_io_utils",
        "//preprocessing:string_cleaning_utils",
        "//nlp:stanza_utils",
        ":feature_extractor",
    ]
)
