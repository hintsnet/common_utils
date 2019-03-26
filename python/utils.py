#!/usr/bin/python3
"""pimgeek 常用 python 方法"""

def class_var_dump(a_class):
	"""对 class variable 进行 dump, 以便调试脚本时检查"""
	class_vars = vars(a_class)
	dump_str = "\n".join("%s: [ %s ]" % item for item in class_vars.items() if not item[0].startswith('__'))
	return dump_str
