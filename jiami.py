from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

from crypto.Util.Padding import pad

# 定义密钥和加密的数据
key = "123".encode('utf-8')  # 将密钥转换为字节
encrypted_data_hex = '0426b26e5972723b8761d0a1905e8a02'  # 加密后的数据（十六进制表示）

# 对密钥进行填充以符合AES的密钥长度要求
key_padded = pad(key, AES.block_size)

# 创建一个AES解密器实例，使用ECB模式
cipher_decrypt = AES.new(key_padded, AES.MODE_ECB)

# 将加密的十六进制数据转换为字节
encrypted_data = unhexlify(encrypted_data_hex)

# 使用解密器解密数据
decrypted_data = cipher_decrypt.decrypt(encrypted_data)

# 移除填充，恢复原始数据
decrypted_data_unpadded = unpad(decrypted_data, AES.block_size)

# 将字节数据转换回字符串形式
decrypted_text = decrypted_data_unpadded.decode('utf-8')

print(decrypted_text)
