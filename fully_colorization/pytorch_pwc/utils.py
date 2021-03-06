import os
import numpy


# +
def get_names(dir='./'):
    old_names = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    old_names.sort()
    new_names = [None]*len(old_names)
    for idx in range(len(old_names)):
        new_names[idx] =os.path.join(dir,old_names[idx])
    return new_names


def store_flow(flow, filename='./data/result.flo'):
    objOutput = open(filename, 'wb')

    numpy.array([ 80, 73, 69, 72 ], numpy.uint8).tofile(objOutput)
    numpy.array([ flow.shape[2], flow.shape[1] ], numpy.int32).tofile(objOutput)
    numpy.array(flow.numpy().transpose(1, 2, 0), numpy.float32).tofile(objOutput)

    objOutput.close()
    return 



