def cut(gene: str, prefix, suffix):
    gene = gene.replace(prefix, " ")
    gene = gene.replace(suffix[0], " ")
    gene = gene.replace(suffix[1], " ")
    gene = gene.replace(suffix[2], " ")
    gene = gene.split()
    gene.sort(key=lambda x: (len(x), x))
    return gene


def main():
    prefix = input()
    suffix = input().split()
    gene = input()
    x = gene.count(prefix)
    gene = gene.replace(prefix, " ")
    y = [gene.count(i) for i in suffix]
    if x == -1 or sum(y) == 0:
        print("No gene")
    elif x == sum(y):
        print("\n".join(cut(gene, prefix, suffix)))
    else:
        print("No gene")


if __name__ == "__main__":
    main()
