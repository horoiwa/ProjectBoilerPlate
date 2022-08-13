=================
About
=================

|

.. contents::
  :local:

|

目的: クリーンな推論エンジンはMLプロダクトの価値を高める
===========================================================

継続的な意思決定支援システム開発のためのML推論エンジン/最適化ソルバ開発プロジェクトが近年増加しています.


しかし、ML推論エンジン/最適化ソルバ開発プロジェクトは設計の不確実性が高くコードベースが荒れがちです

- ビジネスロジック（とくにデータ周り）への依存が強いため
- R&D的な試行錯誤プロセスを多く含むため

推論エンジンの荒れたコードベースはMLプロダクトのライフサイクル全体でさまざまな問題を引き起こします


- エンジン開発時: 低い可読性によりチームへの新規メンバー投入初期コストが増大する
- アプリ開発時： 推論エンジンのアプリケーション開発チームへの引き渡しが困難になり、初デプロイが遅延する
- Ops時: 推論精度低下時の原因検証、改善コストが大きいためにやがて使われなくなる


とはいえ推論エンジンの開発PoCはしばしば厳しいdeadlineを科されるため、プロジェクト開始後にライフサイクル全体最適のためのクリーンコード意識を高く保つことが困難であることも多いかと思います。
そこで、本テンプレートでは,

- プロジェクト開始前にできる準備
- 楽な実装＝クリーンコードとなるコードレベルの導線仕込み

を主な焦点としてリポジトリレベルのクリーンコードを目指します

|


リポジトリ設計
============================

全体: M/P/Sの3階層で関心を分離する
---------------------------------------------

フラットなリポジトリ構成はエンジンに必要不可欠な要素がわかりにくいため、Meta/Project/Srcの3階層構成を採用

- Meta [M]: dockerやドキュメント, 資料など推論エンジンに直接関わらない要素

- Project [P]: 推論パッケージや検証ノートブック

- Src [S]: ソースコード

|

[M] Dockerで再現性を確保する、しかし雑なdocker環境は使いにくい
--------------------------------------------------------------------

dockerは再現性のために非常に重要ですが雑なdocker環境は面倒が多く、開発メンバに使ってもらえなくなりがちです.

- dockerを直接触らずともシェルスクリプトでコンテナログインできるようにする
- 実行ユーザーとコンテナユーザーのUID, GIDを揃えると権限回りの煩わしさが低減される
- webアプリ開発でないなら network: "host"が直感的

.. code-block::

    # cmd.sh
    cmd=$1
    uid=$(id -u)
    gid=$(id -g)
    gname=$(id -g -n)
    uname=$(id -u -n)

    if [ $cmd = "up" ]; then
      echo "Build image and up compose"
      sudo docker-compose build  \
           --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
      sudo docker-compose up -d
      echo "Finished"

    elif [ $cmd = "login" ]; then
      echo "Login to container"
      sudo docker-compose exec pyenv bash


.. code-block::

    # Dockerfile
    RUN groupadd -g $GID $GROUPNAME && \
        useradd -m -u $UID -g $GID $USERNAME
    RUN usermod -aG sudo $USERNAME

|

[M] Documentがないコードは外部委託できない
-----------------------------------------------------

プロダクト通して完全内製なら簡潔なドキュメントでもよいのですが, 外部委託が混じるなら完成度の高い（っぽく見える）ドキュメントは重要です

- ベンダの見積り価格と想定納期にがっつり影響する
- 虚無ドキュメントは技術力のあるベンダであるほど断られやすくなる
- 結果としてfirst deployが大きく遅延することがしばしば


PythonプロジェクトのドキュメントはSphinx(HTML, PDF)で作成すると多くの嬉しさがあります

- github actionsでmasterへのpushごとに自動で変更反映してgithub-pagesでドキュメント閲覧できるので管理が楽
- html,PDFで出力できるのでポータビリティが高い（=社内wikiなどと異なりベンダに渡しやすい）
- Markdown, ReStructuredTextで記述したドキュメントをそのまま取り込める (myst-parser)
- Jupyter Notebookで記述したコード付きドキュメントをそのまま取り込める (nbsphinx)
- ソースコードの__doc__を自動で取り込みドキュメント化できる (autodoc)


