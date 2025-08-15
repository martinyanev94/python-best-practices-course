class RealSubject:
    def request(self):
        return "Real Subject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy: Logging before request.")
        return self.real_subject.request()

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)

print(proxy.request())
