## Meta directory

#### docker関連

- dockerは直接実行せずutil.shから実行する

- minicondaでpython環境構築し、poetryで依存を管理する (rdkit対策)

- 実行ユーザーとコンテナユーザーのidを揃える

- slim-imageは想定外のバグが出るので本当に必要でない限り使わない

- production.ymlで本番環境と区別する

- データサイエンスならnetwork:host が楽。webappならブリッジ

## github actions

- 基本のflake8 & pytest

- sphinxはdocsブランチで自動更新する


## Project direcotory

- manage.pyでスクリプトを管理する

- `poetry install --no-root`

- Djangoライクなモジュール構成で生産性を高める

- app.pyにmockを構築する

- 中間ファイルはstateをもたらすので共有したくない

- 中間ファイルでなくキャッシュを活用する

<br>

## コードレベルの戦術


#### Config管理

- constantsとconfigを区別する

- configだけは型チェックする

- register_configでモジュール別のコンフィグを集約する

- configはyamlで永続化する

#### logger管理


#### ハイパラチューニング

後付けハイパラチューニングはカオスを招く


#### modinを活用する

rayバックエンドの並列分散pandas. RAMに乗る程度のデータサイズなら手軽で◎

```
import modin.pandas as pd
ray.init(include_dashboard=False, local_mode=False)
```
