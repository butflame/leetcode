class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tmp = ""
        for i in path:
            if i == "/":
                if not tmp:
                    continue
                elif tmp == ".":
                    tmp = ""
                    continue
                elif tmp == "..":
                    if stack:
                        stack.pop()
                        tmp = ""
                    else:
                        tmp = ""
                        continue
                else:
                    stack.append(tmp)
                    tmp = ""
            else:
                tmp += i
        if not tmp:
            pass
        elif tmp == ".":
            pass
        elif tmp == "..":
            if stack:
                stack.pop()
        else:
            stack.append(tmp)
        if not stack:
            return "/"
        ret = ""
        for i in stack:
            ret += "/" + i
        return ret
