import base64
import hashlib
import time
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


class EncryptionSystem:
    def __init__(self, master):
        self.master = master
        self.master.title(f"")
        self.master.geometry("800x540")
        self.master.resizable(False, False)

        # 每秒更新一次窗口标题上的时间
        self.update_time()
        self.base64_input = StringVar()
        self.base64_output = StringVar()
        self.md5_input = StringVar()
        self.md5_output = StringVar()
        self.sha1_input = StringVar()
        self.sha1_output = StringVar()
        self.key = None
        self.aes_input = StringVar()
        self.aes_output = StringVar()
        self.rsa_input = StringVar()
        self.rsa_decrypt_input = StringVar()
        self.rsa_public_key = StringVar()
        self.rsa_private_key = StringVar()
        self.rsa_output_l = StringVar()
        self.rsa_output_r = StringVar()

        def base64_encrypt():
            input_str = self.base64_input.get()
            encoded_bytes = base64.b64encode(input_str.encode('utf-8'))
            encoded_str = str(encoded_bytes, 'utf-8')
            self.base64_output.set(encoded_str)

        def base64_decrypt():
            encoded_str = self.base64_output.get()
            decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
            decoded_str = str(decoded_bytes, 'utf-8')
            self.base64_input.set(decoded_str)

        def md5_encrypt():
            input_str = self.md5_input.get()
            encoded_str = hashlib.md5(input_str.encode('utf-8')).hexdigest()
            self.md5_output.set(encoded_str)

        def sha1_encrypt():
            input_str = self.sha1_input.get()
            encoded_str = hashlib.sha1(input_str.encode('utf-8')).hexdigest()
            self.sha1_output.set(encoded_str)

        def aes_encrypt():
            if self.key is None:
                messagebox.showerror(title='错误', message='请先设置密钥！')
                return

            # 加密过程
            aes = AES.new(self.key, AES.MODE_ECB)
            text = self.aes_input.get().encode("utf-8")
            # 加密时必须保证长度是16的倍数，因此需要使用PKCS7填充
            text = pad(text)
            cipher_text = aes.encrypt(text)
            cipher_text = base64.b64encode(cipher_text).decode("utf-8")
            self.aes_output.set(cipher_text)

        def set_key():
            answer = messagebox.askquestion(title='设置密钥',
                                            message='请选择设置密钥的方式：\nY: 随机生成密钥\nN:手动填写密钥')
            if answer == 'yes':
                # 自动生成密钥
                self.key = get_random_key()
                aes_key_label_set.config(text=f"{self.key.hex()}")
            else:
                # 手动填写密钥
                manual_set_key()

        def manual_set_key():
            while True:
                key = simpledialog.askstring(title=' ', prompt="请输入16位十六进制密钥：")
                if key is None:
                    return  # 退出函数
                elif len(key) != 32:
                    messagebox.showerror(title='错误', message='密钥长度必须为16字节的十六进制字符串！')
                else:
                    print(key)
                    break

            # 检查密钥是否符合要求
            try:
                key = bytes.fromhex(key)
                print(key)
            except:
                messagebox.showerror(title='错误', message='密钥必须为十六进制字符串！')
                return

            self.key = key
            aes_key_label_set.config(text=f"{self.key.hex()}")

        def get_random_key():
            # 自动生成16位密钥
            key = hashlib.sha256(str(time.time()).encode('utf-8')).digest()
            return key[:16]

        def aes_decrypt():
            if self.key is None:
                messagebox.showerror(title='错误', message='请先设置密钥！')
                return

            # 解密过程
            aes = AES.new(self.key, AES.MODE_ECB)
            text = self.aes_output.get()
            cipher_text = base64.b64decode(text)
            plain_text = aes.decrypt(cipher_text).decode("utf-8")
            # 解密后需要去除填充
            plain_text = unpad(plain_text)
            self.aes_input.set(plain_text)

        def pad(s):
            # PKCS7填充
            return s + (AES.block_size - len(s) % AES.block_size) * chr(
                AES.block_size - len(s) % AES.block_size).encode()

        def unpad(s):
            # 去除PKCS7填充
            return s[:-ord(s[len(s) - 1:])]

        def rsa_encrypt():
            plain_text = self.rsa_input.get().encode('utf-8')
            public_key_str = self.rsa_public_key.get()
            public_key = RSA.importKey(public_key_str)
            cipher = PKCS1_v1_5.new(public_key)
            cipher_text = cipher.encrypt(plain_text)

            # 将字节数组转为 base64 编码的文本字符串
            cipher_text_b64 = base64.b64encode(cipher_text).decode('utf-8')
            self.rsa_output_l.set(cipher_text_b64)
            rsa_output_label_ll.insert('1.0', self.rsa_output_l.get())

        def rsa_decrypt():
            cipher_text_b64 = self.rsa_decrypt_input.get()
            private_key_str = self.rsa_private_key.get()
            private_key = RSA.importKey(private_key_str)
            cipher = PKCS1_v1_5.new(private_key)

            # 将 base64 编码的文本字符串转为字节数组
            cipher_text = base64.b64decode(cipher_text_b64.encode('utf-8'))
            plaintext = cipher.decrypt(cipher_text, None)

            # 显示明文字符串
            plaintext_str = plaintext.decode('utf-8')
            self.rsa_output_r.set(plaintext_str)
            rsa_output_label_rr.insert('1.0', self.rsa_output_r.get())

        def precautions():
            msg = '1. Base64位加密（可加密解密）\n2. MD5加密（加密不可逆）\n3. sha1加密（加密不可逆）\n4. AES加密（需要密钥才能解密）' \
                  '\n5. RSA加密（公钥加密，私钥解密）' \
                  '\n注: 1.连续进行RSA加密解密可能存在卡顿' \
                  '\n      2.AES采用AES-128加密算法'
            messagebox.showinfo(title='注意事项!', message=msg)

        base64_frame = LabelFrame(self.master, text="Base64位加密解密")
        base64_frame.place(x=30, y=30, anchor='nw')

        base64_input_label = Label(base64_frame, text="明文：")
        base64_input_label.grid(row=0, column=0, padx=5, pady=2)
        base64_input_entry = Entry(base64_frame, textvariable=self.base64_input)
        base64_input_entry.grid(row=0, column=1, padx=5, pady=2)

        base64_output_label = Label(base64_frame, text="密文：")
        base64_output_label.grid(row=1, column=0, padx=5, pady=2)
        base64_output_entry = Entry(base64_frame, textvariable=self.base64_output)
        base64_output_entry.grid(row=1, column=1, padx=5, pady=2)

        base64_encrypt_button = Button(base64_frame, text="加密", command=base64_encrypt)
        base64_encrypt_button.grid(row=2, column=0, padx=5, pady=2)
        base64_decrypt_button = Button(base64_frame, text="解密", command=base64_decrypt)
        base64_decrypt_button.grid(row=2, column=1, padx=5, pady=2)
        base64_clear_button = Button(base64_frame, text="清空",
                                     command=lambda: [self.base64_input.set(""), self.base64_output.set("")])
        base64_clear_button.grid(row=2, column=2, padx=5, pady=2)

        md5_frame = LabelFrame(self.master, text="MD5加密")
        md5_frame.place(x=43, y=175, anchor='nw')

        md5_input_label = Label(md5_frame, text="明文：")
        md5_input_label.grid(row=0, column=0, padx=10, pady=5)
        md5_input_entry = Entry(md5_frame, textvariable=self.md5_input)
        md5_input_entry.grid(row=0, column=1, padx=10, pady=5)

        md5_output_label = Label(md5_frame, text="密文：")
        md5_output_label.grid(row=1, column=0, padx=10, pady=5)
        md5_output_entry = Entry(md5_frame, textvariable=self.md5_output)
        md5_output_entry.grid(row=1, column=1, padx=10, pady=5)

        md5_encrypt_button = Button(md5_frame, text="加密", command=md5_encrypt)
        md5_encrypt_button.grid(row=2, column=0, padx=10, pady=5)
        md5_clear_button = Button(md5_frame, text="清空",
                                  command=lambda: [self.md5_input.set(""), self.md5_output.set("")])
        md5_clear_button.grid(row=2, column=1, padx=10, pady=5)

        sha1_frame = LabelFrame(self.master, text="sha1加密")
        sha1_frame.place(x=43, y=345, anchor='nw')
        sha1_input_label = Label(sha1_frame, text="明文：")
        sha1_input_label.grid(row=0, column=0, padx=10, pady=5)
        sha1_input_entry = Entry(sha1_frame, textvariable=self.sha1_input)
        sha1_input_entry.grid(row=0, column=1, padx=10, pady=5)

        sha1_output_label = Label(sha1_frame, text="密文：")
        sha1_output_label.grid(row=1, column=0, padx=10, pady=5)
        sha1_output_entry = Entry(sha1_frame, textvariable=self.sha1_output)
        sha1_output_entry.grid(row=1, column=1, padx=10, pady=5)

        sha1_encrypt_button = Button(sha1_frame, text="加密", command=sha1_encrypt)
        sha1_encrypt_button.grid(row=2, column=0, padx=10, pady=5)
        sha1_clear_button = Button(sha1_frame, text="清空",
                                   command=lambda: [self.sha1_input.set(""), self.sha1_output.set("")])
        sha1_clear_button.grid(row=2, column=1, padx=10, pady=5)

        aes_frame = LabelFrame(self.master, text="AES加密解密")
        aes_frame.place(x=350, y=15, anchor='nw')

        aes_key_label = Label(aes_frame, text="当前密钥：")
        aes_key_label.grid(row=0, column=0, padx=10, pady=5)
        aes_key_label_set = Label(aes_frame, text="None")
        aes_key_label_set.grid(row=0, column=1, padx=10, pady=5)

        aes_input_label = Label(aes_frame, text="明文：")
        aes_input_label.grid(row=1, column=0, padx=10, pady=5)
        aes_input_entry = Entry(aes_frame, textvariable=self.aes_input)
        aes_input_entry.grid(row=1, column=1, padx=10, pady=5)

        aes_output_label = Label(aes_frame, text="密文：")
        aes_output_label.grid(row=2, column=0, padx=10, pady=5)
        aes_output_entry = Entry(aes_frame, textvariable=self.aes_output)
        aes_output_entry.grid(row=2, column=1, padx=10, pady=5)

        aes_decrypt_button = Button(aes_frame, text="设置密钥", command=set_key)
        aes_decrypt_button.grid(row=3, column=0, padx=10, pady=5)
        aes_encrypt_button = Button(aes_frame, text="加密", command=aes_encrypt)
        aes_encrypt_button.grid(row=3, column=1, padx=10, pady=5)
        aes_decrypt_button = Button(aes_frame, text="解密", command=aes_decrypt)
        aes_decrypt_button.grid(row=3, column=2, padx=10, pady=5)
        aes_decrypt_button = Button(aes_frame, text="清空",
                                    command=lambda: [self.aes_input.set(""), self.aes_output.set(""),
                                                     aes_key_label_set.config(text="None")])
        aes_decrypt_button.grid(row=3, column=3, padx=10, pady=5)

        rsa_frame = LabelFrame(self.master, text="RSA加密解密")
        rsa_frame.place(x=320, y=200, anchor='nw')

        rsa_input_label = Label(rsa_frame, text="明文：")
        rsa_input_label.grid(row=0, column=0, padx=10, pady=5)
        rsa_input_entry = Entry(rsa_frame, textvariable=self.rsa_input)
        rsa_input_entry.grid(row=0, column=1, padx=10, pady=5)

        rsa_decrypt_input_label = Label(rsa_frame, text="密文：")
        rsa_decrypt_input_label.grid(row=0, column=2, padx=10, pady=5)
        rsa_decrypt_input_entry = Entry(rsa_frame, textvariable=self.rsa_decrypt_input)
        rsa_decrypt_input_entry.grid(row=0, column=3, padx=10, pady=5)

        rsa_public_key_label = Label(rsa_frame, text="公钥：")
        rsa_public_key_label.grid(row=1, column=0, padx=10, pady=5)
        rsa_public_key_entry = Entry(rsa_frame, textvariable=self.rsa_public_key)
        rsa_public_key_entry.grid(row=1, column=1, padx=10, pady=5)

        rsa_private_key = Label(rsa_frame, text="私钥：")
        rsa_private_key.grid(row=1, column=2, padx=10, pady=5)
        rsa_private_key_entry = Entry(rsa_frame, textvariable=self.rsa_private_key)
        rsa_private_key_entry.grid(row=1, column=3, padx=10, pady=5)

        rsa_output_label_l = Label(rsa_frame, text="密文：")
        rsa_output_label_l.grid(row=2, column=0, padx=10, pady=5)
        rsa_output_label_ll = Text(rsa_frame, width=20, height=10)
        rsa_output_label_ll.grid(row=2, column=1, padx=10, pady=5)

        rsa_output_label_r = Label(rsa_frame, text="明文：")
        rsa_output_label_r.grid(row=2, column=2, padx=10, pady=5)
        rsa_output_label_rr = Text(rsa_frame, width=20, height=10)
        rsa_output_label_rr.grid(row=2, column=3, padx=10, pady=5)

        rsa_encrypt_button = Button(rsa_frame, text="加密", command=rsa_encrypt)
        rsa_encrypt_button.grid(row=3, column=0, padx=10, pady=5)
        rsa_clear_button = Button(rsa_frame, text="清空",
                                  command=lambda: [self.rsa_input.set(""), self.rsa_public_key.set(""),
                                                   rsa_output_label_ll.delete('1.0', 'end')])
        rsa_clear_button.grid(row=3, column=1, padx=10, pady=5)

        rsa_encrypt_button = Button(rsa_frame, text="解密", command=rsa_decrypt)
        rsa_encrypt_button.grid(row=3, column=2, padx=10, pady=5)
        rsa_clear_button = Button(rsa_frame, text="清空",
                                  command=lambda: [self.rsa_decrypt_input.set(""), self.rsa_private_key.set(""),
                                                   rsa_output_label_rr.delete('1.0', 'end')])
        rsa_clear_button.grid(row=3, column=3, padx=10, pady=5)

        precautions_button = Button(self.master, text='点我看注意事项!', command=precautions)
        precautions_button.place(x=280, y=485, anchor='nw')

    def update_time(self):
        # 获取当前时间，更新窗口标题上的文本
        current_time = time.strftime('%b %d %Y %H:%M:%S', time.localtime())
        self.master.title(f"Encryption and Decryption Tool______Created by VelproMe______当前时间:{current_time}")
        # 继续每秒更新时间
        self.master.after(1000, self.update_time)


root = Tk()
EncryptionSystem(root)
root.mainloop()
