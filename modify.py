#!/usr/bin/env python

import sublime, sublime_plugin

class ModifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      for region in self.view.sel():
        if not region.empty():
          s = self.view.substr(region)
          s = self.convert(s)
          self.view.replace(edit, region, s)

    def convert(self, text):

      # Add any custom replacements here
      self.exception_dict = { 
                   '<' : '&lt;',
                   '>' : '&gt;'
                  }

      final = ''

      # Look for characters to replace
      for c in text:
        if c in self.exception_dict:
          final = final + self.exception_dict[c]
        elif ord(c) < 128:
          final = final + c
        else:
          final = final + "&#" + str(ord(c)) + ";"
      return final