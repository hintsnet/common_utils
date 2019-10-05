#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取当前光标选中的节点的标题
def get_focused_node_title():
  # 获取当前选中的节点的 VNode 对象
  focused_node = c.currentPosition()
  # 获取节点标题 (移除前导和末位空格)
  focused_node_title = focused_node.h.strip()
  return focused_node_title
