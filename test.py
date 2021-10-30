def importRules():
    with open('rules.txt') as f:
        ruleList = f.read().splitlines()
    print(ruleList)
    f.close()
    return ruleList


def main():
    ruleList = importRules()
    print(str(ruleList).split(","))
if __name__ == "__main__":
    main()
