# Duck Typing : It is a concept where the type of an object is determined by it's behaviour 
# not by it's class.Duck Typing is design pattern.

# If it looks like duck, walks like duck and quakes like duck then it must be the duck
# sir konkan example of ajji -> this is opposite of duck typing

class InkjetPrinter:
    def PrintDocument(self, document):
        print("InkjetPrinter printing : ", document)

class LaserPrinter:
    def PrintDocument(self, document):
        print("LaserPrinter printing : ", document)

class PDFWriter:
    def PrintDocument(self, document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()