<!-- endstone-professional-header:start -->
<p align="center">
  <img src="docs/assets/banner.svg" width="100%" alt="Onistone Essentials &mdash; server administration and quality-of-life tools for Endstone">
</p>
<p align="center">
  <a href="README.md">English README はこちら (English README is here)</a>
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
  <strong>Minecraft Bedrock Edition 向けの診断、安定性、QoL(生活の質)向上のためのエッセンシャルプラグイン。</strong>
</p>

<p align="center">
  <a href="#概要">概要</a> &bull;
  <a href="#使い方">使い方</a> &bull;
  <a href="#コマンドと権限">コマンド</a> &bull;
  <a href="commands.md">コマンドガイド</a> &bull;
  <a href="#インストール">インストール</a> &bull;
  <a href="https://github.com/TheNINJALLO/endstone-essentialsbds/releases">リリース</a>
</p>

## 概要

Minecraft Bedrock Edition 向けの診断、安定性、QoL(生活の質)向上のためのエッセンシャルプラグインです。このリリースは Endstone 0.11.13 および Minecraft Bedrock Dedicated Server 1.26.52.3 に対応しており、Endstone サーバーに直接インストールできる Python wheel として配布されています。

バージョン 3.5.5 は Endstone 0.11.13 / BDS 1.26.52.3 をターゲットとしており、`endstone.inventory` または `endstone.level` が利用できない場合に、Endstone のネイティブエクスポートからアイテムや位置タイプを解決することでプラグインがロードできない問題を修正した内容を保持しています。この修正は、コマンドの検出、モデレーション、テレポート、データベースヘルパー、接続ハンドラーに適用されています。

## 機能

- ゲームモード、アイテムツール、メッセージ、モデレーション、テレポートユーティリティ、診断、権限、ランクなどを網羅する幅広い必須（エッセンシャル）スイートを提供します。
- 各コマンドを個別の設定可能なモジュールとしてロードするため、不要なコマンドを無効化できます。
- チャット、参加・退出、戦闘、モニタリング、マルチワールド、サーバー安定性の動作を設定可能です。
- ランクセット、プレイヤーごとの上書き（オーバーライド）、継承、ランクの見た目を管理するためのゲーム内権限マネージャーが含まれています。
- エンティティが集中しているロード済みチャンクや、それに接続された高密度チャンクグループを見つけ出し、管理者ごとの安定したスキャン結果と、安全が確保された調査用テレポートを提供します。

## 使い方

1. 初回起動時に `plugins/onistone_essentials/` が生成され、メイン設定、コマンドモジュール設定、権限、データベース、ルールファイルが作成されます。
2. OP権限を持ったプレイヤーが `/rank` を実行すると、**Onistone Permissions** マネージャーが開きます。
3. ランクセットを選択し、権限カテゴリーを選んでからドロップダウンで権限を選択し、**Allow（許可）**、**Deny（拒否）**、または **Inherit / neutral（継承 / ニュートラル）** に設定します。
4. **Edit title, color & settings** を開くと、`Admin` などの表示タイトルの変更、Minecraftカラーの選択、括弧の切り替え、継承の設定、ウェイトやサフィックスの調整ができます。
5. 特定のプレイヤーにランクの例外処理が必要な場合は、**Manage player overrides** または `/permissions <player>` を使用します。

既存のインストールデータは初回起動時に自動的に移行されます。設定、データベース、ランク、プレイヤーの権限上書きデータは保持され、古い権限エントリーは `onistone.*` 名前空間に変換されます。

### エンティティのホットスポット（密集地）を見つける

管理者は以下の調査ワークフローを実行できます：

```text
/entityinfo hotspots
/entityinfo hotspots groups
/entityinfo hotspots detail 1
/entityinfo tp 1
```

最初のコマンドは、Endstone のロード済みアクター API によって現在公開されているアクターのオンデマンドスキャンを実行します。それ以降のコマンドは、その管理者の保存された不変のスキャン結果を再利用します。別のページを表示したり、ランク付けモードを切り替えたり、詳細を開いたり、テレポートしたりしても、背後でアクターの列挙が再度実行されることはありません。新しいサンプルが必要な場合は `/entityinfo hotspots refresh` を使用してください。

