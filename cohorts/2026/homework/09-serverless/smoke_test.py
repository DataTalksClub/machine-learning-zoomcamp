from __future__ import annotations

from lambda_function import predict_image_url


SAMPLE_URL = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
result = predict_image_url(SAMPLE_URL)

assert 0 <= result["straight_probability"] <= 1
assert isinstance(result["straight"], bool)
print(result)
