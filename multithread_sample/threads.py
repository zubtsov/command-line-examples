from subprocess import PIPE, Popen, call
from threading import Thread, current_thread

def writef(count):
    for i in range(count):
        call(["multithread_sample/file_writer.sh", "tmp_buffer"])
        print "File have been written in thread " + current_thread().name


def readf(count):
    for i in range(count):
        call(["multithread_sample/file_reader.sh", "tmp_buffer"])
        print "File have been read in thread " + current_thread().name


try:
    files=Popen("multithread_sample/get_list_of_files.sh", stdin=PIPE, stdout=PIPE).communicate()[0].strip().split('\n')

    call(["rm", "tmp_buffer"])

    call(["mkfifo", "tmp_buffer"])

    print "Creating threads..."
    t1=Thread(target=writef, args=[10])
    t2=Thread(target=readf, args=[10])

    print "Starting first thread"
    t2.start()
    print "Starting second thread"
    t1.start()

    print "Joining..."
    t1.join()
    t2.join()
finally:
    call(["rm", "tmp_buffer"])
    print ""
