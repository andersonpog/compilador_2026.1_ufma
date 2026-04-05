import sys

def main():
    args = sys.argv

    if(args.__len__() > 1):
        print("Realizando análise léxica do arquivo " + args[1] + ".jack")
    else:
        print("Digite o nome do arquivo jack sem a extensão")

if __name__ == "__main__":
    main()