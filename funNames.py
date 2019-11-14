import csv;
import os;
import sys;

class CVSIO():
    def __init__(self, inputFile, outputFile):
        self.dataName = inputFile;
        self.outputName = outputFile;

        self.data = open(self.dataName, 'r', encoding='utf8');
        self.output = open(self.outputName, 'w', encoding='utf8');
        self.writer =  csv.writer(self.output, delimiter=',', lineterminator='\n');
        self.write(("Seed", "Char"));

    def close(self, file):
        self.file.close();

    def write(self, elems):
        self.writer.writerow(elems);

    def size(self, fileName):
        return os.path.getsize(self.fileName);

    def fnameI(self):
        return self.outputName;

    def fnameO(self):
        return self.dataName;

    def readFile(self):
        for line in self.dataName:
            lineLength = line.length();
            if (lineLength >= 21):
                for i in range(0, lineLength - 20):
                    self.write((line [i:i+20], line [i+20]));


def main():
    ModelIO = CVSIO(sys.argv[1], sys.argv[2]);
    ModelIO.readFile;

if __name__ == "__main__":
    main();

