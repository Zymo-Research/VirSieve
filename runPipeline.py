import os
import sys
import virsieveSupport


def getTargetDirectory():
    targetDirectory = sys.argv[1]
    if not os.path.isdir(targetDirectory):
        raise NotADirectoryError("Unable to find target directory at %s" %targetDirectory)
    return targetDirectory


def runPipeline(targetDirectory):
    for containerTag in virsieveSupport.containerOrder:
        cmd = "docker container run --rm -v %s:/data %s" %(targetDirectory, containerTag)
        print(cmd)
        exitCode = os.system(cmd)
        if exitCode != 0:
            raise RuntimeError("Container run for %s failed with exit code %s" %(containerTag, exitCode))
    print("Pipeline complete")


if __name__ == "__main__":
    targetDirectory = getTargetDirectory()
    runPipeline(targetDirectory)