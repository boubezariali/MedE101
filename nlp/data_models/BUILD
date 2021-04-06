package(default_visibility = ["//visibility:public"])

py_library(
    name = "data_model",
    srcs = ["data_model.py"],
)

py_library(
    name = "comprehensive_data_model",
    srcs = ["comprehensive_data_model.py"],
    deps = [
        ":data_model",
        "//nlp:keyword_handler",
        "//nlp/feature_extractors:anatomy_list_feature_extractor",
        "//nlp/feature_extractors:clause_feature_extractor",
        "//nlp/feature_extractors:mimic_feature_extractor",
    ],
)
