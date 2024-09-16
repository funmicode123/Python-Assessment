def getEncrypted(number):
   digit1 = number % 10
   number = number // 10
   digit2 = number % 10
   number = number // 10
   digit3 = number % 10
   number = number // 10
   digit4 = number % 10
   number = number // 10


   alpha1 = (digit4 + 7) % 10
   alpha2 = (digit3 + 7) % 10
   alpha3 = (digit2 + 7) % 10
   alpha4 = (digit1 + 7) % 10

   encrypted = (alpha3 * 1000) + (alpha4 * 100) + (alpha1 * 10) + alpha2
   return encrypted

def getDecrypted(number):
   digit1 = number % 10
   number = number // 10
   digit2 = number % 10
   number = number // 10
   digit3 = number % 10
   number = number // 10
   digit4 = number % 10
   number = number // 10


   alpha1 = (digit4 + 7) % 10
   alpha2 = (digit3 + 7) % 10
   alpha3 = (digit2 + 7) % 10
   alpha4 = (digit1 + 7) % 10

   beta1 = (alpha1 + 3) % 10
   beta2 = (alpha2 + 3) % 10
   beta3 = (alpha3 + 3) % 10
   beta4 = (alpha4 + 3) % 10

   decrypted = (beta1 * 1000) + (beta2 * 100) + (beta3 * 10) + beta4
   return decrypted

number = int(input("Enter a 4-digit integer: "))

getEncryptedResult = getEncrypted(number)
getDecryptedResult = getDecrypted(number)

print(f"Encrypted: {getEncryptedResult: 04d}")
print(f"Decrypted: {getDecryptedResult: 04d}")

