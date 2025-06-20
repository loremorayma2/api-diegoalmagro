import subprocess
import httpx

OPENAPI_URL = "http://localhost:8000/openapi.json"
OUTPUT_MD = "docs/api-docs.md"

def download_openapi():
    print(f"Downloading OpenAPI spec from {OPENAPI_URL}...")
    response = httpx.get(OPENAPI_URL)
    response.raise_for_status()
    with open("openapi.json", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("OpenAPI spec saved as openapi.json")

def generate_markdown():
    print("Generating Markdown documentation with widdershins...")
    subprocess.run(["widdershins", "openapi.json", "-o", OUTPUT_MD], check=True)
    print(f"Markdown documentation generated at {OUTPUT_MD}")

if __name__ == "__main__":
    download_openapi()
    generate_markdown()
