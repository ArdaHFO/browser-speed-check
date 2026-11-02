<h1 align="center">Speedtest-1</h1>

<p align="center"><strong>Trace a transfer. Understand the timing.</strong></p>
<p align="center">An educational Flask and JavaScript prototype for browser-side download, upload and HTTP round-trip timing.</p>

<p align="center">
  <strong>English</strong> · <a href="README.tr.md">Türkçe</a><br />
  <a href="#run-the-local-interface"><strong>Run the local interface</strong></a> ·
  <a href="#inside-the-project">Features</a> ·
  <a href="#validation-and-current-limits">Current limits</a>
</p>

---

Speedtest-1 places the timing logic in the browser. JavaScript starts requests, records elapsed time and displays transfer-size and timing fields, while Flask serves the page and a small set of endpoints.

**This is an incomplete coursework prototype, not a validated bandwidth benchmark.** The original project documentation records a November 2023 deadline. This repository is a separate implementation from [speedtestFinal](https://github.com/ArdaHFO/speedtestFinal), despite the older README using that name.

## Run the local interface

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Development environment |
| Flask 3.0.0 | Server and Jinja templates |
| Browser with JavaScript | Request timing and result display |

```text
git clone https://github.com/ArdaHFO/speedtest-1.git
cd speedtest-1
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux, then run:

```text
python -m pip install Flask==3.0.0
python -m flask --app app run --host 127.0.0.1 --port 8000
```

Open [localhost:8000](http://127.0.0.1:8000). The CLI starts a local preview without using the script's all-interface, port-80 debug launch settings. The page can be inspected, but its transfer controls have the limitations below.

Only Flask is imported by this variant. [requirements.txt](requirements.txt) preserves a broader historical environment, including speedtest-cli, which these application files do not call.

## Inside the project

- **Browser-side timing.** Download and upload controls use XMLHttpRequest and elapsed browser time.
- **Transfer-size display.** A formatter converts sizes into readable units alongside the results.
- **HTTP round trip.** `GET /ping` returns `Pong` for a request-duration experiment.
- **Small Flask surface.** The app provides the main page, an alternate `/views/` page and an unfinished upload handler.
- **Local fixtures.** The repository includes image files and static transfer assets for development.

## How the experiment is organized

| UI action | Request | Current source behavior |
| --- | --- | --- |
| Download | `GET static/100MB.png` | Referenced file is absent |
| Upload | `POST /upload` | Backend route accepts GET only |
| Ping | `GET /ping` | Returns a short HTTP response |
| Refresh | Page reload | Resets the page |

An HTTP round trip measures browser-to-application latency. It includes more than network transit and is not an ICMP ping. A local server primarily exercises the local connection.

## Validation and current limits

The source files, route declarations, template requests and repository fixtures were inspected. No transfer benchmarks or runtime integration tests were run.

- The template references `static/100MB.png`, but the tracked static assets are `static/20MB.png` and `static/100MB.zip`. A filename is not proof of the actual transfer size.
- The upload handler does not import `request`, does not accept the POST method used by the browser, and expects an `uploads/` directory that is not included.
- Time conversion constants and byte-to-bit conversion are inconsistent with the displayed Mbps labels. The download path also uses an assumed size and response-string length.
- The browser can display a result after an HTTP error because it does not validate response status before calculating.
- The old public IP, Python beta version and 20 MB efficiency claim in earlier documentation are historical notes, not current deployment or benchmark guarantees.

Correcting these paths and validating the arithmetic are prerequisites for meaningful measurements. A future benchmark should report actual byte counts, elapsed seconds, caching conditions and repeat runs.

## Project map

```text
app.py                 Flask page, ping and unfinished upload route
views.py               Alternate page route
templates/index.html   Browser timing logic and size formatter
static/                Existing transfer fixtures
image/                 Additional image fixture and HTML experiment
requirements.txt       Historical dependency snapshot
```

## Development and contributions

Keep changes focused on one measurement path. Include the requested URL, HTTP status, file size and expected calculation in a bug report. Separate interface checks from actual network measurements. Use non-sensitive files when developing upload support.

## License and credits

Distributed under the [MIT license](LICENSE). Python, Flask and the declared dependencies retain their respective licenses.

