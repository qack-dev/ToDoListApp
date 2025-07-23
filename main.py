#!/usr/bin/env python3
# -*- coding: shift-jis -*-

# タスクを格納する変数
tasks = {}
# タスクを保存するファイル名
tasks_file = 'tasks.txt'

# タスクを保存する関数
def save_tasks():
    global tasks
    try:
        with open(tasks_file, 'w') as f:
            f.write(f"{tasks}")
        print("タスクをファイルに保存しました。")
    except IOError as e:
        print(f"ファイルの保存に失敗しました: {e}")

# priorityの入力を判断
def is_priority():
    priority = input("priority: ")
    if priority in ['high', 'middle', 'low']:
        return priority
    else:
        print("priorityは'high', 'middle', 'low'のいずれかを入力してください。")
        is_priority()

# タスクを追加する関数
def add():
    global tasks
    # タスクと優先度の入力を促す
    print('task名とpriority(high, middle, low)を入力してください。')
    task = input("task: ")
    priority = is_priority()
    # タスク追加
    tasks[len(tasks)] = [task, priority]
    save_tasks()

# タスクを削除・完了する関数の共通部分の関数
def delete():
    for i in range(3):
        num = input("あなたは入力を計2回間違えられます。\n> ")
        try:
            num = int(num)
            if num in tasks:
                del tasks[num]
                print(f"タスク {num} を削除しました。")
                save_tasks()
                return
            else:
                print("無効なタスク番号です。")
        except ValueError:
            print("数値を入力してください。")

# タスクを削除する関数
def remove():
    global tasks
    if not tasks:
        print("削除するタスクがありません。")
        return
    show()
    print("削除するタスク番号を選んでください。")
    delete()

def show():
    global tasks
    if not tasks:
        print("タスクはありません。")
    else:
        print("現在のタスク:")
        for key, value in tasks.items():
            print(f"    {key}: {value[0]} (priority: {value[1]})")

# タスクを完了する関数
def complete():
    global tasks
    if not tasks:
        print("完了するタスクがありません。")
        return
    show()
    print("完了するタスク番号を選んでください。")
    delete()

def main():
    # これからグローバル変数を変更することを宣言
    global tasks
    # タスクを読み込み
    with open(tasks_file, 'r') as f:
        tasks = f.read()
    # タスクを辞書に変換
    tasks = eval(tasks) if tasks else {}
    # 初期メッセージ
    a = input('タスクを入力:add,\nタスクを削除:remove,\nタスクを表示:show,\nタスクを完了:complete,\n終了:exit\n> ')
    # 条件分岐
    match a:
        case 'add':
            add()
        case 'remove':
            remove()
        case 'show':
            show()
        case 'complete':
            complete()
        case 'exit':
            print('終了します。')
            exit()
        case _:
            print("無効なコマンドです。'add', 'remove', 'show', 'complete', 'exit' のいずれかを入力してください。")
    main()

if __name__ == '__main__':
	main()
