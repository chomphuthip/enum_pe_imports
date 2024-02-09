import pefile
import os

def create_log(filename):
    return open(filename[:-4] + '.log', 'w')

for filename in os.listdir('./'):
    if '.sys' not in filename:
        continue
    sysfile = pefile.PE(filename)
    log_handle = create_log(filename)
    log_handle.write(filename + '\n')
    for library in sysfile.DIRECTORY_ENTRY_IMPORT:
        log_handle.write('[+] ' + library.dll.decode('utf-8') + ' imports:\n')
        for function in library.imports:
            log_handle.write('\t' + function.name.decode('utf-8') + '\n')
