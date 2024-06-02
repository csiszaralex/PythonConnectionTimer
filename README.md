# Python connection time tester and visualizer

## Usage:

Prerequiests: Need to be installed python on your PC

1. Install required python packages:

```bash
pip install matplotlib pandas openai python-dotenv
```

2. Add the OpenAI API key:

- Copy `.env.example` and rename it to `.env`
- Replace the _OPENAPIKEY_ value to your real API key

3. Run `ai.py` several times with different senteces

_Replace the `SZO` variable_

4. Run `draw.py` to visualize your response times based the charters count

_If you want to generate the image without opening it in new windows just comment the last line (`plt.show()`) and comment out the `plt.savefig("grafikon.png")` line_
