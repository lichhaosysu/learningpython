# -*- coding:UTF-8 -*-
'''
Created on 2013-4-24

@author: Stefan
'''
import re
class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
    
class HeadingRule(Rule):
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)
    
class ListItemRule(Rule):
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self, block):
        return True
    
    
    
'''
为Markdown下面的标题添加的规则，by lichhao
'''
class MarkdownHeadingRule(Rule):
    def condition(self, block):
        return block[0] == '#'
    def action(self, block, handler):
        #由开头的'#'符号决定标题的等级数，依次h1~h6，等级数最大为6
        #末尾可有'#'符号，也可没有，等级数只由开头的'#'个数决定
        pattern = r'^(#{1,6})([#]*[^#]*)(#*)$'
        match = re.match(pattern, block)
        if match:
            level = str(len(match.group(1)))
            print '<h' + level + '>' + match.group(2).strip() + '</h' + level + '>'
        return True