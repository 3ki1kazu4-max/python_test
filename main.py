import random

def main():
    print("=== じゃんけんゲーム ===")
    print("グー(g)、チョキ(c)、パー(p) のいずれかを入力してください")
    
    # ユーザーの入力
    user_input = input("あなたの手: ").lower().strip()
    
    # 入力の検証
    if user_input not in ['g', 'c', 'p', 'グー', 'チョキ', 'パー']:
        print("無効な入力です。g, c, p のいずれかを入力してください。")
        return
    
    # 入力の正規化
    if user_input == 'g' or user_input == 'グー':
        user_hand = 'グー'
    elif user_input == 'c' or user_input == 'チョキ':
        user_hand = 'チョキ'
    else:  # 'p' or 'パー'
        user_hand = 'パー'
    
    # コンピューターの手をランダムに選択
    computer_hand = random.choice(['グー', 'チョキ', 'パー'])
    
    print(f"あなた: {user_hand}")
    print(f"コンピューター: {computer_hand}")
    
    # 勝敗判定
    if user_hand == computer_hand:
        print("結果: あいこです！")
    elif (user_hand == 'グー' and computer_hand == 'チョキ') or \
         (user_hand == 'チョキ' and computer_hand == 'パー') or \
         (user_hand == 'パー' and computer_hand == 'グー'):
        print("結果: あなたの勝ちです！🎉")
    else:
        print("結果: あなたの負けです...")

if __name__ == "__main__":
    main()
