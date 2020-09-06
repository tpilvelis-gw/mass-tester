import os

from src.Glasswall import Glasswall

def writeFile(fileName, outputDir, content):
    fileHandler = open(os.path.join(outputDir, fileName), "wb")
    fileHandler.write(content)
    fileHandler.close()


def main():
    print("Loading Library...")
    #  Load Glasswall Lib
    if os.path.isfile("lib/glasswall.classic.dll"):
        gw = Glasswall("lib/glasswall.classic.dll")
        print("Done!")
    else:
        print("Engine Could Not Be Loaded...")
        return

    os.makedirs("out")

    #  GWFileConfigXML Test
    configFile = open("config.xml", "r")
    xmlContent = configFile.read()
    configFile.close()

    # Apply the content management configuration
    configXMLResult = gw.GWFileConfigXML(xmlContent)

    if configXMLResult.returnStatus != 1:
        print("Failed to apply the content management configuration for the following reason: " + gw.GWFileErrorMsg())
        return

    for root, folders, files in os.walk("data"):
        for eachFile in files:
            filepath = os.path.join(root, eachFile)

            print("Processing file: " + filepath)

            # We use the extension as the file type of the file to be processed
            fileExtension = filepath.split(".")[1]

            # Process the file in File to Memory Protect mode
            manageAndProtectResult = gw.GWFileProtect(filepath, fileExtension)

            if manageAndProtectResult.returnStatus == 1:
                writeFile(eachFile, "out", manageAndProtectResult.fileBuffer)

            # Analyse the file in File to Memory Analysis mode
            analysisResult = gw.GWFileAnalysisAudit(filepath, fileExtension[1:])
            writeFile(eachFile + ".xml", "out", analysisResult.fileBuffer)

    gw.GWFileDone()



def test_run_test():
    file_path = os.path.join("data", "test.bmp")
    engine_path = os.path.join("lib", "glasswall.classic.dll")

    if not os.path.isfile(engine_path):
        print("engine path is invalid...")
        return
    
    print("Loading Library...")
    gw = Glasswall(engine_path)
    print("Done!")

    configFile = open("config.xml", "r")
    xmlContent = configFile.read()
    configFile.close()

    # Apply the content management configuration
    configXMLResult = gw.GWFileConfigXML(xmlContent)

    if configXMLResult.returnStatus != 1:
        print("Failed to apply the content management configuration for the following reason: " + gw.GWFileErrorMsg())
        return

    print("Processing file: " + file_path)
    _, fileExtension = os.path.splitext(file_path)

    manageAndProtectResult = gw.GWFileProtect(file_path, fileExtension[1:])



if __name__ == "__main__":
    main()