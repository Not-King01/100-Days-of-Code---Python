def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

def echo (name):
    return name + name

def title(name):
    return name.title()

print(title(echo("King")))