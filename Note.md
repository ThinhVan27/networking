# 🧩 WeApRous Architecture Overview
## 🏗 Components
| Role | Script | Port | Description |
|------|---------|------|--------------|
| **Client** | (Postman / curl) | 8000 | Sends HTTP requests |
| **Proxy Server** | `start_proxy.py` | 8080 | Acts like **Nginx** — routes requests based on hostname (e.g., `app1.local`, `app2.local`) |
| **Backend Server** | `start_backend.py` | 9000 | Hosts and serves static content or RESTful apps |
| **Sample Application** | `start_sampleapp.py` | 8000 | A demo RESTful backend using **WeApRous** framework |

---

## 🧠 Concepts

- **WeApRous** → A lightweight, custom web framework (similar to **Flask**).  
  It lets you define **routes** (`@app.route('/login')`) that map to **handler functions** (called **hooks**) to process HTTP requests.

- **Proxy (Nginx-like)** →  
  Forwards requests to the correct backend based on the **`Host` header**, not the filename.  
  Example:
  - `Host: app1.local` → forward to App1 backend
  - `Host: app2.local` → forward to App2 backend

- **Backend** →  
  The actual application logic (login, hello, etc.).  
  WeApRous runs the backend on a specific IP and port (like `0.0.0.0:8000`).

- **Route & Hook** →  
  A “route” is a URL path + HTTP method pair,  
  and a “hook” (function) is what handles that request.
  ```python
  @app.route('/login', methods=['POST'])
  def login(headers, body):
      print("[SampleApp] Logging in", headers, "to", body)
  ```

---

## 🌐 Networking Notes
- `0.0.0.0` → listen on **all interfaces** (accessible from anywhere)
- `127.0.0.1` → listen on **localhost only**
- `app1.local` / `app2.local` → just **hostnames** used in the `Host` header  
  (they tell the proxy which backend to route to — not actual server names)

---

✅ **Summary**
- `WeApRous` ≈ `Flask`
- `Proxy` ≈ `Nginx`
- `Backend` ≈ Your app logic server
- `Host: appX.local` ≈ routing hint for proxy
- `0.0.0.0` ≈ all network interfaces
