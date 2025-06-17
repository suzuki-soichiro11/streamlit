# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ作成
WORKDIR /app

# 依存ファイルをコピー
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリをコピー
COPY app.py ./

# ポート指定（Streamlitのデフォルト）
EXPOSE 8501

# Streamlit 起動
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
