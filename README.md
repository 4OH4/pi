# pi
Python estimate of pi using random sampling - long-running process for benchmarking

To run the benchmark (vectorised and non-vectorised code):

    python run_benchmark.py

To run the benchmark in Docker:

    docker run -it 4oh4/pi

Typical output:

```
...
Round 10 of 10:
Estimating pi using random sampling (vectorised), n=1000000
Estimate of pi: 3.141100
Estimate of pi: 3.138712
Estimate of pi: 3.140220
Estimate of pi: 3.141856
Estimate of pi: 3.143404
Estimate of pi: 3.140552
Estimate of pi: 3.141676
Estimate of pi: 3.142624
Estimate of pi: 3.143444
Estimate of pi: 3.142080
10 repeats: 0.689 secs = 0.0689 secs/run
Estimating pi using random sampling (non-vectorised), n=1000000
Estimate of pi: 3.141900
Estimate of pi: 3.141016
Estimate of pi: 3.142372
Estimate of pi: 3.141868
Estimate of pi: 3.142340
Estimate of pi: 3.140564
Estimate of pi: 3.144160
Estimate of pi: 3.142312
Estimate of pi: 3.141284
Estimate of pi: 3.144424
10 repeats: 15.640 secs = 1.5640 secs/run
Final results:
Vectorised implementation: 0.507 seconds (0.424 - 0.689)
Non-vectorised implementation: 14.607 seconds (13.003 - 16.027)
```
