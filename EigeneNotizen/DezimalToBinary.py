def dezimal_to_binary(dezimal):
    out = ""
    for i in range(dezimal,-1,-1):
        digit = 2**i
        if dezimal >= digit:
            if(dezimal -digit >= 0):
                dezimal = dezimal - digit
                out = out + "1"
        else:
            out = out + "0"
    out = out.lstrip("0")
    print(out)

if __name__ == '__main__':
    dezimal_to_binary(18)