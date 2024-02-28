import ast
import string

def count_variables(node):
    sum = 0
    vars = dict()
    for n in ast.walk(node):
        if isinstance(n, ast.Attribute):
            tmp= n.attr
            s = ""
            while isinstance(n.value, ast.Attribute):
                s = n.value.attr + "." +s
                n = n.value
            s = n.value.id + "." +s
            if s[:-1] in vars.keys():
                vars[s[:-1] ] -= 1
            else:
                vars[s[:-1] ] = -1
            s+=tmp

            if s not in vars.keys():

                vars[s] = 1
            else:
                vars[s] +=1
        elif isinstance(n, ast.Constant):
            if str(n.value) not in vars.keys():

                vars[str(n.value)] = 1
            else:
                vars[str(n.value)] +=1
        elif isinstance(n, ast.Name):

            if   n.id not in vars.keys():
                vars[n.id] = 1
            else:
                vars[n.id] +=1

    return vars


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

    return oprs
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
    return loops
def count_try_excent(node):
    tryes = {
        "try..except..finally":0
    }
    for n in ast.walk(node):
        if isinstance(n, ast.Try):
            tryes["try..except..finally"]+=1
    return tryes
def count_func(node,vars):
    funcs = {
        "return":0,
        "yeild" :0,
        "yeild from":0,
        "lambda":0,
        "pass":0,
        "assert":0,
        "with":0,
        "class":0,
        "def":0
    }
    for n in ast.walk(node):
        if isinstance(n, ast.ClassDef):
            funcs["class"]+=1
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
                if n.func.attr  in vars:
                    vars[n.func.attr] -= 1

                if n.func.attr not in funcs:
                    funcs[n.func.attr]=1
                else:
                    funcs[n.func.attr] += 1
            elif isinstance(n.func, ast.Name):#functions
                if n.func.id in vars:
                    vars[n.func.id]-=1
                if n.func.id not in funcs:
                    funcs[n.func.id]=1
                else:
                    funcs[n.func.id] += 1
        #???do we need to add a function declaration to the operands????
        if isinstance(n, ast.FunctionDef):
            funcs["def"]+=1
            if n.name not in funcs:
                funcs[n.name] = 1
            else:
                funcs[n.name] += 1
        if isinstance(n, ast.ClassDef):
            funcs["class"]+=1
            if n.name not in funcs:
                funcs[n.name] = 1
            else:
                funcs[n.name] += 1

    return funcs
def count_skobki(text, funcs):
    last_word = ""
    new_word = ""
    res = 0
    temp = (3+4)*4
    for char in text:
        if  char not in string.ascii_letters and new_word != "":
            last_word = new_word
            new_word = ""
        elif char == "(" and ((new_word == "" and last_word not in funcs) or new_word not in funcs):
            res+=1
        else:
            new_word+=char
    return res





def parse_file(file_path):
    with open(file_path, 'r') as f:
        text= f.read()
        tree = ast.parse(text)


    vars = count_variables(tree)
    loops = count_loops(tree)
    tryes = count_try_excent(tree)
    opr = count_binaty_opr(tree)
    funcs = count_func(tree, vars)
    skobki = count_skobki(text, funcs)
    print(f"vars  : {vars}\n loops: {loops}\n opr: {opr}\n funcs {funcs}\n tryes: {tryes} skobki: {skobki}")
if __name__ == "__main__":
    file_path = "example.py"
    parse_file(file_path)