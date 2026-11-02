This app shows estimated download and upload speeds between your browser and the app's server.

<h1 align="center">Browser Speed Check</h1>

<p align="center"><strong>Trace a transfer. Understand the timing.</strong></p>
<p align="center">A Flask and JavaScript application for browser-side download, upload and HTTP round-trip timing.</p>

<p align="center">
  <strong>English</strong> · <a href="README.tr.md">Türkçe</a><br />
  <a href="#run-the-local-interface"><strong>Run the local interface</strong></a> ·
  <a href="#inside-the-project">Features</a> ·
  <a href="#validation-and-current-limits">Current limits</a>
</p>

---

Browser Speed Check places the timing logic in the browser. JavaScript starts requests, records elapsed time and displays transfer-size and timing fields, while Flask serves the page and a small set of endpoints.

**Measurement accuracy has not been validated.** The separate [Network Transfer Check](https://github.com/ArdaHFO/network-transfer-check) explores server-side transfers alongside a browser interface.

## Run the local interface

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Development environment |
| Flask 3.0.0 | Server and Jinja templates |
| Browser with JavaScript | Request timing and result display |

```text
git clone https://github.com/ArdaHFO/browser-speed-check.git
cd browser-speed-check
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux, then run:

```text
python -m pip install Flask==3.0.0
python -m flask --app app run --host 127.0.0.1 --port 8000
```

Open [localhost:8000](http://127.0.0.1:8000). The CLI starts a local preview on port 8000. The application entry point also defaults to local access with debug mode disabled.

Only Flask is imported by this variant. [requirements.txt](requirements.txt) preserves a broader historical environment, including speedtest-cli, which these application files do not call.

## Inside the project

- **Browser-side timing.** Download and upload controls use XMLHttpRequest and elapsed browser time.
- **Transfer-size display.** A formatter converts sizes into readable units alongside the results.
- **HTTP round trip.** `GET /ping` returns `Pong` for request-duration measurement.
- **Small Flask surface.** The app provides the main page, an alternate `/views/` page and a byte-counting upload handler.
- **Local fixtures.** The repository includes image files and static transfer assets for development.

## How the application works

| UI action | Request | Current source behavior |
| --- | --- | --- |
| Download | `GET /download` | Serves the bundled `20MB.png` without caching |
| Upload | `POST /upload` | Returns the received byte count without saving an application file |
| Ping | `GET /ping` | Returns a short HTTP response |
| Refresh | Page reload | Resets the page |

An HTTP round trip measures browser-to-application latency. It includes more than network transit and is not an ICMP ping. A local server primarily exercises the local connection.

## Validation and current limits

The source has been reviewed statically. No application execution, automated tests, transfer measurements or benchmarks were performed for these changes.

- Download timing uses the actual byte size of the bundled `20MB.png`. Rates use elapsed seconds and decimal Mbps, and failed HTTP responses are not presented as results.
- The upload endpoint accepts POST, checks that a file is present and confirms the received byte count. Total request size is limited to 32 MiB including multipart overhead. No application file is saved.
- Download and ping responses disable caching. Request timeouts and browser error messages are implemented, but their behavior has not been verified by execution.
- Measurements describe the browser-to-Flask path. On localhost this is a local transfer, not an internet-provider speed test.
- Browser timing includes HTTP/application overhead. Accuracy and repeatability still require controlled measurements.

Historical public IP addresses and old payload-efficiency claims are not current deployment or benchmark guarantees.

## Project map

```text
app.py                 Flask page, download, upload and ping routes
views.py               Alternate page route
templates/index.html   Browser timing logic and size formatter
static/                Existing transfer fixtures
image/                 Additional image fixture and HTML page
requirements.txt       Historical dependency snapshot
```

## Development and contributions

Keep changes focused on one measurement path. Include the requested URL, HTTP status, file size and expected calculation in a bug report. Separate interface checks from actual network measurements. Use non-sensitive files when developing upload support.

## License and credits

Distributed under the [MIT license](LICENSE). Python, Flask and the declared dependencies retain their respective licenses.
