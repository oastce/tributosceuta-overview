import html.parser
import sys

class HTMLStructureValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_tags:
            line, col = self.getpos()
            self.stack.append((tag, line, col))

    def handle_endtag(self, tag):
        if tag in self.void_tags:
            return
        if not self.stack:
            line, col = self.getpos()
            self.errors.append(f"Mismatched closing tag </{tag}> at line {line}, col {col} (no opening tag)")
            return
        
        expected_tag, line, col = self.stack.pop()
        if expected_tag != tag:
            current_line, current_col = self.getpos()
            # If there's a mismatch, we report it and put the expected tag back or keep going.
            self.errors.append(
                f"Tag mismatch: </{tag}> at line {current_line}, col {current_col} "
                f"does not match opening <{expected_tag}> at line {line}, col {col}"
            )
            # Try to recover by popping until we find a match or just restoring
            # For simplicity, we just report it.

    def close(self):
        super().close()
        while self.stack:
            tag, line, col = self.stack.pop()
            self.errors.append(f"Unclosed tag <{tag}> opened at line {line}, col {col}")

if __name__ == '__main__':
    with open('/Users/emiliorodrigocarreiravillalta/Desktop/tributosceuta-overview/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = HTMLStructureValidator()
    try:
        parser.feed(content)
        parser.close()
    except Exception as e:
        print(f"Parser error: {e}")
        sys.exit(1)
        
    if parser.errors:
        print("HTML validation errors found:")
        for error in parser.errors[:50]:  # Limit output
            print(error)
        sys.exit(1)
    else:
        print("HTML tag structure is perfectly balanced and valid!")
        sys.exit(0)
