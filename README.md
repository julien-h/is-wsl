# ![](https://docs.python.org/3/_static/py.png) is_wsl

Python utility to check whether the current script runs inside Windows' WSL.

## Install

```
pip install iswsl
```
## Usage
Here's how to use it:

```python
from iswsl import is_wsl

if is_wsl():
    print('Running inside WSL')
else:
    print('Running outside WSL')
```
## Licence
MIT © Julien Harbulot

Inspired from the node version [is-wsl](https://github.com/sindresorhus/is-wsl) by Sindre Sorhus
