# network-benchmark
**This piece of code is originanly forked from FlipperPA: https://github.com/FlipperPA/latency-tester**

[![Build Status](https://travis-ci.org/matthieu-lapeyre/network-benchmark.svg?branch=master)](https://travis-ci.org/matthieu-lapeyre/network-benchmark)

You can quickly evaluate the latency of your network and obtain mean, std, percentile, timeout data. 
Usage is `python network_test.py <ip> <n_sample> <timeout>` for example you can run:
```console
python network_test.py 192.168.0.1 50 1300
```
and the output will be something like this:

``` console
mean latency: 19.0138426854 ms
std latency: 91.3184052069 ms
99% latency: 7.4905 ms
95% latency: 7.4905 ms
timeout: 0.2 %
```
