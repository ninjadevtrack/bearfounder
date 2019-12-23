from diff_match_patch import diff_match_patch
from django import template

register = template.Library()


@register.simple_tag
def compare_values(value1, value2):
    dmp = diff_match_patch()
    diff = dmp.diff_main(value1, value2)
    dmp.diff_cleanupSemantic(diff)
    html = dmp.diff_prettyHtml(diff)
    return html


@register.tag(name='make_list')
def make_list(parser, token):
  bits = list(token.split_contents())
  if len(bits) >= 4 and bits[-2] == "as":
    varname = bits[-1]
    items = bits[1:-2]
    return MakeListNode(items, varname)
  else:
    raise template.TemplateSyntaxError("%r expected format is 'item [item ...] as varname'" % bits[0])


class MakeListNode(template.Node):
  def __init__(self, items, varname):
    self.items = map(template.Variable, items)
    self.varname = varname

  def render(self, context):
    context[self.varname] = [ i.resolve(context) for i in self.items ]
    return ""
