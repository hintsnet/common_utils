#!/usr/bin/python3
"""pimgeek 常用 python 方法"""

def class_var_dump(a_class):
	"""对 class variable 进行 dump, 以便调试脚本时检查"""
	class_vars = vars(a_class)
	dump_str = "\n".join("%s: [ %s ]" % item for item in class_vars.items() if not item[0].startswith('__'))
	return dump_str

def class_var_dump2(a_class):
	"""对 class variable 进行 dump, 以便调试脚本时检查"""
	var_names = dir(a_class)
	user_var_names = [item for item in var_names if not item.startswith('__')]
	dump_str = "\n".join("%s: [ %s ]" % (item, getattr(a_class, item)) for item in user_var_names)
	return dump_str
