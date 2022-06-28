#valid json {{{}}} - valid, {}{}{} - not valid, {{}{}{}{}{}} - valid, {{{}}}{}-not valid

def valid(str):

    if len(str) % 2 != 0:
        # print("First return")
        return False

    openp = ['{']
    stackl = []

    for index, para in enumerate(str):
        if para in openp:
            stackl.append(para)
        else:
            if len(stackl) == 0:
                # print("Second return")
                return False
            else:
                stackl.pop()
                # print(str)
                if len(stackl) == 0 and index != len(str)-1:
                    #print("Third return")
                    return False
    return True
