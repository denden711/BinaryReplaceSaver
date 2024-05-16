import tkinter as tk
from tkinter import simpledialog, messagebox
import os

PROGRAM_NAME = "BinaryReplaceSaver"  # プログラム名を設定

def replace_binary_strings_and_save(file_path, replacements):
    try:
        # ファイルをバイナリモードで読み込み
        with open(file_path, 'rb') as file:
            binary_data = file.read()

        # 置換処理
        for old_string, new_string in replacements.items():
            binary_data = binary_data.replace(old_string.encode('latin1'), new_string.encode('latin1'))

        # 新しいファイル名を生成
        new_file_path = generate_new_file_path(file_path, replacements)

        # 変更されたバイナリデータを新しいファイルに書き込み
        with open(new_file_path, 'wb') as file:
            file.write(binary_data)

        messagebox.showinfo("完了", f"置換が完了しました。新しいファイルとして保存されました: {new_file_path}")
    except Exception as e:
        messagebox.showerror("エラー", f"ファイルの処理中にエラーが発生しました: {str(e)}")

def generate_new_file_path(original_file_path, replacements):
    new_file_name = replacements.get("x=0.txp", "x=0.txp").replace(".txp", ".pl3")
    directory = os.path.dirname(original_file_path)
    new_file_path = os.path.join(directory, new_file_name)
    return new_file_path

def get_replacements():
    replacements = {}
    keys = ["V=40", "F=2", "x0=30", "x=0.txp"]
    for key in keys:
        try:
            if key == "x=0.txp":
                value = simpledialog.askinteger("入力", f"{key} を置換する新しい数字を入力してください:")
                if value is not None:
                    replacements[key] = f"x={value}.txp"
            else:
                value = simpledialog.askinteger("入力", f"{key} を置換する新しい数字を入力してください:")
                if value is not None:
                    replacements[key] = f"{key.split('=')[0]}={value}"
        except Exception as e:
            messagebox.showerror("エラー", f"{key} の入力中にエラーが発生しました: {str(e)}")
    return replacements

def main():
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを非表示にする

    # プログラム名を表示
    messagebox.showinfo(PROGRAM_NAME, f"ようこそ {PROGRAM_NAME} へ")

    # ファイルパスを指定
    file_path = r"C:\Users\User\Documents\プログラム\BinaryReplaceSaver\x=BinaryReplaceSaver.pl3"
    
    if not os.path.exists(file_path):
        messagebox.showerror("エラー", f"ファイルが見つかりません: {file_path}")
        return

    replacements = get_replacements()
    
    if replacements:
        replace_binary_strings_and_save(file_path, replacements)

if __name__ == "__main__":
    main()
