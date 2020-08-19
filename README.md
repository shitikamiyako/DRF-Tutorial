# DRFチュートリアルを終えてみて

## はじめに

チュートリアル各章についてのまとめはこちら

[DRFチュートリアル要旨1](https://qiita.com/shitikakei/items/0515deae9317093606fb)

[DRFチュートリアル要旨2](https://qiita.com/shitikakei/items/816f70309cd8a5125a71)

[DRFチュートリアル要旨3](https://qiita.com/shitikakei/items/6f2ea953f31a599315c1)

[DRFチュートリアル要旨4](https://qiita.com/shitikakei/items/1127c7f3328e14084d29)

[DRFチュートリアル要旨5](https://qiita.com/shitikakei/items/3fd1898d42726734d42a)

[DRFチュートリアル要旨6](https://qiita.com/shitikakei/items/d91d70d1b1255cd26a35)

ここではこれらを踏まえて簡単に思うところをまとめてみました。


## DRFをなぜ学習したのか

Reactのチュートリアルを終えてReact+Djangoで少し自分にとっては挑戦的なToDoアプリを作ろうと思い、そうなるとフロントとバックエンドでやり取りをするということはJSONを扱ったり、
そもそも非同期でやりとりをしたくなるだろうと思ったことと、ToDoアプリという仕様上、CRUDが処理の大半になるはずなので、それであるならこれを気にDRFを使ってみようと思ったから。


## DRFで楽になること・やれること

- シリアライズとデシリアライズ(フロントとバックエンドとでデータをやり取りする際に相互にデータ形式を変換する仕組み)の実装
- リクエストの識別、及びメソッドハンドラ(こちらからrequest.POSTなどと定義しなくても、request.dataと定義すればフレームワークがリクエストを識別し、どのHTTPリクエストメソッドを使うか判断する)
- レスポンスハンドラ(リクエストに応じて、フレームワークがデータをjsonで返すかHTMLフォーマットしたものを返すのかなどレスポンスを判断して適切なものを実行してくれる)
- HTTP status codesの明示化
- ブラウザでのAPI挙動の確認(デフォルトはHTMLフォーマット済みで表示) → 明示的にデータ形式を参照する場合は例えばhttp://localhost/snippets.jsonなどと叩くとJSON形式でデータを表示することが可能
- エンティティへのPermissionの作成(例えばToDoは作成したユーザーしか編集削除はできないが、閲覧は全ユーザーができるなど)
- APIルートエンドポイントの作成
- エンティティー間のリレーションの表現の定義(ハイパーリンクされたAPIなど)
- 上記までの項目を簡略化し、ルーティングまでほぼ自動で行ってくれるViewSets

## 完走してみて

学習コストはそこそこ高いと思います。
APIについての理解があるかどうかというのはもちろん、日本語の情報も少なく、それを抜きにしてもDjango特有の抽象化がより強い印象を受ける(特に6章)ので、
自分で公式のドキュメントを適宜参照していかないと理解は難しいと感じました。
かくいう私もまだ半分理解できているかどうかで、あとはとりあえず使いながらより深めていくという感じですね……

## 使う場合の懸念点

- ソーシャルログイン及びTwitterとの連携機能を使うような機能を実装するのでそれに使うdjango-allauthライブラリとの相性問題(普通に使うのにもやや癖があるので）
- APIの理解の不足(API=外部から呼び出せる機能の塊くらいの理解はある、だからTwitterのTLやGoogleMapの地図をサイトに埋め込むことができるわけなので)
- CRUD以外のアクションを少々実装する予定なのでそれがうまく定義できるか。


## 参考

[DRF公式](https://www.django-rest-framework.org/)
[Django REST Frameworkのチュートリアルをやってみた](https://saitosho.me/blog/2020-03-16-about-django-rest-framework-tutorial1/)
[Django REST frameworkで学んだことをまとめてみた](https://qiita.com/breakthrough/items/f845592961d8863a72c5)
