import sys

from upload import Upload

argvs = sys.argv

test = Upload()
print(test.upload(str(argvs[1])))

