def get_xml_string(obj, level = 0):
    res_str = ''
    if isinstance(obj, dict):
        level += 1
        for k, v in obj.items():
            if v == obj:
                raise ValueError("Cyclic reference in dict")
            inner_elem=get_xml_string(v, level+1)
            if isinstance(get_xml_string(v, level+1),str) and inner_elem.isdigit():
                res_str += level * '\t' + f"<item key='{k}' type='str'>{inner_elem}</item>\n"
            else:
                res_str+= level*'\t'+ f"<item key='{k}'>{inner_elem}</item>\n"
        if not res_str:
            return f'<dict>{res_str}</dict>'
        else:
            line_start = '' if level == 1 else '\n'
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        level+=1
        local_type = str(type(obj))
        local_type = local_type[local_type.find(' ')+2:-2]
        for elem in obj:
            if elem == obj:
                raise ValueError("cyclic reference")
            inner_elem = get_xml_string(elem,level+1)
            if not isinstance(get_xml_string(elem,level+1),str) and inner_elem.isdigit:
                res_str += level * '\t' + f"<item type='str'>{inner_elem}</item>\n"
            else:
                res_str += level * '\t' + f"<item>{inner_elem}</item>\n"
        if not obj:
            return f'<{local_type}>'+res_str+ f'</{local_type}>'
        else:
            line_start = '' if level == 1 else '\n'
            return line_start + (level - 1) * '\t' + f'</{local_type}>\n' +res_str+(level -1)*'\t' +f'</{local_type}>'+ (level - 2) * '\t'
    elif level == 0:
        single_type = str(type(obj))
        single_type = single_type[single_type.find(' ')+2:-2]
        return  f'<obj type={single_type}>{obj}</obj>'
    else:
        return obj

a = {'a': 3, 45: ['abc', 6, '56']}
get_xml_string(a)