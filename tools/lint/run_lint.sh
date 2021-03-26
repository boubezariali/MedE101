#!/usr/bin/bash
black -S */**.py
isort */**.py
bazel run //:buildifier
