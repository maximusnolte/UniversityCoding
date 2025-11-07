import time
def dezimal_to_binary(dezimal):
    dezimal = int(dezimal)
    start_t = time.perf_counter()
    out = ""
    p = 1
    while 2** (p+1) <= dezimal:
        p +=1
    print("Benötigte Bits: " + str(p))

    for i in range(p,-1,-1):
        digit = 2**i
        if dezimal >= digit:
            if(dezimal -digit >= 0):
                dezimal = dezimal - digit
                out = out + "1"
        else:
            out = out + "0"
    out = out.lstrip("0")
    print(out)

    end_t = time.perf_counter()
    print(f"(in {end_t - start_t:.10f} Sekunden)")

if __name__ == '__main__':
    while True:
        dezimal = input("Bitte Dezimal: ")

        dezimal_to_binary(dezimal)