チャンク（Chunk）モードは、垂直方向のチャンク列をランク付けします。グループ（Group）モードは、斜めを含む8方向のX/Z隣接を通じて、同じディメンション内の条件を満たすチャンクを結合します。グループは接続された高密度のチャンク領域であり、半径ベースや3次元的なクラスターではありません。チャンクが連なることで広範囲に広がるグループが形成されることもあります。詳細出力（detail）では、その範囲とピークとなるチャンクが表示されます。

プレイヤーはデフォルトで除外されます。名前付き、手懐けられた、およびカスタムアクターは引き続き対象となり、カスタムアクターはバニラのエンティティリストではなく Endstone の `Mob`、`Item`、`Player` タイプによって分類されます。ドロップされたアイテムのアクターはそれぞれ1つのエンティティとしてカウントされます。公開されたスタック数量は別途報告され、エンティティカウントを増やすことはありません。

> [!NOTE]
> 結果はロードされているアクターのみをカバーします。アンロードされた/保存されたエンティティやオフラインのワールドファイルは検索されず、チャンクが強制ロードされることもありません。また、複数ティックにまたがる収集はサンプリングウィンドウであり、アトミックな（完全に同時の）ワールドスナップショットではありません。高いエンティティカウントは診断の手掛かりであって、サーバーラグの確証ではありません。

すべてのホットスポットの構文、フィルター、権限、出力のセマンティクス、および設定オプションについては、[commands.md](commands.md) を参照してください。

### 権限 GUI

- `/rank` または `/rank gui` で完全なランクセットマネージャーを開きます。
- `/permissions` でオンラインプレイヤーの上書き（オーバーライド）ピッカーを開きます。
- `/permissions <player>` で、オンラインまたは既知のオフラインプレイヤーの上書き設定を編集します。
- `/permissionslist [player]` は、読み取り専用の権限監査用として引き続き利用可能です。
- 既存の `/rank set`、`/rank perm`、`/rank prefix`、`/rank suffix`、`/rank inherit`、および直接的な `/permissions ... settrue|setfalse|setneutral` コマンドは、コンソールでの使用や自動化のために引き続き利用可能です。

## コマンドと権限

