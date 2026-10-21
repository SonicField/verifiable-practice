# Current check04 setup failure

`python3 vp/artefacts/R-000013/check-current-02.py current-check-04` exited1 before an attempt directory or any results were created: `/usr/local/bin/python3` cannot import `yaml` (`ModuleNotFoundError`). This is a runtime dependency/setup failure, not a source verdict. Retry with the system Python that provides the already installed parser; preserve this failure and identify that executable in successful results.
