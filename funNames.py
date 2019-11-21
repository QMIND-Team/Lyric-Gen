import csv;
import os;
import sys;

class CVSIO():
    def __init__(self, inputFile, outputFile):
        self.dataName = inputFile;
        self.outputName = outputFile;

        # Opens files
        self.data = open(self.dataName, 'r', encoding='utf8');
        self.output = open(self.outputName, 'w', encoding='utf8');
        self.writer =  csv.writer(self.output, delimiter=',', lineterminator='\n');

        # Creates header for the output file
        self.write(("Seed", "Char", "ASCII"));

    def close(self, file):
        file.close();

    def write(self, elems):
        self.writer.writerow(elems);

    def size(self, fileName):
        return os.path.getsize(self.fileName);

    def fI(self):
        return self.data;

    def fO(self):
        return self.output;

    def readFile(self):
        for line in self.fI():
            lineLength = len(line);  
            # If we want to get ride of new lines: line = line.strip()

            # Ensures that the line has at least 21 lines
            if (lineLength >= 21):
                for i in range(0, lineLength - 20):
                    # Writes the seed, char, and ascii value respectively to output file
                    self.write((line [i:i+20], line [i+20], ord(line [i+20])));


def main():
    # Input and Output filenames are read from the command line
    inputFile = sys.argv [1]
    outputFile = sys.argv [2]
    
    # Creates IO Class and reads the file
    ModelIO = CVSIO(inputFile, outputFile);
    ModelIO.readFile();

    # Closes files
    ModelIO.close(ModelIO.fI());
    ModelIO.close(ModelIO.fO());
    print("Done");

if __name__ == "__main__":
    main();