| コマンド / 使い方 | 機能 | 権限ノード |
|---|---|---|
| `/gma [player: player]` | ゲームモードをアドベンチャーに設定します！ | `onistone.command.gma` |
| `/gmc [player: player]` | 自分または他のプレイヤーのゲームモードをクリエイティブに設定します | `onistone.command.gmc` |
| `/gms [player: player]` | 自分または他のプレイヤーのゲームモードをサバイバルに設定します | `onistone.command.gms` |
| `/gmsp [player: player]` | ゲームモードをスペクテイターに設定します！ | `onistone.command.gmsp` |
| `/gmt [player: player]` | サバイバルとクリエイティブモードを切り替えます！ | `onistone.command.gmt` |
| `/iteminfo [player: player] (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotTypeInfo: slotTypeInfo] [slot: int]` | アイテムのデータを確認します！ | `onistone.command.iteminfo` |
| `/itemlore <player: player> (add)<add_lore: add_lore> <item_lore: string> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeAddLore] [slot: int]`<br>`/itemlore <player: player> (set)<set_lore: set_lore> <replaced_lore: string> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeSetLore] [slot: int]`<br>`/itemlore <player: player> (delete)<delete_lore: delete_lore> [item_lore_line: int] (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeDeleteLore] [slot: int]`<br>`/itemlore <player: player> (clear)<clear_lore: clear_lore> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeSlotClearLore] [slot: int]`<br><sub>エイリアス: `/lore`</sub> | アイテムの伝承（Lore）データを変更します！ | `onistone.command.itemlore` |
| `/itemname <player: player> (set)<set_name: set_name> <item_name: string> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeSetName] [slot: int]`<br>`/itemname <player: player> (clear)<clear_name: clear_name> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotType: slotTypeClearName] [slot: int]` | アイテムの名前データを変更します！ | `onistone.command.itemname` |
| `/itemtag <player: player> (unbreakable)<itemTag: itemTag> <is: bool> (slot\|helmet\|chestplate\|leggings\|boots\|mainhand\|offhand)[slotTypeTag: slotTypeTag] [slot: int]` | アイテムのタグを変更します！ | `onistone.command.itemtag` |
| `/more` | 手に持っているアイテムを最大スタックにします！ | `onistone.command.more` |
| `/repair [player: player]` | 手に持っているアイテムを修理します！ | `onistone.command.repair`, `onistone.command.repair.other` |
| `/spectate [player: player]` | スペクテイターではないプレイヤーの場所にワープします！ | `onistone.command.spectate` |
| `/broadcast <message: message>` | サーバー全体に通知を送信します！ | `onistone.command.broadcast` |
| `/clearchat` | チャットに100行の空行を追加します！ | `onistone.command.clearchat` |
| `/note <player: player> (clear)<note_clear: note_clear>`<br>`/note <player: player> [page: int]`<br>`/note <player: player> (remove)<note_remove: note_remove> <id: int>`<br>`/note <player: player> (add)<note_add: note_add> <message: message>` | プレイヤーに対するモデレーション用メモ（ノート）を管理します！ | `onistone.command.note` |
| `/popup <player: player> <text: message>` | カスタムポップアップメッセージを送信します！ | `onistone.command.popup` |
| `/tip <player: player> <text: message>` | カスタムTipメッセージを送信します！ | `onistone.command.tip` |
| `/toast <player: player> <title: string> <text: message>` | カスタムトーストメッセージを送信します！ | `onistone.command.toast` |
| `/blockinfo [location: pos]` | 見ているブロックの情報を表示します！ | `onistone.command.blockinfo` |
| `/blockscan (disable)[blockscan: blockscan]` | 見ているブロックの情報を継続的に表示します。 | `onistone.command.blockscan` |
| `/check <player: player> (info\|mod\|jail\|network\|world)[info: info]`<br><sub>エイリアス: `/seen`</sub> | プレイヤーのクライアント情報を確認します！ | `onistone.command.check` |
| `/entityinfo`<br>`/entityinfo list [page]`<br>`/entityinfo hotspots [page]`<br>`/entityinfo hotspots chunks [page]`<br>`/entityinfo hotspots groups [page]`<br>`/entityinfo hotspots detail <rank>`<br>`/entityinfo hotspots refresh`<br>`/entityinfo hotspots help`<br>`/entityinfo hotspots filter <chunks\|groups> <dimension> <type-or-category> [page]`<br>`/entityinfo tp <rank>` | ターゲットしたエンティティを調査したり、ロード済みのエンティティタイプのリストを表示したり、ロード済みエンティティのホットスポットを見つけて安全に調査したりします。 | 基本: `onistone.command.entityinfo`<br>スキャン/表示: `onistone.command.entityinfo.hotspots`<br>テレポート: `onistone.command.entityinfo.hotspots.teleport` |
| `/heal [player: player]` | プレイヤーの体力を全回復します！ | `onistone.command.heal`, `onistone.command.heal.other` |
| `/ping [player: player]` | サーバーのPingを確認します！ | `onistone.command.ping` |
| `/jail <player: player> <jail: string> <duration_number: int> (second\|minute\|hour\|day\|week\|month\|year)<duration_length: jail_length> [reason: message]`<br>`/jail <player: player> <jail: string> (forever)<perm_jail: perm_jail> [reason: message]` | プレイヤーを指定したエリアに投獄（ジェイル）します！ | `onistone.command.jail` |
| `/jails (list)[list_jails: list_jails]`<br>`/jails (create\|delete\|tp)<jail_action: jail_action> <jail: string> [location: pos]` | サーバーのジェイルを管理します！ | `onistone.command.jails` |
| `/nameban <player: player> <duration_number: int> (second\|minute\|hour\|day\|week\|month\|year)<duration_length: name_ban_length> [reason: message]`<br>`/nameban <player: player> (forever)<name_ban: name_ban> [reason: message]` | プレイヤーの名前をサーバーから一時的または永久にBANします！ | `onistone.command.nameban` |
| `/unnameban <player: player>` | プレイヤーのアクティブな名前BANを解除します！ | `onistone.command.unnameban` |
| `/permban <player: player> [reason: message]` | プレイヤーをサーバーから永久にBANします！ | `onistone.command.permban` |
| `/punishments <player: player> [page: int]`<br>`/punishments <player: player> (remove\|clear) <punishment_removal: remove_punishment_log>` | 指定したプレイヤーの処罰履歴を管理します！ | `onistone.command.punishments` |
| `/removeban <player: player>`<br>`/removeban <player: player> (ip)<perm_removeban: perm_removeban>` | プレイヤーのアクティブなBANを解除します！ | `onistone.command.removeban`, `onistone.command.pardon` |
| `/tempban <player: player> <duration_number: int> (second\|minute\|hour\|day\|week\|month\|year)<duration_length: ban_length> [reason: message]` | プレイヤーをサーバーから一時的にBANします！ | `onistone.command.tempban` |
| `/unjail <player: player>` | 投獄されたプレイヤーを解放します！ | `onistone.command.unjail` |
| `/unwarn <player: player> (clear)<warn_action: warn_action>`<br>`/unwarn <player: player> [id: int]` | プレイヤーの警告を削除、またはすべての警告をクリアします！ | `onistone.command.unwarn` |
| `/vanish` | サーバー上での自分の姿を完全に隠します！ | `onistone.command.vanish` |
| `/warn <player: player> <reason: string> [duration_number: int] (second\|minute\|hour\|day\|week\|month\|year)[duration_length: warn_length]` | ルール違反をしたプレイヤーに警告を与えます！ | `onistone.command.warn` |
| `/warnings <player: player> [page: int]`<br>`/warnings <player: player> (delete\|clear)<del_warn: del_warn> [id: int]` | 警告のリストを表示、またはプレイヤーから永久に削除します！ | `onistone.command.warnings` |
| `/bottom` | 自分の下にある一番近い空気のポケット（安全な空間）にワープします！ | `onistone.command.bottom` |
| `/offlinetp [player: player]`<br><sub>エイリアス: `/otp`</sub> | プレイヤーが最後にログアウトした場所にテレポートします。 | `onistone.command.offlinetp` |
| `/spawn` | スポーン地点にワープします！ | `onistone.command.spawn` |
| `/top` | 空気がある最上部のブロックにワープします！ | `onistone.command.top` |
| `/monitor (server\|packets\|disable)[debug: debug]` | サーバーのパフォーマンスをリアルタイムで監視します！ | `onistone.command.monitor` |
| `/permissions`<br>`/permissions <player: player>`<br>`/permissions <player: player> (settrue\|setfalse\|setneutral)<set_perm: set_perm> <perm: string>`<br><sub>エイリアス: `/perms`</sub> | プレイヤー上書き用のGUIを開くか、プレイヤーの権限を直接更新します。 | `onistone.command.permissions` |
| `/permissionslist`<br><sub>エイリアス: `/permslist`</sub> | グローバルまたはプレイヤー個別の権限リストを表示します！ | `onistone.command.permissionslist` |
| `/rank`<br>`/rank gui`<br>`/rank (set)<rank_set: rank_set> <player: player> <rank: string>`<br>`/rank (prefix\|suffix)<rank_meta: rank_meta> <rank: string> <meta: message>`<br>`/rank (perm)<rank_perm: rank_perm> (add\|remove)<perm_action: perm_action> <rank: string> <perm: string> [state: bool]`<br>`/rank (weight)<rank_weight: rank_weight> <rank: string> <weight: int>`<br>`/rank (inherit)<rank_inherit: rank_inherit> <rank_child: string> <rank_parent: string>`<br>`/rank (create\|delete\|list\|info)<rank_action: rank_action> [rank: message]` | ランクのGUIを開くか、ランクを直接管理します。 | `onistone.command.rank` |
| `/reloadscripts`<br><sub>エイリアス: `/rscripts`, `/rs`</sub> | サーバーのスクリプトを再読み込みします！ | `onistone.command.reloadscripts` |

