import sys

from JackTokenizer import JackTokenizer

def main():
    args = sys.argv

    if(args.__len__() < 2):
        print("Digite o nome do arquivo jack sem a extensão.")
        sys.exit(1)
    
    print("Realizando análise léxica do arquivo " + args[1] + ".jack")

    tokenizer = JackTokenizer(args[1])
    tokenizer.content()
        
        

if __name__ == "__main__":
    main()