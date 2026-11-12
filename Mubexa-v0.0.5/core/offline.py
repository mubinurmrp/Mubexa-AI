from datetime import datetime
import ast
import operator
import subprocess
import re


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):
        if type(node.op) in OPS:
            return OPS[type(node.op)](
                safe_eval(node.left),
                safe_eval(node.right)
            )

    raise ValueError()


def calculate(text):
    expr = re.sub(r"[^0-9+\-*/().]", "", text)

    if not re.search(r"\d[\+\-\*/]\d", expr):
        return None

    try:
        result = safe_eval(
            ast.parse(expr, mode="eval")
        )
        return f"উত্তর {result}"

    except Exception:
        return None


def offline_command(text):

    t = text.lower()

    # সময়
    if "সময়" in t or "সময়" in t:
        return "এখন সময় " + datetime.now().strftime("%I:%M %p")

    # তারিখ
    if "তারিখ" in t:
        return "আজ " + datetime.now().strftime("%d-%m-%Y")

    # ক্যালকুলেটর
    calc = calculate(text)
    if calc:
        return calc

    # ব্যাটারি
    if "ব্যাটারি" in t or "battery" in t:
        try:
            r = subprocess.run(
                ["termux-battery-status"],
                capture_output=True,
                text=True
            )
            return r.stdout
        except:
            return "ব্যাটারি তথ্য পাওয়া যায়নি।"

    return None

