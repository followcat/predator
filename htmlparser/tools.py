def queryString(str):
    if str.find("?") == -1:
        return -1
    else:
        params_str = str.split("?")[1]
        result = dict()
        if params_str.find("&") != -1:
            params_list = params_str.split("&")
        else:
            params_list = params_str
        for e in params_list:
            arr = e.split("=")
            result[arr[0]] = arr[1]
        return result
