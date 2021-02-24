py_library (
    name = "sentence_splitting_utils", 
    srcs = ["sentence_splitting_utils.py"]
)

py_binary (
    name = "preprocessing_main", 
    srcs = ["preprocessing_main.py"], 
    deps = [
        ":sentence_splitting_utils",
    ]
)		
