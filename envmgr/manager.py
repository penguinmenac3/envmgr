"""
# 01. Environment Manager

> Easily manage your environment (paths etc.) specific to projcets
"""
import json
import os


def setup() -> None:
    with open("envmgr.json", "r") as f:
        data = json.loads(f.read())
    for k, v in data["paths"].items():
        parts = v.split("/")
        parsed_parts = []
        for part in parts:
            if part.startswith("$"):
                part = os.environ[part[1:]]
            parsed_parts.append(part)
        path = "/".join(parsed_parts)
        os.environ[k] = path

def get(variable_name) -> str:
    return os.environ[variable_name]
