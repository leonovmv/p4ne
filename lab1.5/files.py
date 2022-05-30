import glob
ip = set()
for file_name in glob.glob("config_files\*.txt"):
    with open(file_name) as f:
        for line in f:
            if line.find("ip address") == 1:
                ip.add(line.replace("ip address", "").strip())
for i in ip:
    print(i)