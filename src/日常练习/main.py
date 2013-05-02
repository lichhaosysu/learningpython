import re
text = '[ClojureWerkz Clojure libraries](http://clojurewerkz.org)'
pattern = r'\[(.*)\]\((http[s]?://[\.a-zA-Z/]+)\)'
#self.addFilter(r'\[(.*)\]\((http[s]?://[\.a-zA-Z/]+)\)','markdownurl')

match = re.match(pattern, text)
if match:
    print '<a href="%s">%s</a>' % (match.group(2), match.group(1))

