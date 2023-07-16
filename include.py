import sys
import re
import logging
FORMAT = "[ %(asctime)s ] %(message)s"
logging.basicConfig(filename="compiler.log", level=logging.INFO, format=FORMAT);
#main vars
this = sys.argv[0]
argsv = sys.argv[1:]
directivePrefix = '$'


directive = "include"
regex = re.compile(rf'\{directivePrefix}{directive[0]}\(".+?"\)\s*?', re.DOTALL)

def findIncludeDirectives(arquivo: str) -> list[tuple[str, int]]:
    with open(arquivo, "r") as f:
        content = f.readlines();

        logging.info(f"Lines already was read from {arquivo}: {content};\n")



    lines = [(line, lineno) for lineno, line in enumerate(content, start=1)];

    logging.info(f"Lines enumerated: {lines};\n")


    tlines = [];


    for line in lines:
        if regex.match(line[0]):
            tlines.append(line);


    logging.info(f"$include directives lines found: {tlines}")
    return tlines;





def extractFileName(include_directive: str) -> str:
    filere = r'".*?"'
    value = re.findall(filere, include_directive);
    logging.info(f"File name extracted succesfully: {value[0]}")
    return value[0][1:-1]




def readFile(file: str) -> str:
    with open(file) as f:
        content = f.read();
    return content;




def processInclude(line: tuple[str, int]):
    FILE_NAME = extractFileName(line[0])
    FILE_CONTENT = readFile(FILE_NAME)
    CODE_OBJECT = compile(FILE_CONTENT, FILE_NAME, 'exec')
    logging.debug("Code compiled sucessufully!;\n")

    exec(CODE_OBJECT, globals())

def execMain():
    FILE_NAME = argsv[0]
    FILE_CONTENT = readFile(FILE_NAME).replace('$include', '#');
    CODE_OBJECT = compile(FILE_CONTENT, FILE_NAME, 'exec')
    exec(CODE_OBJECT, globals())

def main()->None:
    direcs = findIncludeDirectives(argsv[0]);
    for direc in direcs:
        processInclude(direc)
    execMain()



if __name__ == "__main__":
    main();
