<head>
<style>
.monospaced-background {
  background-color: #7777;
  font-family: monospace;
  padding: 5px;
}
</style>
</head>

<h1 align="center">Performance-Preview</h1>

Performance-Preview — бэкенд-сервис для сбора и управления отзывами о сотрудниках с поддержкой авторизации, ролей и
базовых аналитик.

# Зависимости & Установка

<hr>
<ul>
  <li>Python (рекомендуется ≥ 3.13)</li>
  <li>PostgreSQL ≥ 17.0</li>
  <li>Redis 7.2.11</li>
</ul>

# Быстрая установка

<hr>
<ol>
  <li class="monospaced-background">git clone https://github.com/LLergibt/Performance-Preview.git</li>
  <li class="monospaced-background">cd Performance-Preview/api</li>
  <li class="monospaced-background">pip intall uv</li>
  <li class="monospaced-background">uv sync --frozen --no-cache</li>
</ol>