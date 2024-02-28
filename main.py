import ast


def count_variables(node):
    sum = 0
    vars = dict()
    for n in ast.walk(node):
        print(n)
        if isinstance(n, ast.Constant):
            if str(n.value) not in vars.keys():
                vars[str(n.value)] = 1
            else:
                vars[str(n.value)] +=1
        if isinstance(n, ast.Name):
            if   n.id not in vars.keys():
                vars[n.id] = 1
            else:
                vars[n.id] +=1

    print(vars)
    return sum


def count_binaty_opr(node):
    oprs = {
        "+" :0 ,
        "-": 0,
        "*": 0,
        "/": 0,
        "//": 0,
        "%": 0,
        "**": 0,
        ">>" :0,
        "<<" :0,
        "|" :0,
        "^" :0,
        "&" :0,
        "@" : 0,
        "and" :0,
        "or" : 0,
        "==": 0,
        "!=": 0,
        "<": 0,
        "<=": 0,
        ">": 0,
        ">=": 0,
        "is": 0,
        "is not": 0,
        "in": 0,
        "not in" :0,
        "not": 0,
        "~" :0,
        "if":0,
        "if else" :0,
        "elif":0,
        "=":0,
        "+=": 0,
        "-=": 0,
        "*=": 0,
        "/=": 0,
        "//=": 0,
        "%=": 0,
        "**=": 0,
        ">>=": 0,
        "<<=": 0,
        "|=": 0,
        "^=": 0,
        "&=": 0,
        "@=": 0,

    }

    for n in ast.walk(node):
        if isinstance(n, ast.Assign):
            oprs["="]+=len(n.targets)
        if isinstance(n, ast.If):

            if n.orelse:
                oprs["if else"] += 1
                #???elif is new operands???
                # if isinstance(n.orelse[0], ast.If):
                #     oprs["if else"]-=1
                #     oprs['elif']+=1
                # else:
                #     oprs["else"]+=1
            else:
                oprs["if"]+=1
        if isinstance(n, ast.UAdd):
            oprs["+"]+=1
        if isinstance(n, ast.USub):
            oprs["-"]+=1
        if isinstance(n, ast.Invert):
            oprs["~"]+=1
        if isinstance(n, ast.Not):
            oprs["not"]+=1
        if isinstance(n, ast.Eq):
            oprs["=="]+=1
        if isinstance(n, ast.NotEq):
            oprs["!="]+=1
        if isinstance(n, ast.Lt):
            oprs["<"]+=1
        if isinstance(n, ast.LtE):
            oprs["<="]+=1
        if isinstance(n, ast.Gt):
            oprs[">"] += 1
        if isinstance(n, ast.GtE):
            oprs[">="] += 1
        if isinstance(n, ast.Is):
            oprs["is"]+=1
        if isinstance(n, ast.IsNot):
            oprs["is not"]+=1
        if isinstance(n, ast.In):
            oprs["in"] += 1
        if isinstance(n, ast.NotIn):
            oprs["not in"] += 1
        if isinstance(n, ast.BinOp):

            if isinstance(n.op, ast.Add):
                oprs["+"] +=1
            if isinstance(n.op, ast.Sub):
                oprs["-"] +=1
            if isinstance(n.op, ast.Mult):
                oprs["*"] +=1
            if isinstance(n.op, ast.Div):
                oprs["/"] +=1
            if isinstance(n.op, ast.FloorDiv):
                oprs["//"] +=1
            if isinstance(n.op, ast.Mod):
                oprs["%"] +=1
            if isinstance(n.op, ast.Pow):
                oprs["**"] +=1
            if isinstance(n.op, ast.LShift):
                oprs["<<"] +=1
            if isinstance(n.op, ast.RShift):
                oprs[">>"] +=1
            if isinstance(n.op, ast.BitOr):
                oprs["|"] +=1
            if isinstance(n.op, ast.BitXor):
                oprs["^"] +=1
            if isinstance(n.op, ast.BitAnd):
                oprs["&"] +=1
            if isinstance(n.op, ast.MatMult):
                oprs["@"] +=1
        if isinstance(n, ast.AugAssign):

            if isinstance(n.op, ast.Add):
                oprs["+="] +=1
            if isinstance(n.op, ast.Sub):
                oprs["-="] +=1
            if isinstance(n.op, ast.Mult):
                oprs["*="] +=1
            if isinstance(n.op, ast.Div):
                oprs["/="] +=1
            if isinstance(n.op, ast.FloorDiv):
                oprs["//="] +=1
            if isinstance(n.op, ast.Mod):
                oprs["%="] +=1
            if isinstance(n.op, ast.Pow):
                oprs["**="] +=1
            if isinstance(n.op, ast.LShift):
                oprs["<<="] +=1
            if isinstance(n.op, ast.RShift):
                oprs[">>="] +=1
            if isinstance(n.op, ast.BitOr):
                oprs["|="] +=1
            if isinstance(n.op, ast.BitXor):
                oprs["^="] +=1
            if isinstance(n.op, ast.BitAnd):
                oprs["&="] +=1
            if isinstance(n.op, ast.MatMult):
                oprs["@="] +=1
        if isinstance(n, ast.BoolOp):
            if isinstance(n.op, ast.And):
                oprs["and"] +=1
            if isinstance(n.op, ast.Or):
                oprs["or"] +=1

    print(oprs)
def count_loops(node):
    loops= {
        "For" :0,
        "While":0,
        "break" :0,
        "continue" :0,
    }
    for n in ast.walk(node):
        if isinstance(n, ast.For):
            loops["For"]+=1
        elif isinstance(n,ast.While):
            loops["While"]+=1
        elif isinstance(n,ast.Break):
            loops["break"]+=1
        elif isinstance(n, ast.Continue):
            loops["continue"] += 1
    print(f"funcs: {loops}")
def count_try_excent(node):
    tryes = {
        "try..except..finally":0
    }
    for n in ast.walk(node):
        if isinstance(n, ast.Try):
            tryes["try..except..finally"]+=1
def count_func(node):
    funcs = {
        "return":0,
        "yeild" :0,
        "yeild from":0,
        "lambda":0,
        "pass":0,
        "assert":0,
        "with":0,
    }
    for n in ast.walk(node):
        if isinstance(n, ast.With):
            funcs["with"]+=1
        if isinstance(n, ast.Assert):
            funcs["assert"]+=1
        if isinstance(n, ast.Return):
            funcs["return"]+=1
        elif isinstance(n, ast.Pass):
            funcs["pass"]+=1
        elif isinstance(n, ast.Lambda):
            funcs["lambda"]+=1
        elif isinstance(n, ast.Yield):
            funcs["yeild"]+=1
        elif isinstance(n, ast.YieldFrom):
            funcs["yeild from"]+=1
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Attribute):#methods
                if n.func.attr not in funcs:
                    funcs[n.func.attr]=1
                else:
                    funcs[n.func.attr] += 1
            elif isinstance(n.func, ast.Name):#functions
                if n.func.id not in funcs:
                    funcs[n.func.id]=1
                else:
                    funcs[n.func.id] += 1
        #???do we need to add a function declaration to the operands????
        # if isinstance(n, ast.FunctionDef):
        #     if n.func.attr not in funcs:
        #         funcs[n.name] = 1
        #     else:
        #         funcs[n.name] += 1

    print(funcs)

def parse_file(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())


    num_variables = count_variables(tree)
    num_loops = count_loops(tree)

    count_binaty_opr(tree)
    count_func(tree)
if __name__ == "__main__":
    file_path = "example.py"
    parse_file(file_path)