import requests

response = requests.get("https://api.github.com", timeout=10)

print("狀態碼：", response.status_code)
print("Python 環境執行成功")
