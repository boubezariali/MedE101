py_library (
    name = "sentence_splitting_utils", 
    srcs = ["sentence_splitting_utils.py"]
)

py_binary (
    name = "preprocessing_main", 
    srcs = ["preprocessing_main.py"], 
    deps = [
        ":sentence_splitting_utils",
        ":string_cleaning_utils",
    ]
)		

py_library (
    name = "string_cleaning_utils",
    data = [":stopwords"],
    srcs = ["string_cleaning_utils.py"], 
)

filegroup(
    name = "stopwords", 
    srcs = ["stopwords.txt"],
)
