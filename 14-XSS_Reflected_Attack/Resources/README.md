# 14 - XSS Reflected (Data URI)

## Walkthrough

### 1. Detect the Vulnerability

Navigate to the **media page** of the application. Observe the URL structure:

```
http://<target>/?page=media&src=nsa
```

The page renders an `<object>` tag that loads an image using the `src` parameter:

```html
<object data="http://<target>/images/nsa_prism.jpg"></object>
```

The `src` query parameter is directly injected into the `data` attribute of the `<object>` tag —
a classic entry point for a **Reflected XSS** attack.

---

### 2. Confirm the Entry Point

Change the `src` value to anything arbitrary:

```
http://<target>/?page=media&src=test
```

The server returns a **404 Not Found** — confirming that whatever is passed in `src`
is reflected directly into the page without sanitization.

---

### 3. First Attempt — Inline Data URI (No Flag)

Craft a basic XSS payload using an inline `data:text/html` URI and inject it into `src`:

```
http://<target>/?page=media&src=data:text/html,<script>alert(1)</script>
```

The `alert(1)` **fires** — confirming this is a valid XSS entry point.
However, the **flag does not appear**.

> The server likely applies a filter or check on the raw payload string before serving the flag.

---

### 4. Bypass with Base64 Encoding

Encode the exact same payload in **Base64** to bypass the filter:

**Original payload:**
```html
<script>alert(1)</script>
```

**Base64 encoded:**
```
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

Inject it using the `data:text/html;base64,` URI scheme:

```
http://<target>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

The browser **decodes the Base64**, executes the script, the alert fires —
and this time the server returns the **flag**.

---

### 5. Why Base64 Works

| Attempt | Payload | Alert | Flag |
|---------|---------|-------|------|
| Inline Data URI | `data:text/html,<script>alert(1)</script>` | ✅ | ❌ |
| Base64 Data URI | `data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==` | ✅ | ✅ |

The server-side filter detects and blocks raw `<script>` strings in the `src` parameter.
By encoding the payload in Base64, the raw string never appears in the request —
the browser handles the decoding transparently, executing the script as normal.

---

### 6. Why This Is a Reflected XSS

This is a **Reflected XSS** because:

- The payload is **not stored** server-side — it lives entirely in the URL
- The `src` parameter is **reflected directly** into the `data` attribute of the `<object>` tag
- The attack requires the victim to **visit a crafted URL**
- The script executes **in the victim's browser** in the context of the application

---

## Summary

Observe `src` parameter → Confirm reflection via 404 → Test inline Data URI (alert fires, no flag) → Encode payload in Base64 → Inject via `data:text/html;base64,` → Get flag

---

## Screenshot

![Flag screenshot](xss_reflected.png)