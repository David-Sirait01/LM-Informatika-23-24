import numpy

class nums:
    class max:
        class signed:
            int_8 = numpy.iinfo(numpy.int8).max
            int_16 = numpy.iinfo(numpy.int16).max
            int_32 = numpy.iinfo(numpy.int32).max
            int_64 = numpy.iinfo(numpy.int64).max
        class unsigned:
            uint_8 = numpy.iinfo(numpy.uint8).max
            uint_16 = numpy.iinfo(numpy.uint16).max
            uint_32 = numpy.iinfo(numpy.uint32).max
            uint_64 = numpy.iinfo(numpy.uint64).max
    class min:
        class signed:
            int_8 = numpy.iinfo(numpy.int8).min
            int_16 = numpy.iinfo(numpy.int16).min
            int_32 = numpy.iinfo(numpy.int32).min
            int_64 = numpy.iinfo(numpy.int64).min
        class unsigned:
            uint_8 = numpy.iinfo(numpy.uint8).min
            uint_16 = numpy.iinfo(numpy.uint16).min
            uint_32 = numpy.iinfo(numpy.uint32).min
            uint_64 = numpy.iinfo(numpy.uint64).min