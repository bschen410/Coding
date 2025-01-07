def is_prime(n):
    if n == 2:
        return True
    elif n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def findGene(prefix, suffix, seq):
    if seq[:3] == prefix and len(seq) > 3:
        seq = seq[3:]
        sufIdx = min(
            seq.find(suffix[i], 1) for i in range(3) if seq.find(suffix[i], 1) > 0
        )
        if is_prime(seq[:sufIdx]):
            yield seq[:sufIdx]
        yield from findGene(prefix, suffix, seq[sufIdx + 3 :])
    else:
        return


def main():
    prefix = input()
    suffix = input().split()
    seq = input()
    mix = prefix + suffix[0] + suffix[1] + suffix[2] + seq
    if set(mix) not in ["A", "C", "G", "T"]:
        print("Input error")
        exit()
    try:
        result = findGene(prefix, suffix, seq)
        result = sorted(list(result), key=lambda x: (len(x), x))
        print("\n".join(result))
    except:
        print("No gene")


if __name__ == "__main__":
    main()
