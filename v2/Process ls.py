def process_ls(output):
    l = output.splitlines()
    l = [i.split(maxsplit=8) for i in output.splitlines()]
    m = [i for i in line if i[1] == '1']
    m.sort(key = lambda x: int(x[4]), reverse=True)
    return [i[8] for i in m]