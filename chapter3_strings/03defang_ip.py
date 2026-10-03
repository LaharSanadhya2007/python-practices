def defang_ip(d):
    return d.replace("192.168.0.1","192[.]168[.]0[.]1")
print(defang_ip("192.168.0.1"))