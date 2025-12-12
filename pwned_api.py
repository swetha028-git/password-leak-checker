import hashlib
import requests

API_URL = "https://api.pwnedpasswords.com/range/{}"

def sha1_hex(password: str) -> str:
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def get_pwned_count(password: str) -> int:
   
    h = sha1_hex(password)
    prefix, suffix = h[:5], h[5:]
    url = API_URL.format(prefix)
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Error querying HIBP API: {resp.status_code}")
    for line in resp.text.splitlines():
        parts = line.split(":")
        if len(parts) != 2:
            continue
        remote_suffix, count = parts[0].strip(), parts[1].strip()
        if remote_suffix.upper() == suffix:
            return int(count)
    return 0
