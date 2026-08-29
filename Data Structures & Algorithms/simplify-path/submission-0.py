class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for s in path.split('/'):
            if not s:
                continue
            if s == '.':
                continue
            elif s == '..' and stack:
                stack.pop()
            elif s != '..':
                stack.append(s)

        return '/' + '/'.join(stack)