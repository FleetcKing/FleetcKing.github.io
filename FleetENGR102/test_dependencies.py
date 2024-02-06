errors = []

try:
    import bs4
except ModuleNotFoundError as e:
    errors.append(str(e))

try:
    import requests
except ModuleNotFoundError as e:
    errors.append(str(e))

try:
    import pandas
except ModuleNotFoundError as e:
    errors.append(str(e))

if not errors:
    print("No Issues Detected")
else:
    print("\n".join(errors))