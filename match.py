def http_error(status):
    match status:
    case 400:
        return "Bad request"
    case 404:
        return "Not found"
    case 418:
        return "I'am joshua "
    case _:
       return "something went wrong with the internet"
