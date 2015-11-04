import numpy
import pexpect


class NetworkLatencyBenchmark(object):
    def __init__(self, ip, timeout=1200):
        object.__init__(self)

        self.ip = ip
        self.interval = 0.5

        ping_command = 'ping -i ' + str(self.interval) + ' ' + self.ip
        self.ping = pexpect.spawn(ping_command)

        self.ping.timeout = timeout
        self.ping.readline()  # init

        self.wifi_latency = []
        self.wifi_timeout = 0
        self.print_status = True

    def run_test(self, n_sample=100):
        for n in xrange(n_sample):
            p = self.ping.readline()

            try:
                ping_time = float(p[p.find('time=') + 5:p.find(' ms')])
                self.wifi_latency.append(ping_time)
                if self.print_status:
                    print 'test:', n + 1, '/', n_sample, ', ping latency :', ping_time, 'ms'

            except:
                self.wifi_timeout = self.wifi_timeout + 1
                print 'timeout'

        self.wifi_timeout = self.wifi_timeout / float(n_sample)
        self.wifi_latency = numpy.array(self.wifi_latency)

    def get_results(self):
        print 'mean latency:', numpy.mean(self.wifi_latency), 'ms'
        print 'std latency:', numpy.std(self.wifi_latency), 'ms'
        print '99% latency:', numpy.percentile(self.wifi_latency, 50), 'ms'
        print '95% latency:', numpy.percentile(self.wifi_latency, 50), 'ms'
        print 'timeout:', self.wifi_timeout * 100, '%'


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print "usage: python network_latency_test.py <ip> <n_sample> <timeout>"
        sys.exit(1)

    ip = sys.argv[1]
    n_sample = int(sys.argv[2]) 
    timeout = int(sys.argv[3]) 
    

    network = NetworkLatencyBenchmark(ip,timeout)
    network.print_status = False

    network.run_test(n_sample)
    network.get_results()
