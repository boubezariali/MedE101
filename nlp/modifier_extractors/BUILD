package(default_visibility = ["//visibility:public"])

py_library(
    name = "modifier_extractor",
    srcs = ["modifier_extractor.py"],
    deps = [
        "//nlp:keyword_handler",
    ],
)

py_library(
    name = "negation_modifier_extractor",
    srcs = ["negation_modifier_extractor.py"],
    deps = [
        ":modifier_extractor",
        "//file_utils:array_io_utils",
        "//nlp:stanza_utils",
    ],
)
