class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i = 0
        n = len(formula)

        count = Counter()
        stack = [count]

        while i<n:
            if formula[i]=="(":
                count = Counter()
                stack.append(count)
                i+=1

            elif formula[i]==")":
                digit = ""
                i+=1
                while i<n and formula[i].isdigit():
                    digit += formula[i]
                    i+=1
                
                val = int(digit or 1)
                top = stack.pop()

                for v,c in top.items():
                    stack[-1][v] += c*val

                count = stack[-1]
            else:
                atom = formula[i]
                i+=1

                while i<n and formula[i].islower():
                    atom += formula[i]
                    i+=1
                
                digit = ""
                while i<n and formula[i].isdigit():
                    digit += formula[i]
                    i+=1
                
                val = int(digit or 1)

                stack[-1][atom] += val

        return "".join(name+(str(count[name]) if count[name]>1 else "") for name in sorted(count))