## 互換性

| コンポーネント | サポートバージョン |
|---|---|
| Endstone | `0.11.13` |
| Endstone API | `0.11` |
| Bedrock Dedicated Server | `1.26.52.3` |
| Python | `>=3.10` |
| プラグインリリース | `v3.5.5` |

## インストール

対応するGitHubリリースからwheelをダウンロードしてください：

```bash
gh release download v3.5.5 --repo TheNINJALLO/endstone-essentialsbds --pattern "*.whl"
```

ダウンロードしたwheelをサーバーの `plugins/` ディレクトリにコピーし、同じプラグインの古いwheelがあれば削除してから、Endstoneを再起動します。

> [!NOTE]
> v3.5.1 以降、wheelの名前は `endstone_onistone_essentials-<version>-py3-none-any.whl` となります。Endstoneが両方のディストリビューションを検出しないように、再起動する前に古い `endstone_essentialsbds-*.whl` ファイルを削除してください。

> [!IMPORTANT]
> BDS `1.26.52.3` とともに Endstone `0.11.13` を使用してください。本番サーバーをアップグレードする前に、ワールドとプラグインデータをバックアップしてください。

## 設定とシークレット

ランタイムデータベース、ログ、ローカルの `.env` ファイル、サーバーディレクトリ、およびルートの `config.toml` ファイルは、ソースリリースから除外されています。サンプルの設定が提供されている場合は、それをローカルにコピーし、有効なトークン、パスワード、Webhook URL、およびサーバー識別子をGitの管理下（ソースコード）に含めないようにしてください。

