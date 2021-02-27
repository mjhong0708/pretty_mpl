# prettympl

A simple package for prettier matplotlib plot

## Features
- 별도의 설치 없이 리눅스에서도 사용 가능한 다양한 폰트 내 (Arial, Lato, Times new roman 등)
- `set_style` 함수를 통한 플롯 스타일 설정


## Requirements
- python >= 3.6
- matplotlib

## Installation
1. 소스 코드를 다운받고 `setup.py`가 있는 경로로 이동
2. 해당 경로에서 `pip install .` (python 3 버전을 명시해야 할 경우는 `python3 -m pip install .`)

## Usage
`set_style` 함수를 사용하여 해당 스크립트에서 사용할 스타일을 결정하면 된다.
함수에 대한 설명은 `help(set_style)`로 확인 가능함.
```python3
import matplotlib.pyplot as plt
from prettympl import set_style
import numpy as np

x1 = np.linspace(0, np.pi / 2, 200)
x2 = np.random.uniform(0, np.pi / 2, 30)
y1 = np.cos(x1)
y2 = np.sin(x1)
y3 = np.random.uniform(-1,1,30)
y4 = np.random.uniform(-1,1,30)

set_style(style='simple_white') # Style 작성
plt.figure()
plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.plot(x1, y1, label='cos')
plt.plot(x1, y2, label='sin')
plt.plot(x2, y3, 'o', label='scatter1')
plt.plot(x2, y4, 's', mfc='none', label='scatter2')
plt.ylim(-1.5, 1.5)
plt.legend(edgecolor='none')
plt.tight_layout()   # 반드시 이 함수를 사용할 것을 권장.
plt.savefig("prettympl.jpg", dpi=600)
plt.show()
```
결과는 다음과 같음.
![test](./prettympl.jpg)