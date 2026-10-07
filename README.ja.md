<!-- endstone-professional-header:start -->
<p align="center">
  <img src="docs/assets/banner.svg" width="100%" alt="Onistone Essentials &mdash; server administration and quality-of-life tools for Endstone">
</p>
<p align="center">
  <a href="README.md">English README is here</a>
</p>

<p align="center">
  <a href="https://github.com/TheNINJALLO/endstone-essentialsbds/actions/workflows/wheel-release.yml"><img alt="Build" src="https://img.shields.io/github/actions/workflow/status/TheNINJALLO/endstone-essentialsbds/wheel-release.yml?branch=main&amp;style=for-the-badge&amp;logo=githubactions&amp;logoColor=white&amp;label=Build"></a>
  <a href="https://github.com/TheNINJALLO/endstone-essentialsbds/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/TheNINJALLO/endstone-essentialsbds?display_name=tag&amp;style=for-the-badge&amp;label=Release"></a>
</p>

<p align="center">
  <img alt="Endstone 0.11.13" src="https://img.shields.io/badge/Endstone-0.11.13-52b7a8?style=flat-square">
  <img alt="API 0.11" src="https://img.shields.io/badge/API-0.11-63b8ff?style=flat-square">
  <img alt="BDS 1.26.52.3" src="https://img.shields.io/badge/BDS-1.26.52.3-8b7dff?style=flat-square">
  <img alt="Python >=3.10" src="https://img.shields.io/badge/Python-%3E=3.10-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <strong>Minecraft Bedrock Edition向けの診断、安定性向上、各種便利機能を備えたEssentialsプラグイン</strong>
</p>

## 概要

Minecraft Bedrock Edition向けの診断機能、安定性、QoL(生活の質)向上のための統合エッセンシャルプラグインです。このリリースは Endstone 0.11.13 および Minecraft Bedrock Dedicated Server 1.26.52.3 に対応しており、PythonのWheel形式で配布され、Endstoneサーバーへ直接インストール可能です。

また、本プラグインは多言語（ローカライズ）対応しており、`plugins/onistone_essentials/config.json` にて `language: "ja_JP"` などと設定することでメッセージ類を日本語化できます。

## 監査レポートと注意点（Audit Report & Notes）

> [!WARNING]
> **【実績解除・チート判定に関する監査結果】**
> 本プラグインは内部的にEndstone APIおよびサーバーディスパッチャーを介してコマンド（例: `gamemode`, `tp` など）を実行します。Bedrock Serverにおいて、一部のコマンド（特にゲームモード変更等）を実行した場合、サーバーの設定(`allow-cheats`)によっては、あるいは該当コマンドのバニラの振る舞いとして **ワールドの「チートが有効」フラグがオンになり、実績解除が無効化される可能性があります**。実績を維持したサバイバルサーバーで利用する場合は、バニラのチートコマンドを呼び出す機能（`/gmc`, `/iteminfo`等）の利用に十分注意するか、別ワールドで事前にテストすることをおすすめします。
> 
> **【権限管理に関する監査結果】**
> 調査の結果、本プラグインで追加される**全てのコマンドは、デフォルトで `op` (管理者) 専用として定義されている**ことが確認されました。一般プレイヤー（メンバー）が誤って管理者用コマンドを実行できてしまう不備はありません。一般プレイヤーに解放したいコマンド（例: `/spawn`, `/ping`, `/heal` など）がある場合は、`/rank` GUI（Permissions Manager）を使用して明示的に各プレイヤーやグループに許可（Allow）を設定してください。

## 主な機能

- ゲームモード変更、アイテム操作、メッセージ管理、モデレーション、テレポート、診断、権限管理など、幅広い必須コマンドを提供します。
- 各コマンドは個別のモジュールとしてロードされ、不要なコマンドは設定で無効化できます。
- チャット、参加・退出メッセージ、戦闘、モニタリング、マルチワールド、サーバー最適化の動作を細かく設定可能です。
- ゲーム内で動作する権限マネージャー（Permissions Manager）を備え、ランクごとの権限、プレイヤー個別のオーバーライド、継承などを設定できます。
- エンティティの負荷が高いチャンクやグループを検出し、安全なテレポート調査が行える「ホットスポットスキャン機能」を搭載しています。

## 使い方

1. 初回起動時に `plugins/onistone_essentials/` が生成され、設定ファイルやデータベースなどが作成されます。
2. OP権限を持ったプレイヤーが `/rank` を実行すると、**Onistone Permissions** マネージャーが開きます。
3. ランクを選択し、権限カテゴリーから必要な権限を選んで「Allow（許可）」「Deny（拒否）」「Inherit（継承）」を設定します。
4. `/permissions <player>` を使用して、特定のプレイヤーに対する権限の例外処理（オーバーライド）を行うこともできます。

## コマンド一覧

詳しいコマンドの使い方や引数については、[commands.md (英語)](commands.md) をご参照ください。以下は一部の抜粋です。

- `/gma`, `/gmc`, `/gms`, `/gmsp`, `/gmt`: ゲームモード変更
- `/iteminfo`, `/itemlore`, `/itemname`: アイテム情報確認・編集
- `/heal`, `/spawn`, `/top`, `/bottom`, `/ping`: 各種便利・移動コマンド
- `/jail`, `/permban`, `/tempban`, `/warn`, `/punishments`: モデレーションコマンド
- `/entityinfo hotspots`: エンティティの高負荷エリア（ホットスポット）を調査

## インストール方法

GitHubのReleaseページから対応するバージョンの `.whl` ファイルをダウンロードし、サーバーの `plugins/` フォルダへ配置してサーバーを再起動してください。
※既存の古い `endstone_essentialsbds-*.whl` ファイルがある場合は、事前に削除してください。