.. code-block::

    jobs:
      # Single deploy job since we're just deploying
      deploy:
        environment:
          name: github-pages
          url: ${{ steps.deployment.outputs.page_url }}
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v3
          - name: Setup Python
            uses: actions/setup-python@v4
            with:
              python-version: "3.9"
              architecture: x64
          - name: Install sphinx
            run: |
              python -m pip install --upgrade pip
              pip install sphinx sphinx_rtd_theme myst-parser nbsphinx
          - name: Build html
            run: |
              sphinx-apidoc -e -f -o ./docs ./project/package
              cd ../docs/
              make html
          - name: Setup Pages
            uses: actions/configure-pages@v1
          - name: Upload artifact
            uses: actions/upload-pages-artifact@v1
            with:
              path: './docs/_build/html'
          - name: Deploy to GitHub Pages
            id: deployment
            uses: actions/deploy-pages@main

|


[M] Github Actionsで楽に管理する
--------------------------------------------

- Code-CI: flake8チェック & pytest
- ML-CI: PRごとに自動で精度検証 (https://github.com/iterative/cml)
- Docs: sphinx documentのbuild & deploy

|

[P] エンジン開発ならパッケージマネージャはPoetry
--------------------------------------------------

Poetryで管理すればローカルインストール可能になるため, アプリケーション開発チームへのhand overがとても容易

- ``pip install project`` ローカルPipインストールできる
- dockerコンテナではpoetryを意識せず使えるように記述しておくと親切

.. code-block:: shell

    # editableモードでのインストール: "pip install -e ." に相当
    ENV PYTHONPATH $PYTHONPATH:/project
    RUN poetry config virtualenvs.create false && \
        poetry install --no-root

- pip install困難なライブラリを含む場合(rdkitとかmkl-numpyとか)はminicondaと併用することも

|

[P] manage.pyで非定常作業を管理する
-----------------------------------

statelessなリポジトリがベストですが、現実的にはDBセットアップや巨大データの前処理など非定常的に実行が必要なスクリプトが発生します。
これらの非定常作業スクリプトはプロジェクト直下のmanage.pyに集約することでブラックボックス化を防ぎます. (from django)

.. code-block::

    # DBの初期セットアップ
    python manage.py init_db
    # 週次バッチの実行
    python manage.py run_weekly_batch --log /log/yyyymmdd


このようなコマンドラインツールの開発では ``click`` ライブラリを使用すると楽です

|


[P] Notebookは ``yymmdd_{仮説検証の結論}.ipynb`` で保存する
----------------------------------------------------------------

- プロジェクトが積み上げた仮説検証を容易に一覧できるようにする

- もちろん1仮説検証1フォルダでもOK

.. toctree::
    :maxdepth: 2

    notebooks/220701_ファイル名は結論

|

[S] 画一的なモジュール構成で協働コストを減らす
----------------------------------------------------------------

サブモジュールごとのファイル名構成を似せる努力をするだけで協働コストが大きく低減されます (from django)

- 初見でもどこに何があるかを理解しやすく可読性が高い
- 自然に関数を役割で区切るようになりテストしやすくなる

※ディレクトリ構成図

横串モジュールの方が美しく見えますが縦串モジュールの方が管理が楽です

- モジュール単位での切り捨て/復帰が楽になるのでR&Dと相性がよい
- コンフリクト起こりにくくコードレビューが楽


※たてとよこの図解



|

[S] util.pyは気づかれないと意味が無い
---------------------------------------------

よく使うutility関数を共用化することは生産性を向上させます。
しかし、``common.py`` や ``util.py`` のように汎用的すぎるファイル名ではせっかくの便利な関数の存在にチームメンバーが気が付きません.

そこで、 ``commons/ABC_util.py`` , ``commons/XYZ_util.py`` というように具体的なファイル名を与えます。


|

コードパターン
=======================


使いにくいConfigはハードコーディングの呼び水
-------------------------------------------------



loggerは一括管理しないと意味が無い
-------------------------------------------------


StatelessなインスタンスはグローバルアクセスでOK
-------------------------------------------------


安易な中間テーブルはstatefulカオスを導入する, 永続キャッシュを活用する
-------------------------------------------------------------------------


”後でやる”チューニングでは元コードからの変更をできるだけ抑えたい
--------------------------------------------------------------------

- CPUこそパワー: 並列化はrayを使う

- pandasパフォーマンスチューニングはmodinを活用する


- ハイパラチューニングはmodel.fit()の内部で行う
