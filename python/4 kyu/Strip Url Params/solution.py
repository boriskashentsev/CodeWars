def strip_url_params(url, params_to_strip = []):
    index = url.find("?")
    if index == -1 :
        # no parameters
        return url
    else :
        # split to parameters, preserve the oreder
        stringURL = url[:index+1]
        stringParameters = url[index+1:]
        arrayParameters = stringParameters.split('&')

        dictionary = {}
        paramOrder = []
        for param in arrayParameters:
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            if key not in dictionary and key not in params_to_strip:
                paramOrder.append(key)
                dictionary[key] = value

        stringParameters = ''
        for index, key in enumerate(paramOrder):
            if index == 0:
                stringParameters += key + '=' + dictionary[key]
            else:
                stringParameters += '&' + key + '=' + dictionary[key]

return stringURL + stringParameters