エンティティホットスポットのデフォルト設定は、`plugins/onistone_essentials/config.json` の `modules.entity_hotspots` 配下に追加されます。存在しないキーは起動時に統合（マージ）され、既存の値が置き換えられることはありません：

```json
{
  "modules": {
    "entity_hotspots": {
      "enabled": true,
      "write_report_file": true,
      "results_per_page": 5,
      "include_players": false,
      "scan_cooldown_seconds": 15,
      "snapshot_lifetime_seconds": 300,
      "max_retained_snapshots": 16,
      "max_concurrent_scans": 1,
      "max_actors": 20000,
      "max_scan_seconds": 8.0,
      "actors_per_tick": 750,
      "dense_chunk_threshold": 10,
      "teleport_enabled": true,
      "teleport_horizontal_radius": 4,
      "teleport_vertical_radius": 32,
      "teleport_max_candidates": 512
    }
  }
}
```

また、スキャンが完了するたびに、読みやすいマークダウン形式のレポートが `plugins/onistone_essentials/entity_hotspot_report.md` にアトミックに（不可分に）置換・保存されます。これには、完全な概要と、ランク付けされたすべてのチャンクや高密度グループが含まれます。大きなレポートがサーバーのティック（処理）をブロックしないように、レポートのフォーマット処理とディスクI/Oはバックグラウンドの1つのワーカーで実行されます。ファイルの出力を無効にするには、`write_report_file` を `false` に設定してください。

Endstone 0.11.13 は、ロードされたアクターのコレクションを1つの分割不可能な操作として公開しているため、`actors_per_tick` は、その測定された取得操作の後に続くアクターの検証やプリミティブデータのキャプチャを制限することはできますが、初回のコレクション呼び出し自体を制限することはできません。アクター数、実行時間、またはアクセス制限に達した場合、結果は `INCOMPLETE` （不完全）とマークされます。

## リリース自動化

`v*` タグが作成されるたびに、[wheel release workflow](.github/workflows/wheel-release.yml) が実行され、クリーンなGitHubランナーでパッケージがビルドされ、ワークフローのアーティファクトとしてwheelが保存されたのち、対応するGitHubリリースに添付されます。
<!-- endstone-professional-header:end -->
