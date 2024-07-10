# Sprint_6
Testing Yandex Samokat Service

# Allure get an error allure-result not generating:
ImportError while importing test module '/Users/alexsoul/work/Sprint_6/Tests/test_main_page.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
Tests/test_main_page.py:4: in <module>
    from Page_object.base_page import BasePage
E   ModuleNotFoundError: No module named 'Page_object'