# ipyloglite &emsp; [![PyPi]][pypi-url]  [![License Apache-2.0]][apache-2.0] [![License MIT]][mit] [![CI Status]][ci-status]

[PyPI]: https://img.shields.io/pypi/v/ipyloglite
[pypi-url]: https://pypi.org/project/ipyloglite

[License Apache-2.0]: https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg
[apache-2.0]: https://opensource.org/licenses/Apache-2.0

[License MIT]: https://img.shields.io/badge/License-MIT-yellow.svg
[mit]: https://opensource.org/licenses/MIT

[CI Status]: https://img.shields.io/github/actions/workflow/status/juntyr/ipyloglite/ci.yml?branch=main&label=CI
[ci-status]: https://github.com/juntyr/ipyloglite/actions/workflows/ci.yml?query=branch%3Amain

`ipyloglite` is a Python package to capture `console.log` and frieds and forward them to cell outputs in a JupyterLite notebook running a Pyodide Python kernel.

## Installation

### pip

The `ipyloglite` package is available on the Python Package Index (PyPI) and can be installed using
```bash
pip install ipyloglite
```
This command can also be run inside a conda environment to install `ipyloglite` with conda.

### From Source

First, clone the git repository using
```bash
git clone https://github.com/juntyr/ipyloglite.git
```
or
```bash
git clone git@github.com:juntyr/ipyloglite.git
```

Next, enter the repository folder and use `pip` to install the program:
```bash
cd ipyloglite && pip install .
```

## License

Licensed under either of

* Apache License, Version 2.0 ([`LICENSE-APACHE`](https://github.com/juntyr/phepy/blob/main/LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
* MIT license ([`LICENSE-MIT`](https://github.com/juntyr/phepy/blob/main/LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.
