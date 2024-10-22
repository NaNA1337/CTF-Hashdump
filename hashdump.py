import hashlib
import itertools
import string


def brute_force_hash(target_hash, max_length=5):
    # 生成一个字符集，可以是字母、数字等
    charset = string.ascii_letters + string.digits

    # 生成所有可能的字符串组合，从1到max_length长度
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            # 拼接字符以形成一个字符串
            attempt_str = ''.join(attempt)

            # 计算这个字符串的 MD5 哈希
            attempt_hash = hashlib.md5(attempt_str.encode()).hexdigest()

            # 打印当前尝试的字符串及其哈希值（可选）
            print(f"Trying: {attempt_str} -> {attempt_hash}")

            # 检查哈希是否匹配
            if attempt_hash == target_hash:
                return attempt_str

    return None


if __name__ == "__main__":
    # 示例目标哈希值（用MD5生成）
    target = "x"  # 哈希值对应的字符串为 "x"

    # 爆破哈希值，寻找匹配的字符串
    result = brute_force_hash(target)

    if result:
        print(f"匹配的字符串: {result}")
    else:
        print("没有匹配的字符串")
