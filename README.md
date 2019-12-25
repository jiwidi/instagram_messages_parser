# Instagram messager json to csv and sample exploration

Download your personal data with https://help.instagram.com/181231772500920 and move it into the data/ folder of the repo

This repo contains a script `processJSON.py` that will help you process instagram private messages JSON file `messages.json` to csv files that easily readble with pandas. I also attached a notebook `Explore_conversation.ipynb` to showcase a basic analysis, the rest is up to you.

To run `processJSON.py` specify your usename and the filepath for the messages.json

```python
python processJSON.py --f filepath --f username
```
