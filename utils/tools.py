def replace_tnr(string):
    result = string
    result = result.replace('\t', '')
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    return result
