def main():
    file_name = input ("File name: ").lower().strip()
    print (file_type(file_name))

def file_type(file_name):
    if file_name.endswith('.gif'):
        return ("image/gif")
    elif file_name.endswith('.jpg'):
        return ("image/jpeg")
    elif file_name.endswith('.jpeg'):
        return ("image/jpeg")
    else:
        return (file_kind(file_name))


def file_kind(file_name):
    file, type = file_name.split('.')
    print (file, type)

    match type:
        case 'png':
            return ('image/png')
        case 'pdf':
            return ('application/pdf')
        case 'txt':
            return ('text/plain')
        case 'zip':
            return ('application/zip')
        case _:
            return ("Invalid file format!")


