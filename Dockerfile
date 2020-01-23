FROM continuumio/miniconda3
MAINTAINER 4oh4

WORKDIR /

COPY estimate_pi.py estimate_pi.py
COPY estimate_pi_for_loop.py estimate_pi_for_loop.py
COPY run_benchmark.py run_benchmark.py

RUN pip install numpy

CMD python run_benchmark.py