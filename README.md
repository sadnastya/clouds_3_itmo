# Отчет по 3 лабораторной работе

## Задание:
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).

## Процесс выполнения работы:

* Для выполнения работы были взяты: программа на языке Python из лабораторной работы номер 2, которая выполняет преобразования с матрицами, и написанный ранее Dockerfile с инструкциями, необходимыми для создания образа контейнера.
* Далее была создана скрытая папка .github/workflows, внутри которой находится наш файлик github-actions.yml который и будет запускать прописанные действия при выполнения каких-либо условий(в данном случае это push в оснувную ветку main):
```
name: Docker Build

on:
  push:
    branches:
      - main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Build Docker Image
      run: docker build -t message-image .

    - name: Prepare Artifacts Directory
      run: mkdir -p github_workspace/artifacts

    - name: Save Docker Image
      run: docker save message-image -o github_workspace/artifacts/result.tar
      if: success()

    - name: Upload Artifacts
      uses: actions/upload-artifact@v2
      with:
        name: result
        path: github_workspace/artifacts
```
* В рамках jobs последовательно выполняется несколько шагов: checkout репозитория внутри виртуальной машины GitHub Actions(с помощью готового action, который GitHub предоставляет), сборка Docker-образа(Docker собирает образ из текущего каталога, где находится Dockerfile), создание директория "github_workspace/artifacts", где будет храниться результат сборки, сохранение собранного образа в архив result.tar и наконец загрузка Docker-образа в артефакты(тоже готовый action)

## Результат выполнения при пуше изменений в основную ветку:

Сборка выполнилась:

![](https://github.com/sadnastya/clouds_3_itmo/blob/main/images/actions_output.png)

Артефакт появился:

![](https://github.com/sadnastya/clouds_3_itmo/blob/main/images/artifact.png)
