def obj_to_xml(obj, depth=0):
    s_out = ''
    if isinstance(obj, dict):
        return dict_to_xml(depth, s_out, obj)
    elif not isinstance(obj, str) and hasattr(obj, "__iter__"):
        return iter_to_xml(depth, s_out, obj)
    elif depth == 0:
        return object_to_xml(obj)
    else:
        return obj


def object_to_xml(obj):
    only = str(type(obj))
    only = only[only.find(' ') + 2:-2]
    return f'<obj type={only}>{obj}</obj>'


def make_sout(depth, k, internal, fl):
    if fl == True:
        return depth * '  ' + f"<item key='{k}' type='str'>" f"{internal}</item>\n"
    else:
        return depth * '  ' + f"<item key='{k}'>{internal}</item>\n"


def dict_to_xml(depth, s_out, obj):
    depth += 1
    for k, val in obj.items():
        fl = 0
        if val == obj:
            raise ValueError("infinite cycle")
        if isinstance(internal := obj_to_xml(val, depth + 1), str) and internal.isdigit():
            fl = 1
            s_out += make_sout(depth, k, internal, fl)
        else:
            s_out += make_sout(depth, k, internal, fl)
    if not s_out:
        return f'<dict>{s_out}</dict>'
    else:
        begin = '' if depth == 1 else '\n'
        return begin + (depth - 1) * '  ' + f'<dict>\n{s_out}' + (depth - 1) * '  ' + '<dict>\n' + (depth - 2) * '  '


def iter_to_xml(depth, s_out, obj):
    depth += 1
    local = str(type(obj))
    st_from = local.find(' ') + 2
    local = local[st_from:-2]
    for elem in obj:
        if elem == obj:
            raise ValueError(f"cycle reference in {local} cannot be handled")
        if isinstance(internal := obj_to_xml(elem, depth + 1), str) and internal.isdigit():
            s_out += depth * '  ' + f"item type='str'{internal}</item>\n"
        else:
            s_out += depth * '  ' + f'<item>{internal}</item>\n'
    if not obj:
        return f'<{local}>' + s_out + f'</local_type>'
    else:
        begin = '' if depth == 1 else '\n'
        return begin + (depth - 1) * '  ' + f'<{local}>\n' + s_out + (depth - 1) * '  ' + f'</{local}>\n' + (
                    depth - 2) * '  '


def xml_to_file(obj, filename: str):
    with open(f'{filename}', 'w+', encoding="utf8") as f:
        f.write(obj_to_xml(obj))
        f.close()


if __name__ == '__main__':
    obj = [{3: 4}, ([9])]
    print(obj)
    print(obj_to_xml(obj))
    xml_to_file(obj, 'file.xml')
