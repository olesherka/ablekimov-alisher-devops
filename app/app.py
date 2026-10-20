import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_student():
    # values come from environment variables, defaults are used if they are not set
    return {
        "Name": os.getenv("STUDENT_NAME", "Alisher"),
        "Surname": os.getenv("STUDENT_SURNAME", "Ablekimov"),
        "Group": os.getenv("STUDENT_GROUP", "IT2-2312"),
        "Student ID": os.getenv("STUDENT_ID", "37637"),
    }


def build_message(student):
    line = "=" * 32
    lines = [line, "DevOps Student Application", line, ""]
    for key, value in student.items():
        lines.append(f"{key}: {value}")
    lines.append("")
    lines.append("Application is running successfully!")
    return "\n".join(lines)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = build_message(get_student()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    # docker stop sends SIGTERM, so the app should stop by itself
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    print(build_message(get_student()), flush=True)
    port = int(os.getenv("APP_PORT", "8080"))
    print(f"Web page is available on port {port}", flush=True)
    try:
        HTTPServer(("0.0.0.0", port), Handler).serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Application stopped", flush=True)
