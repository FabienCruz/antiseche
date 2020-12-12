import file

dir_content = file.Dir('content/')
dir_files = dir_content.list_files('md')

print (dir_files)


