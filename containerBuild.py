import os
import virsieveSupport


def buildContainers():
    contentRootFolder = os.path.dirname(os.path.realpath(__file__))
    for tag, context in virsieveSupport.containerTagTable.items():
        cmd = "docker image build -t %s %s" % (tag, os.path.join(contentRootFolder, context))
        print("RUN: %s" % cmd)
        returnCode = os.system(cmd)
        if returnCode != 0:
            raise RuntimeError("Failed to build container %s with return code %s" % (tag, returnCode))
    print("All containers build successfully")
    return


if __name__ == "__main__":
    buildContainers()