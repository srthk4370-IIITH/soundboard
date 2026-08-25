# Run the Soundboard

## Start the local server

Open a terminal in this folder and run:

```bash
python server.py
```

The soundboard will be available at:

```text
http://localhost:8000
```

The server listens only on your computer at `127.0.0.1` using port `8000`.

Stop the server at any time with `Ctrl+C` in the terminal where it is running.

## Add sounds

Place `.mp3` and `.m4a` files in this same folder, beside `index.html` and `server.py`. Refresh the browser and the files will appear automatically as sound buttons.

## Change the port

If port `8000` is already in use, open `server.py` and find this line:

```python
address = ("127.0.0.1", 8000)
```

Replace `8000` with an available port, for example `8080`:

```python
address = ("127.0.0.1", 8080)
```

Start the server again, then open the matching address:

```text
http://localhost:8080
```

You do not need to change anything in `index.html`, because it requests `/sounds` from whichever local server and port loaded the page.
